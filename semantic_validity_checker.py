import argparse
import random
import json
import threading
import os
from llm_gateway_client import LLM, LLMs
import prompt_templates
import time
from utils import Example, LearningPrompt, get_number_of_tokens, supported_models, report_usage, get_file_content

input_tokens = 0
output_tokens = 0
validation_count = 0
improvement_count = 0

def extract_policy_logic(policy):
    policy_components = policy.split("\n")
    policy_components = [component for component in policy_components if component.startswith("If")]
    policy = "\n".join(policy_components)
    return policy

class SemanticValidator:
    def __init__(self, model, learning_prompt, debug_file=None, dry_run=False, endpoint="http://llm-gateway:31211"):
        self.input_tokens = 0
        self.output_tokens = 0
        self.dry_run = dry_run
        self.learning_prompt = learning_prompt
        self.debug_file = debug_file
        
        self.llm = LLM(LLMs[model], endpoint)
        self.session = self.llm.create_session()
        self.session.default(max_tokens=256, temperature=0.7, top_p=1.0)

    def translate_policy_to_text(self, policy):
        learning_data = self.learning_prompt.to_dict()
        context = """\nYou are a formal policy to plain text translator. I will teach you how to translate a formal policy to plain text with a tutorial and some examples.\n"""
        context += ("Tutorial: \n" + str(learning_data["tutorial"]) + "\n\n")
        context += "Examples:\n"
        if learning_data["examples"]:
            for example in learning_data["examples"]:
                context += ("Policy:\n" + example["policy"] + "\n\n")
                context += ("Text:\n" + example["text"] + "\n")

        else:
            context += "No examples provided\n\n"
        
        prompt = prompt_templates.user_query_policy_to_text + "\"" + policy + "\"\n"
        self.input_tokens += get_number_of_tokens(prompt)
        self.input_tokens += get_number_of_tokens(context)
        output = ""
        if not self.dry_run:
            self.session.clear_context()
       
            result = self.session.inference(
                [
                    {"role": "system", "content": context},
                    {"role": "user", "content": prompt}
                ]
            )
            if result:
                output = result["content"]
        if output:
            self.output_tokens += get_number_of_tokens(output)
        else:
            self.output_tokens += 50

        if self.debug_file:
            self.debug_file.write("\nContext:\n" + context)
            self.debug_file.write("Prompt:\n" + prompt)
            self.debug_file.write("Output:\n" + output)

        return output

    def is_semantically_valid_v2(self, actual_policy_text, generated_policy_text):
        prompt = "Are the following two policies equivalent? Consider only action and condition. Answer Yes or No\n\n"
        prompt += "1: " + actual_policy_text + "\n"
        prompt += "2: " + generated_policy_text + "\n"
        self.input_tokens += get_number_of_tokens(prompt)
        output = "No"

        if not self.dry_run:
            self.session.clear_context()
            response = self.session.inference([
                {"role": "user", "content": prompt}
            ])
            output = response["content"]
        self.output_tokens += get_number_of_tokens(output)
        
        if self.debug_file:
            self.debug_file.write("\nPrompt:\n" + prompt)
            self.debug_file.write("Output:\n" + output)

        return output.strip(" .").lower() in ["yes", "true", "correct"]


def perform_semantic_validation(file, args, all_data, lock):
    tutorial = get_file_content(f"dataset/raw_data/policy_tutorial_simplified.md")
    id = file.split("/")[-1].split(".")[0]
    learning_prompt = LearningPrompt(id,tutorial=tutorial)
    debug_file = open(f"{file.replace('output', 'debug')}-sem-val.debug", 'w')
    semantic_validator = SemanticValidator(args.llm, learning_prompt=learning_prompt, debug_file=debug_file, dry_run=args.dry_run)

    count = 0
    improvement = 0
    with open(file, 'r') as in_file:
        objects = json.load(in_file)
        for obj in objects:
            if not args.override and "semantically_valid" in obj:
                continue
            
            syntactically_valid = False
            for r in range(5):
                if not f"syntactically_valid_{r}" in obj:
                    break
                else:
                    syntactically_valid = obj[f"syntactically_valid_{r}"]
            if syntactically_valid and (args.override or "semantically_valid" not in obj):
                try:
                    if args.wrong_only and obj["semantically_valid"] == obj["valid"]:
                        continue
                except Exception as e:
                    print(obj)
                    raise e
                semantic_validator.learning_prompt.examples = Example.get_learning_examples(all_data, obj["category"], excluded_examples=[obj], count=3)
                obj["generated_policy_text"] = semantic_validator.translate_policy_to_text(obj["generated_policy"])
                obj["semantically_valid"] = semantic_validator.is_semantically_valid_v2(obj["text"], obj["generated_policy_text"])
                if obj["semantically_valid"] == obj["valid"]:
                    improvement += 1
                count += 1
    if not args.dry_run:
        with open(file, 'w') as out_file:
            json.dump(objects, out_file, indent=4)

    debug_file.close()
    lock.acquire()
    global input_tokens
    global output_tokens
    global validation_count
    global improvement_count
    validation_count += count
    improvement_count += improvement
    input_tokens += semantic_validator.input_tokens
    output_tokens += semantic_validator.output_tokens
    lock.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Semantic Validity Checker")
    parser.add_argument('-m', '--llm', required=True, type=str, default="",
                        choices=supported_models,
                        help='Percentage of examples to include for trainging from each class of dataset')
    parser.add_argument('-d', '--directory', type=str, help='File contianing list of json objects.')
    parser.add_argument('-f', '--file', type=str, help='File contianing list of json objects.')
    parser.add_argument('--dry-run', action="store_true", help="Don't actually run the translator, just print prompts to console")
    parser.add_argument('-o', '--override', action="store_true", help="Override previous validation")
    parser.add_argument('-w', '--wrong-only', action="store_true", help="Validate wrong validations only")

    args = parser.parse_args()
    random.seed(1)
    start_time = time.time()

    files = []
    if args.directory:
        try:
            files = [f"{args.directory}/{file}" for file in os.listdir(args.directory)]
        except:
            pass
    elif args.file:
        files = [args.file]
    
    all_data = Example.load_data_from_json("dataset/processed_data/manually_categorized_dataset.json")

    lock = threading.Lock()
    threads = []
    for file in files:
        if file.endswith(".csv"):
            continue
        t = threading.Thread(target=perform_semantic_validation, args=(file, args, all_data, lock))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"Total number of validations: {validation_count}")
    report_usage(input_tokens, output_tokens)
    print(f"Average input tokens: {input_tokens/(validation_count+0.00001)}")
    
    end_time = time.time()
    print(f"Total time: {int(end_time - start_time)} seconds")
    print(f"Improvement: {improvement_count} out of {validation_count}")
