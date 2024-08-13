
import os
import json
from utils import extract_info_from_filename
import matplotlib.pyplot as plt
import numpy as np
from utils import graph_colors

if __name__ == "__main__":    
    model = "GPT3_5_Turbo"
    data = [
        [],
        [],
        []
    ]
    example_types = ["random", "human-categorized", "llm-categorized"]
    runs = [1, 2, 3]
    for r in runs:
        dirs = [
            f"evaluations/example-type/output/{model}/p100/r{r}",
        ]
        files = [
            f"evaluations/tutorial/output/{model}/p100/r{r}/exp-example-human-categorized-tutorial-policy_tutorial_simplified.md-grammar-None.json",
        ]
        for dir in dirs:
            files = files + [f"{dir}/{file}" for file in os.listdir(dir)]

        syntactically_valid_count = {
            "random": 0,
            "human-categorized": 0,
            "llm-categorized": 0
        }
        semantically_valid_count = {
            "random": 0,
            "human-categorized": 0,
            "llm-categorized": 0
        }
        total = {
            "random": 0,
            "human-categorized": 0,
            "llm-categorized": 0
        }
        for file in files:
            example_type, _ , _ = extract_info_from_filename(file.split('/')[-1])
            example_type = example_type.split("example-")[-1]

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
                    total[example_type] +=1
                    if object.get("semantically_valid", False):
                        semantically_valid_count[example_type] += 1
                    if object.get(f"syntactically_valid_0", False):
                        syntactically_valid_count[example_type] += 1
                    

        for example_type in example_types:
            data[r-1].append(float(format(syntactically_valid_count[example_type]*100/total[example_type], '.2f')))

    # Plotting
    plt.rcParams.update({
        'font.sans-serif': 'Helvetica',
        'font.family': 'sans-serif',
        'text.usetex': True
    })

    fig =plt.figure()
    ax = plt.gca()

    fontsize=12
    data = np.array(data)
    bar_width = 0.17
    bar_positions = np.arange(len(runs))

    for i in range(len(example_types)):
        label = example_types[i].split("-")[0]
        if label == "llm":
            label = "LLM"
        elif label == "human":
            label = "Manual"
        else:
            label = label.capitalize()
        plt.bar(bar_positions + i * bar_width, data[:, i], width=bar_width-0.02, label=label, color=graph_colors[i])
        for j, value in enumerate(data[:, i]):
            plt.text( j+i*bar_width, value + 0.5, str(int(value)), ha='center', va='bottom', rotation=0, fontsize=fontsize)


    # Customize the plot
    ax.set_xlabel('Runs', fontsize=fontsize)
    ax.set_ylabel('Syn. Validation \%', fontsize=fontsize)
    ax.set_xticks(bar_positions + (bar_width * (len(example_types) - 1)) / 2, runs, fontsize=fontsize)
    ax.set_yticks(np.arange(0, 91, 10), np.arange(0, 91, 10), fontsize=fontsize)
   
    ax.legend(bbox_to_anchor=(0.5,1.12), loc='upper center', ncol=3, fontsize=fontsize)
    fig.tight_layout()
    # Show the plot
    plt.savefig("img/rq2_ablation_example_selection.pdf", format="pdf")
 