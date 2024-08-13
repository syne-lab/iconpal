
import argparse
import os
import json
from utils import supported_models, extract_info_from_filename, get_table_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate policy from text")

    parser.add_argument('-m', '--llm', type=str, default="GPT3_5_Turbo",
                        choices=supported_models,
                        help='LLM model')
    args = parser.parse_args()
    dirs = [
        f"evaluations/example-count/output/{args.llm}/p100/r1",
        f"evaluations/example-count/output/{args.llm}/p100/r2",
        f"evaluations/example-count/output/{args.llm}/p100/r3"
    ]
    files = [
        f"evaluations/tutorial/output/{args.llm}/p100/r1/exp-example-human-categorized-tutorial-policy_tutorial_simplified.md-grammar-None.json",
        f"evaluations/tutorial/output/{args.llm}/p100/r2/exp-example-human-categorized-tutorial-policy_tutorial_simplified.md-grammar-None.json",
        f"evaluations/tutorial/output/{args.llm}/p100/r3/exp-example-human-categorized-tutorial-policy_tutorial_simplified.md-grammar-None.json"
    ]
    for dir in dirs:
        files = files + [f"{dir}/{file}" for file in os.listdir(dir)]

    data = [[]]
    data[-1].append("Example Count")
    data[-1].append("Total")
    data[-1].append(f"Syntactically Valid")
    data[-1].append("Semantically Valid")
    syntactically_valid_count = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0
    }
    semantically_valid_count = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0
    }
    total = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0
    }
    validation_count = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0
    }
    for file in files:
        example_count, _, _ = extract_info_from_filename(file.split('/')[-1])
        example_count = example_count.split("example-")[-1]
        if example_count == "human-categorized":
            example_count = "1"
    
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
                total[example_count] +=1
                if "valid" in object:
                    validation_count[example_count] += 1
                    if object.get("valid", False):
                        semantically_valid_count[example_count] += 1
                if object.get(f"syntactically_valid_0", False):
                    syntactically_valid_count[example_count] += 1
                

    for example_count in ["0", "1", "2", "3"]:
        data.append([])
        data[-1].append(example_count)
        data[-1].extend(get_table_data(total[example_count], syntactically_valid_count[example_count], semantically_valid_count[example_count]))
        

    table = """
\\begin{table}
\\caption{Impact of number of examples in learning prompt. Model: GPT 3.5, Temperature: 0.5, Tutorial: Simplified, Example Selection: Manual, E.: Example, Syn.:Syntax, Sem.:Semantic, r$_{syn}$: Syntax validity percentage w.r.t. total count, r$_{sem}$: Semantic validity percentage w.r.t. total count.}
\\label{tab:rq2-ablation-example-count}

\\centering
\\begin{tabular}{ |c|c|c|c|c|c| }
\\hline
\\multirow{2}{*}{\\textbf{E. Count}} & \\multirow{2}{*}{\\textbf{Total}} & \\multicolumn{2}{|c|}{\\textbf{Syn. Validation}} & \\multicolumn{2}{|c|}{\\textbf{Sem. Validation}} \\\\
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
