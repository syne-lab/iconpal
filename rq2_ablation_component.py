
import argparse
import os
import json
from utils import get_table_data, supported_models, extract_info_from_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate policy from text")

    parser.add_argument('-m', '--llm', type=str, default="GPT3_5_Turbo",
                        choices=supported_models,
                        help='LLM model')
    args = parser.parse_args()
    dirs = [
        f"evaluations/ablation/output/{args.llm}/p100/r1",
        f"evaluations/ablation/output/{args.llm}/p100/r2",
        f"evaluations/ablation/output/{args.llm}/p100/r3"
    ]
    files = []
    for dir in dirs:
        files = files + [f"{dir}/{file}" for file in os.listdir(dir)]
 
    data = [[]]
    data[-1].append("Components, Tutorial, Grammar")
    data[-1].append("Total")
    data[-1].append(f"Syntactically Valid")
    data[-1].append("Semantically Valid")
    components = [
        "example:yes,tutorial:yes,grammar:yes",
        "example:yes,tutorial:yes,grammar:no",
        "example:yes,tutorial:no,grammar:yes",
        "example:yes,tutorial:no,grammar:no",
        "example:no,tutorial:yes,grammar:yes",
        "example:no,tutorial:yes,grammar:no",
        "example:no,tutorial:no,grammar:yes",
        "example:no,tutorial:no,grammar:no"
    ]

    syntactically_valid_count = {}
    semantically_valid_count = {}
    semantically_valid_count_llm = {}
    total = {}
    validation_count = {}
    for component in components:
        syntactically_valid_count[component] = 0
        semantically_valid_count[component] = 0
        semantically_valid_count_llm[component] = 0
        total[component] = 0
        validation_count[component] = 0
    for file in files:
        example, tutorial, grammar = extract_info_from_filename(file.split('/')[-1])
        example = example.split("example-")[-1]
        if example == "0":
            example = "example:no"
        else:
            example = "example:yes"
        
        if tutorial == "None":
            tutorial = "tutorial:no"
        else:
            tutorial = "tutorial:yes"
        
        if grammar == "None":
            grammar = "grammar:no"
        else:
            grammar = "grammar:yes"

        component = f"{example},{tutorial},{grammar}"
        with open(file, 'r') as in_file:
            try:
                objects = json.load(in_file)
            except:
                continue
            
            total_count = len(objects)
            if total_count < 1:
                print(f"{file} does not have any data")
                continue

            for object in objects:
                total[component] +=1
                if "semantically_valid" in object:
                    if object.get("semantically_valid", False):
                        semantically_valid_count_llm[component] += 1
                if "valid" in object:
                    validation_count[component] += 1
                    if object.get("valid", False):
                        semantically_valid_count[component] += 1
                if object.get(f"syntactically_valid_0", False):
                    syntactically_valid_count[component] += 1
                

    for component in  components:
        data.append([])
        parts = component.split(",")
        for part in parts:
            _, value = part.split(":")
            if value == "yes":
                value = "\\cmark"
            else:
                value = "\\xmark"
            data[-1].append(value)

        data[-1].extend(get_table_data(total[component], syntactically_valid_count[component], semantically_valid_count[component]))  

    table = """
\\begin{table}

\\centering
\\caption{Effectiveness of different components in learning prompt. Model: GPT 3.5, Temperature: 0.5, Tutorial: Full, Example Selection: Manual, E.: Example, T.: Tutorial, G.: Grammar, Syn.: Syntax, Sem: Semantic, r$_{syn}$: Syntax validity percentage w.r.t. total count, r$_{sem}$: Semantic validity percentage w.r.t. total count}
\\label{tab:rq2-ablation-component}
\\begin{tabular}{|c|c|c|c|c|c|c|c|}
\\hline
\\multicolumn{3}{|c|}{\\textbf{Components}} & \\multirow{2}{*}{\\textbf{Total}} & \\multicolumn{2}{|c|}{\\textbf{Syn. Validation}} & \\multicolumn{2}{|c|}{\\textbf{Sem. Validation}}  \\\\
\cline{1-3} \cline{5-8}
E. & T. & G. & & Count & r$_{syn}$ & Count & r$_{sem}$ \\\\
\\hline
"""
    for d in data[1:]:
        table = table + " & ".join(map(lambda x: str(x), d)) + "\\\\\n"
        table = table + "\n\\hline\n"

    
    table = table + """
\\end{tabular}
\\end{table}
"""
    print(table)
