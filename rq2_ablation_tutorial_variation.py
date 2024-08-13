
import argparse
import os
import re
import json
from utils import get_table_data, supported_models, extract_info_from_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate policy from text")

    parser.add_argument('-m', '--llm', type=str, default="GPT3_5_Turbo",
                        choices=supported_models,
                        help='LLM model')
    args = parser.parse_args()
    dirs = [
        f"evaluations/tutorial/output/{args.llm}/p100/r1",
        f"evaluations/tutorial/output/{args.llm}/p100/r2",
        f"evaluations/tutorial/output/{args.llm}/p100/r3"
    ]
    files = [
        f"evaluations/ablation/output/{args.llm}/p100/r1/exp-example-human-categorized-tutorial-policy_tutorial.md-grammar-None.json",
        f"evaluations/ablation/output/{args.llm}/p100/r2/exp-example-human-categorized-tutorial-policy_tutorial.md-grammar-None.json",
        f"evaluations/ablation/output/{args.llm}/p100/r3/exp-example-human-categorized-tutorial-policy_tutorial.md-grammar-None.json"
    ]
    for dir in dirs:
        files = files + [f"{dir}/{file}" for file in os.listdir(dir)]

    data = [[]]
    data[-1].append("Tutorial")
    data[-1].append("Total")
    data[-1].append(f"Syntactically Valid")
    data[-1].append("Semantically Valid")
    syntactically_valid_count = {
        "full": 0,
        "summarized": 0,
        "simplified": 0
    }
    semantically_valid_count = {
        "full": 0,
        "summarized": 0,
        "simplified": 0
    }
    total = {
        "full": 0,
        "summarized": 0,
        "simplified": 0
    }
    validation_count = {
        "full": 0,
        "summarized": 0,
        "simplified": 0
    }
    for file in files:
        _, tutorial , _ = extract_info_from_filename(file.split('/')[-1])
        if tutorial == "None":
            continue
        match = re.search(r'_tutorial_([a-zA-Z]+)\.md', tutorial)
        if match:
            tutorial = match.group(1)
        else:
            tutorial = "full"
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
                total[tutorial] +=1
                if "valid" in object:
                    validation_count[tutorial] += 1
                    if object.get("valid", False):
                        semantically_valid_count[tutorial] += 1
                if object.get(f"syntactically_valid_0", False):
                    syntactically_valid_count[tutorial] += 1
                

    for tutorial in ["full", "simplified", "summarized"]:
        data.append([])
        data[-1].append(tutorial.capitalize())

        data[-1].extend(get_table_data(total[tutorial], syntactically_valid_count[tutorial], semantically_valid_count[tutorial])) 
        

    table = """
\\begin{table}
\\caption{Impact of tutorial variation in learning prompt. Model: GPT 3.5, Temperature: 0.5, Example Selection: Manual, Example \#: 1, . Syn.:Syntax, Sem.:Semantic, r$_{syn}$: Syntax validity percentage w.r.t. total count, r$_{sem}$: Semantic validity percentage w.r.t. total count.}
\\label{tab:rq2-ablation-tutorial-variation}

\\centering

\\begin{tabular}{ |l|c|c|c|c|c| }
\\hline
\\multirow{2}{*}{\\textbf{Tutorial}} & \\multirow{2}{*}{\\textbf{Total}} & \\multicolumn{2}{|c|}{\\textbf{Syn. Validation}} & \\multicolumn{2}{|c|}{\\textbf{Sem. Validation}} \\\\
\cline{3-6}
 & & Count & r$_{syn}$ & Count & r$_{sem}$ \\\\
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
