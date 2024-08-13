
import os
import json

model_name_mapping = {
    "GPT3_5_Turbo" : "GPT 3.5",
    "GPT4_1106_Preview": "GPT 4",
    "Llama_2_13b_Chat": "Llama2 13B",
    "Llama_2_70b_Chat_Quant": "Llama2 70B",
    "Mistral_7b_0_1_Instruct": "Mistral",
    "Mixtral_8x7b_0_1_Instruct": "Mixtral",
    "Yi_34b_Chat": "Yi 34B"
}
if __name__ == "__main__":
    data = [[]]
    data[-1].append("Model")
    data[-1].append("Total")
    data[-1].append(f"Syntactically Valid")
    data[-1].append("Semantically Valid")
    for m in ["GPT4_1106_Preview", "GPT3_5_Turbo", "Llama_2_70b_Chat_Quant", "Mixtral_8x7b_0_1_Instruct", "Mistral_7b_0_1_Instruct", "Yi_34b_Chat", "Llama_2_13b_Chat" ]:
        syntactically_valid_count = {
            "0": 0,
            "1": 0,
            "2": 0,
        }
        semantically_valid_count = 0
        total = 0
        validation_count = 0
        dirs = []
        for r in range(1,4):
            dirs = dirs + [f"evaluations/custom/output/{m}/p100/r{r}"]

        files = []
        for dir in dirs:
            try:
                files = files + [f"{dir}/{file}" for file in os.listdir(dir)]
            except:
                pass

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
                        if object.get("valid", False):
                            semantically_valid_count += 1
                    if object.get("syntactically_valid_0", False):
                        syntactically_valid_count["0"] +=1
                    if object.get("syntactically_valid_1", False):
                        syntactically_valid_count["1"] +=1
                    if object.get("syntactically_valid_2", False):
                        syntactically_valid_count["2"] +=1
                    

        syntactically_valid_count["1"] += syntactically_valid_count["0"]
        syntactically_valid_count["2"] += syntactically_valid_count["1"]

    
        data.append([])
        data[-1].append(model_name_mapping[m])
        data[-1].extend(get_table_data(total, syntactically_valid_count["2"], semantically_valid_count))


# \\begin{tabular}{ |p{0.1\linewidth}|p{0.1\linewidth}|p{0.1\linewidth}|p{0.07\linewidth}|p{0.05\linewidth}|p{0.07\linewidth}|p{0.05\linewidth}| }

    table = """
\\begin{table}
\\caption{Effectiveness of LLM on \\sysname's performance. Temperature: 0.5, Tutorial: Full, Example Selection: Manual, Example \#: 3, Refinement Limit: 2, Syn.: Syntax, Sem.: Semantic, r$_{syn}$: Syntax validity percentage w.r.t. total count, r$_{sem}$: Semantic validity percentage w.r.t. total count.}
\\label{tab:rq3-model-variation-simplified}

\\centering
\\begin{tabular}{ |c|c|c|c|c|c|c| }
\\hline
\\multirow{2}{*}{\\textbf{Model}} & \\multirow{2}{*}{\\textbf{Total}} & \\multicolumn{2}{|c|}{\\textbf{Syn. Validation}} & \\multicolumn{2}{|c|}{\\textbf{Sem. Validation}} \\\\
\cline{3-6}
 & & Count & r$_{syn}$ & Count & r$_{sem}$ \\\\
 \\hline
"""
    for i,d in enumerate(data[1:]):
        table = table + " & ".join(map(lambda x: str(x), d)) + "\\\\\n"
        table = table + "\n\\hline\n"
    
    table = table + """
\\hline
\\end{tabular}

\\end{table}
"""
    print(table)
