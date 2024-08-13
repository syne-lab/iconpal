
import argparse

from pathlib import Path
from utils import (
    Example, Prompt, LearningPrompt, PolicyTranslator, supported_models,
    get_file_content, report_usage
)
import time
import json
import os
import random
from experiment_configs import configs
import traceback, sys
from policy_validator import is_valid_policy

import sys


if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser("Generate policy from text")

    parser.add_argument('-p', '--percentage', default=100, type=int, help='Percentage of examples to include for query')
    parser.add_argument('-m', '--llm', type=str, default="Llama_2_7b",
                        choices=supported_models,
                        help='LLM model')
    parser.add_argument('-e', '--endpoint', type=str, default="http://llm-gateway:31211", help='LLM endpoint')
    parser.add_argument('-c', '--config', type=str, required=True, choices=list(configs.keys()), help="Experiment config")
    parser.add_argument('-r', '--repeat-number', type=int, required=True, help="Repeat number")
    parser.add_argument('--dry-run', action="store_true", help="Don't actually run the translator, just print prompts to console")
    parser.add_argument('--override', action="store_true", help="Override existing results")
    parser.add_argument('--reprompt-count', type=int, default=0, help="Number of reprompt with error messages")
    parser.add_argument('-b', '--base-directory', type=str, default=".", help="Base directory")



    args = parser.parse_args()

    random.seed(args.repeat_number)

    debug_directory = f"{args.base_directory}/evaluations/{args.config}/debug/{args.llm}/p{args.percentage}/r{args.repeat_number}"
    debug_path = Path(debug_directory)
    debug_path.mkdir(parents=True,exist_ok=True)

    output_directory = f"{args.base_directory}/evaluations/{args.config}/output/{args.llm}/p{args.percentage}/r{args.repeat_number}"
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)

    all_data = Example.load_data_from_json("dataset/processed_data/manually_categorized_dataset.json")

    random_learning_examples = Example.get_random_learning_examples(all_data, count=8)
    learning_examples_from_each_category = Example.get_learning_examples_from_each_category(all_data, count_per_category=1)
    
    llm_categorized_data = Example.load_data_from_json("dataset/processed_data/llm_categorized_dataset.json")
    learning_examples_from_each_category_in_llm_categorized_data = Example.get_learning_examples_from_each_category(llm_categorized_data, count_per_category=1)

    prompts = []

    experiment_config = configs[args.config]
 
    total_input_tokens = 0
    total_output_tokens = 0
    for config in experiment_config:
        
        examples = []
        if config["examples"] == "random":
            examples = random_learning_examples
        elif config["examples"] == "human-categorized":
            examples = learning_examples_from_each_category
        elif config["examples"] == "llm-categorized":
            examples = learning_examples_from_each_category_in_llm_categorized_data
        else:
            examples = Example.get_learning_examples_from_each_category(all_data, count_per_category=config["examples"])
        tutorial = None
        if config["tutorial"]:
            tutorial = get_file_content(f"dataset/raw_data/{config['tutorial']}")
        
        grammar = None
        if config["grammar"]:
            grammar = get_file_content(f"dataset/raw_data/{config['grammar']}")
        
        temperature = config["temperature"]
        id = f"example-{config['examples']}-tutorial-{config['tutorial']}-grammar-{config['grammar']}"
        if temperature!=0.5:
            id = id + f"-tmp-{temperature}"

        print(f"Running for {id}")

        learning_prompt = LearningPrompt(id, examples=examples, tutorial=tutorial, grammar=grammar)
        prompts.append(learning_prompt)

        query_data_set = Example.get_query_data(all_data=all_data, learning_examples=examples, percentage=args.percentage)
        
        debug_file = open(f"{debug_directory}/exp-{id}.txt", 'w')

        output_filename = f"{output_directory}/exp-{id}.json"
        outputs = []
        try:
            output_file_size = os.stat(output_filename).st_size
            if(output_file_size>2):
                try:
                    print(f"{output_filename} exists.")
                    with open(output_filename, 'r') as output_file:
                        outputs = json.load(output_file)
                    for output in outputs:
                        if not output.get("generated_policy") or args.override:
                            if config["examples"] == "random":
                                learning_prompt.examples = random.sample(random_learning_examples, 1)
                            else:
                                learning_prompt.examples = [ex for ex in examples if ex.category == output["category"]]
                            translator = PolicyTranslator(args.llm, learning_prompt.to_dict(), dry_run=args.dry_run, temperature=temperature, debug_file=debug_file, endpoint=args.endpoint)
                            generated_policy = translator.translate_text_to_policy(output["text"])
                            output["generated_policy"] = generated_policy
                            syntactically_valid, reason = is_valid_policy(generated_policy)
                            output["syntactically_valid_0"] = syntactically_valid
                            retry_count=1
                            while (not syntactically_valid and retry_count <= args.reprompt_count):
                                retry_count += 1
                                failure_message = "You generated following invalid policy.\n\n" + generated_policy + "\n\nReason:\n" + reason + "\n\n"
                                generated_policy = translator.translate_text_to_policy(output["text"], failure_message)
                                output["generated_policy"] = generated_policy
                                syntactically_valid, reason = is_valid_policy(generated_policy)
                                output[f"syntactically_valid_{retry_count-1}"] = syntactically_valid

                            print(output, flush=True)
                    if not args.dry_run:
                        outputs = [o for o in outputs if o["id"] in [q.id for q in query_data_set]]
                        with open(output_filename, 'w') as output_file:
                            json.dump(outputs, output_file, indent=4)
                except Exception as e:
                    print(e)
                    traceback.print_exc(file=sys.stdout)
        except Exception as e:
            pass


        existing_ids = [o["id"] for o in outputs]
        query_data_set = [q for q in query_data_set if q.id not in existing_ids]
        try:
            count = 0
            for query_data in query_data_set:
                print("Count: " + str(count), flush=True)
                count += 1
                output = {
                    "id": query_data.id,
                    "text": query_data.text,
                    "policy": query_data.policy,
                    "category": query_data.category
                }
                if config["examples"] == "random":
                    learning_prompt.examples = random.sample(random_learning_examples, 1)
                else:
                    learning_prompt.examples = [ex for ex in examples if ex.category == query_data.category]
                
                translator = PolicyTranslator(args.llm, learning_prompt.to_dict(), dry_run=args.dry_run, debug_file=debug_file, temperature=temperature, endpoint=args.endpoint)
                generated_policy = translator.translate_text_to_policy(query_data.text)
                output["generated_policy"] = generated_policy
                syntactically_valid, reason = is_valid_policy(generated_policy)
                output["syntactically_valid_0"] = syntactically_valid
                retry_count=1
                while (not syntactically_valid and retry_count <= args.reprompt_count):
                    retry_count += 1
                    retry_instruction = (
                        "Your translation is invalid due to following reason.\n"
                        + "Reason:\n"
                        + reason
                        + "\nPlease try again."
                    )
                    generated_policy = translator.translate_text_to_policy(query_data.text, old_translation=generated_policy, retry_instruction=retry_instruction)
                    output["generated_policy"] = generated_policy
                    syntactically_valid, reason = is_valid_policy(generated_policy)
                    output[f"syntactically_valid_{retry_count-1}"] = syntactically_valid

                print(output, flush=True)
                outputs.append(output)

                # Intermediate save of outputs
                if not args.dry_run:
                    with open(output_filename, 'w') as output_file:
                        json.dump(outputs, output_file, indent=4)

                total_input_tokens += translator.input_tokens
                total_output_tokens += translator.output_tokens

        except  KeyboardInterrupt:
            print("Keyboard interrupt")
        except Exception as e:
            print("ERROR: " + str(e))
            traceback.print_exc(file=sys.stdout)
        finally:
            if not args.dry_run:
                with open(output_filename, 'w') as output_file:
                    json.dump(outputs, output_file, indent=4)
            debug_file.close()

        

    report_usage(total_input_tokens, total_output_tokens, args.llm)

    Prompt.dump_json(prompts, f"{args.base_directory}/evaluations/{args.config}/prompts/{args.llm}/p{args.percentage}/r{args.repeat_number}/prompts.txt")
    end_time = time.time()
    print(f"Total time: {int(end_time - start_time)} seconds")
