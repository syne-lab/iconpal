
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
    data[-1].append("Retry Count")
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

        for retry_count in ["0", "1", "2"]:
            data.append([])
            average_total = int(total/3)
            average_syn_valid_count = int(syntactically_valid_count[retry_count]/3)
            syn_valid_percentage = format(average_syn_valid_count*100/average_total, '.2f')
            average_sem_valid_count = int(semantically_valid_count/3)
            sem_valid_percentage = format(average_sem_valid_count*100/average_total, '.2f')
            if retry_count=="0":
                data[-1].append("\\hline\n\\multirow{3}{*}{"+ model_name_mapping[m] +"}")
            else:
                data[-1].append("\\cline{2-2}\\cline{4-5}\n ")
            data[-1].append(retry_count)
            if retry_count == "0":
                data[-1].append("\\multirow{3}{*}{"+str(average_total)+"}")
            else:
                data[-1].append(" ")
            data[-1].append(average_syn_valid_count)
            data[-1].append(f"{syn_valid_percentage}\\%")
            if retry_count == "0":
                data[-1].append("\\multirow{3}{*}{"+str(average_sem_valid_count)+"}")
            else:
               data[-1].append(" ")
            if retry_count == "0":
                if not average_total:
                    sem_valid_percentage = 0
                else:
                    sem_valid_percentage = "\\multirow{3}{*}{"+sem_valid_percentage+"\\%}"
                data[-1].append(sem_valid_percentage)
            else:
                data[-1].append(" ")

# \\begin{tabular}{ |p{0.1\linewidth}|p{0.1\linewidth}|p{0.1\linewidth}|p{0.07\linewidth}|p{0.05\linewidth}|p{0.07\linewidth}|p{0.05\linewidth}| }

    table = """
\\begin{table}
\\caption{Effectiveness of LLM on \\sysname's performance.. Temperature: 0.5, Tutorial: Full, Example Selection: Manual, Example \#: 3, R.: Refinement, Syn.: Syntax, Sem.: Semantic, r$_{syn}$: Syntax validity percentage w.r.t. total count, r$_{sem}$: Semantic validity percentage w.r.t. total count.}
\\label{tab:rq3-model-variation}

\\centering
\\begin{tabular}{ |c|c|c|c|c|c|c| }
\\hline
\\multirow{2}{*}{\\textbf{Model}} & \\multirow{2}{*}{\\textbf{R.L.}} & \\multirow{2}{*}{\\textbf{Total}} & \\multicolumn{2}{|c|}{\\textbf{Syn. Validation}} & \\multicolumn{2}{|c|}{\\textbf{Sem. Validation}} \\\\
\cline{4-7}
 & & & Count & r$_{syn}$ & Count & r$_{sem}$ \\\\
"""
    for i,d in enumerate(data[1:]):
        table = table + " & ".join(map(lambda x: str(x), d)) + "\\\\\n"

    
    table = table + """
\\hline
\\end{tabular}

\\end{table}
"""
    print(table)
