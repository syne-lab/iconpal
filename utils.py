import os
import pandas as pd
import json
import re
from pathlib import Path
from policy_validator import is_valid_policy, is_valid_snippet
import random
from llm_gateway_client import LLM, LLMs
import prompt_templates
import tiktoken

graph_colors = [(212/255.0, 202/255.0, 181/255.0), (162/255.0, 155/255.0, 143/255.0), (115/255.0, 113/255.0, 113/255.0), (72/255.0, 73/255.0, 84/255.0)]


supported_models = [e.name for e in LLMs]

def get_table_data(total, syntactically_valid_count, semantically_valid_count):
    data = []
    average_total = int(total/3)
    data.append(average_total)
    average_syn_valid_count = int(syntactically_valid_count/3)
    data.append(average_syn_valid_count)
    average_percentage = format(average_syn_valid_count*100/average_total, '.2f')
    data.append(f"{average_percentage}\\%")

    if not average_total:
        data.append(0)
        data.append(0)
    else:
        average_sem_valid_count = int(semantically_valid_count/3)
        data.append(average_sem_valid_count)
        average_sem_valid_percentage = format(average_sem_valid_count*100/average_total, '.2f')
        data.append(f"{average_sem_valid_percentage}\\%")
    return data


def extract_info_from_filename(filename):
    pattern = re.compile(r'exp-(?P<example>.*)-tutorial-(?P<tutorial>.*)-grammar-(?P<grammar>.*)\.json')

    match = pattern.match(filename)

    if match:
        example = match.group('example')
        tutorial = match.group('tutorial')
        grammar = match.group('grammar')

        return (example, tutorial, grammar)
    else:
        return ("None", "None", "None")

def extract_policy(policy):
    policy_components = policy.split("\n")
    valid_components = []
    for policy_component in policy_components:
        if is_valid_snippet(policy_component):
            valid_components.append(policy_component)

    extracted_policy = "\n".join(valid_components)
    is_valid, _ = is_valid_policy(extracted_policy)
    if is_valid:
        return is_valid, extracted_policy
    return False, policy


def create_directory_path(file_path):
    dir_name = os.path.dirname(os.path.abspath(file_path))
    Path(dir_name).mkdir(parents=True, exist_ok=True)

def get_number_of_tokens(text, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(text))
    return num_tokens

def report_usage(total_input_tokens, total_output_tokens, model="GPT3_5_Turbo"):
    input_cost = {
        "GPT3_5_Turbo": 0.0015,
        "GPT4_1106_Preview" : 0.01
    }
    output_cost = {
         "GPT3_5_Turbo": 0.002,
        "GPT4_1106_Preview" : 0.03
    }
    print(f"Input Tokens: {total_input_tokens}")
    print(f"Ouput Tokens: {total_output_tokens}")
    cost = (total_input_tokens/1000)*input_cost.get(model, 0.0015) + (total_output_tokens/1000)*output_cost.get(model, 0.002)
    print(f"Cost: {cost}")

def get_file_content(file):
    if not file:
        return ""
    with open(file, 'r') as file:
        return file.read()


class Example:
    """
    data = Example.load_data("dataset")
    class_5_data = Example.filter(data, category="Class_5")

    Example.dump_json(data, "dataset/data.json")
    """
    def __init__(self, id, text, policy, category):
        self.id = id
        self.text = text
        self.policy = policy
        self.category = category
        try:
            self.syntax_valid = self.is_syntactially_valid()
        except:
            self.syntax_valid = False

    def to_dict(self, **kwargs):
        fields = kwargs.get("fields", ["id", "text", "policy", "category", "syntax_valid"])

        data = {}
        for field in fields:
            data[field] = getattr(self, field)
        return data

    def is_syntactially_valid(self):
        is_valid, _ = is_valid_policy(self.policy)
        return is_valid

    @classmethod
    def get_categories(cls, examples):
        categories = set()
        for example in examples:
            category = example.category if isinstance(example, Example) else example["category"]
            categories.add(category)
        return categories

    @staticmethod
    def filter(examples, category):
        return [example for example in examples if example.category==category]

    @staticmethod
    def dump_json(examples, file, **kwargs):
        create_directory_path(file)
        with open(file, 'w') as json_file:
            json.dump([example.to_dict(**kwargs) for example in examples], json_file, indent=4)

    @classmethod
    def dump_categorized_data(cls, examples, file):
        create_directory_path(file)
        categories = cls.get_categories(examples)
        data = {}
        for category in categories:
            data[category] = {}
            data[category]["policies"]=[e.text for e in cls.filter(examples, category)]
            data[category]["count"] = len(data[category]["policies"])
        with open(file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def dump_text(examples, file):
        create_directory_path(file)
        with open(file, 'w') as text_file:
            for example in examples:
                text_file.write(example.text + "\n\n")

    @classmethod
    def from_dict(cls, data):
        return cls(data["text"], data["policy"], data["category"])

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    @staticmethod
    def load_data_from_json(file):
        with open(file, "r") as json_file:
            examples = json.load(json_file)
            return [Example(example["id"], example["text"], example["policy"], example["category"]) for example in examples]

    @staticmethod
    def load_data_from_csv(file_path):
        """
        Load data from csv files. The csv files must contain
        two columns - 'Natural Language' and 'Maverick Translation'
        """
        if os.path.isdir(file_path):
            csv_files = os.listdir(file_path)
            directory_path = file_path
        else:
            csv_files = [os.path.basename(file_path)]
            directory_path = os.path.dirname(file_path)

        data = []
        id=1
        for csv_file in csv_files:
            if csv_file.endswith(".csv"):
                file_path = os.path.join(directory_path, csv_file)
                category = csv_file.split(".")[0]

                data_frame = pd.read_csv(file_path)
                for _, row in data_frame.iterrows():
                    category = row.get("Category") or category
                    example = Example(id, row["Natural Language"], row["Maverick Translation"], category)
                    data.append(example)
                    id+=1
        return data

    @classmethod
    def get_learning_examples(cls, examples, category, excluded_examples=[], count=1):
        excluded_example_ids = [example["id"] for example in excluded_examples]
        
        filtered_examples = cls.filter(examples, category)
        filtered_examples = [example for example in filtered_examples if example.id not in excluded_example_ids]
        return random.sample(filtered_examples, count)

    @classmethod
    def get_learning_examples_from_each_category(cls, examples, count_per_category):
        learning_examples = []
        for category in sorted(cls.get_categories(examples)):
            filtered_examples = cls.filter(examples, category)
            sampled_indices = random.sample(range(len(filtered_examples)), count_per_category)
            for index in sampled_indices:
                learning_examples.append(filtered_examples[index])
        return learning_examples

    @classmethod
    def get_random_learning_examples(cls, examples, count=1):
        return random.sample(examples, count)


    @classmethod
    def get_query_data(cls, all_data, learning_examples, percentage):
        result = []
        learning_example_ids = [example.id for example in learning_examples]
        query_data = [example for example in all_data if example.id not in learning_example_ids]

        for category in sorted(cls.get_categories(all_data)):
            filtered_examples = cls.filter(query_data, category)
            example_count = int(percentage*len(filtered_examples)/100)
            selected_examples = random.sample(filtered_examples, example_count)
            result.extend(selected_examples)
        return result


class Prompt:
    @staticmethod
    def generate_learning_prompt(example=None, tutorial=None, grammar=None):
        prompt = LearningPrompt(id=f"prompt-example-{example}-tutorial-{tutorial}-grammar-{grammar}")
        if example == "random":
            prompt.examples = Example.get_learning_examples(random=True)
        elif example == "from-each-category":
            prompt.examples = Example.get_learning_examples(random=False)
        
        if tutorial:
            prompt.tutorial = f"dataset/raw_data/{tutorial}"
        if grammar:
            prompt.grammar = f"dataset/raw_data/{grammar}"
        
        return prompt
    
    @staticmethod
    def generate_learning_prompts(examples, grammar, tutorial):
        prompt_classes = LearningPrompt.get_prompt_classes()
        prompts = []
        for prompt_class in prompt_classes:
            prompt = LearningPrompt(id="-".join(map(str, sorted(list(prompt_class)))))
            if "examples" in prompt_class:
                prompt.examples = examples
            if "grammar" in prompt_class:
                prompt.grammar = grammar
            if "tutorial" in prompt_class:
                prompt.tutorial = tutorial
            prompts.append(prompt)
        return prompts


    @staticmethod
    def generate_query_prompts(examples):
        prompts = []
        for example in examples:
            prompts.append(QueryPrompt(id=example.id, text=example.text, policy=example.policy))
        return prompts

    @staticmethod
    def dump_json(prompts, file, **kwargs):
        create_directory_path(file)
        with open(file, 'w') as json_file:
            json.dump([prompt.to_dict(**kwargs) for prompt in prompts], json_file, indent=4)


class QueryPrompt(Prompt):
    def __init__(self, id, text, policy):
        self.id = id
        self.text = text
        self.policy = policy
    
    def to_dict(self, **kwargs):
        return {
            "id": self.id,
            "text": self.text,
            "policy": self.policy
        }


class LearningPrompt(Prompt):
    def __init__(self, id, examples=None, grammar=None, tutorial=None):
        self.id = id
        self.grammar = grammar
        self.tutorial = tutorial
        self.examples = examples

    def to_dict(self, **kwargs):
        if self.examples and "examples" in kwargs:
            examples = kwargs["examples"]
        else:
            examples = [example.to_dict() for example in self.examples] if self.examples else None

        return {
            "id": self.id,
            "grammar": self.grammar,
            "tutorial": self.tutorial,
            "examples": examples
        }

    @staticmethod
    def get_prompt_classes():
        prompt_components = ["examples", "grammar", "tutorial"]
        prompt_classes = set()
        n = len(prompt_components)
        for i in range(2**n):
            prompt_class = set()
            for j in range(n):
                if (i >> j) & 1:
                    prompt_class.add(prompt_components[j])
            prompt_classes.add(frozenset(prompt_class))
        return prompt_classes


class PolicyTranslator:
    def __init__(self, model, learning_data, dry_run=True, temperature=1, top_p=1, max_tokens=256, debug_file=None, endpoint="http://172.17.0.1:31211"):
        self.input_tokens = 0
        self.output_tokens = 0

        self.debug_file = debug_file
        self.dry_run = dry_run

        if not self.dry_run:
            self.llm = LLM(LLMs[model], endpoint)
            self.session = self.llm.create_session()
            self.session.default(max_tokens=max_tokens, temperature=temperature, top_p=top_p)

        learning_prompt = prompt_templates.system_learn_from_context
        learning_prompt += ("Grammar in extended Backus–Naur (EBNF) form: \n" + str(learning_data["grammar"]) + "\n\n")
        learning_prompt += ("Tutorial: \n" + str(learning_data["tutorial"]) + "\n\n")
        learning_prompt += "Examples:\n"
        if learning_data["examples"]:
            for example in learning_data["examples"]:
                learning_prompt += ("Text:\n" + example["text"] + "\n")
                learning_prompt += ("Policy:\n" + example["policy"] + "\n\n")
        else:
            learning_prompt += "No examples provided\n\n"
        self.learning_prompt = learning_prompt

    def translate_text_to_policy(self, text, old_translation=None, retry_instruction=None):
        prompt = prompt_templates.user_query_text_to_policy + "\"" + text + "\"\n"
        if self.debug_file:
            self.debug_file.write(self.learning_prompt)
            if retry_instruction:
                self.debug_file.write(retry_instruction)
            self.debug_file.write(prompt)
            self.debug_file.flush()
        self.input_tokens += get_number_of_tokens(self.learning_prompt)
        self.input_tokens += get_number_of_tokens(prompt)
        self.input_tokens += get_number_of_tokens(old_translation)
        self.input_tokens += get_number_of_tokens(retry_instruction)
        output = ""
        if not self.dry_run:
            self.session.clear_context()
            messages = [
                {"role": "system", "content": self.learning_prompt},
                {"role": "user", "content": prompt_templates.user_query_text_to_policy + '"' + text + '"\n'},
            ]
            if old_translation:
                messages.append({"role": "assistant", "content": old_translation})
                messages.append({"role": "user", "content": retry_instruction})
            result = self.session.inference(messages)
            if result:
                output = result["content"]
        if output:
            self.output_tokens += get_number_of_tokens(output)
        else:
            self.output_tokens += 50
        _, output = extract_policy(output)
        return output


class DataCategorizer:
    def __init__(self, model, max_tokens=256, temperature=1, top_p=1, dry_run=True, debug=False):
        self.input_tokens = 0
        self.output_tokens = 0

        self.dry_run = dry_run
        self.debug = debug

        if not self.dry_run:
            self.llm = LLM(LLMs[model])
            self.session = self.llm.create_session()
            self.session.set_max_tokens(max_tokens)
            self.session.set_temperature(temperature)
            self.session.set_top_p(top_p)
        self.learning_prompt = prompt_templates.use_category_definitions
        category_definitions = get_file_content("dataset/raw_data/category_definitions.json")
        self.learning_prompt += category_definitions

    def get_category(self, text):
        prompt = prompt_templates.categorize_dataset
        prompt += text

        self.input_tokens += get_number_of_tokens(prompt)

        if self.debug:
            print(self.learning_prompt)
            print(prompt)
        output = ""  

        if not self.dry_run:
            self.session.clear_context()
            result = self.session.inference(
                [
                    {"role": "system", "content": self.learning_prompt},
                    {"role": "user", "content": prompt},
                    
                ]
            )
            if result:
                output = result["content"]

        if output:
            self.output_tokens += get_number_of_tokens(output)
        else:
            self.output_tokens += 50
        return output