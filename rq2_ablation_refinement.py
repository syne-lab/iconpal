# Impact of reprompting

import argparse
import os
import json
from utils import get_table_data, supported_models

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate table for reprompt")

    parser.add_argument('-m', '--llm', type=str, default="GPT3_5_Turbo",
                        choices=supported_models,
                        help='LLM model')
    args = parser.parse_args()
    dirs = [
        f"evaluations/custom/output/{args.llm}/p100/r1",
        f"evaluations/custom/output/{args.llm}/p100/r2",
        f"evaluations/custom/output/{args.llm}/p100/r3"
    ]
    files = []
    for dir in dirs:
        files = files + [f"{dir}/{file}" for file in os.listdir(dir)]

    data = [[]]
    data[-1].append("Retry Count")
    data[-1].append(f"Syntactically Valid")
    data[-1].append("Semantically Valid")
    syntactically_valid_count = {
        "0": 0,
        "1": 0,
        "2": 0,
    }
    semantically_valid_count = {
        "0": 0,
        "1": 0,
        "2": 0,
    }
    validation_count = 0
    total = 0
    for file in files:
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
                total += 1
                
                if "valid" in object:
                    validation_count += 1
                if object.get("syntactically_valid_0", False):
                    syntactically_valid_count["0"] +=1
                    if "valid" in object:
                        if object.get("valid", False):
                            semantically_valid_count["0"] += 1
                if object.get("syntactically_valid_1", False):
                    syntactically_valid_count["1"] +=1
                    if "valid" in object:
                        if object.get("valid", False):
                            semantically_valid_count["1"] += 1
                if object.get("syntactically_valid_2", False):
                    syntactically_valid_count["2"] +=1
                    if "valid" in object:
                        if object.get("valid", False):
                            semantically_valid_count["2"] += 1
                

    syntactically_valid_count["1"] += syntactically_valid_count["0"]
    syntactically_valid_count["2"] += syntactically_valid_count["1"]

    semantically_valid_count["1"] += semantically_valid_count["0"]
    semantically_valid_count["2"] += semantically_valid_count["1"]

    for retry_count in ["0", "1", "2"]:
        data.append([])
        data[-1].append(retry_count)
        data[-1].extend(get_table_data(total, syntactically_valid_count[retry_count], semantically_valid_count[retry_count]))
         

    table = """
\\begin{table}

\\caption{Effectiveness of prompt refinement. Model: GPT 3.5, Temperature: 0.5, Tutorial: Simplified, Example Selection: Manual, Example \#: 1, R.: Refinement, Syn.: Syntax, Sem.: Semantic, r$_{syn}$: Syntax validity percentage w.r.t. total count, r$_{sem}$: Semantic validity percentage w.r.t. total count.}
\\label{tab:rq2-ablation-refinement}

\\centering
\\begin{tabular}{ |c|c|c|c|c|c| }
\\hline
\\multirow{2}{*}{\\textbf{R. Limit}} & \\multirow{2}{*}{\\textbf{Total}} & \\multicolumn{2}{|c|}{\\textbf{Syn. Validation}} & \\multicolumn{2}{|c|}{\\textbf{Sem. Validation}} \\\\
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
