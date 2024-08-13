
import os
import json
from utils import extract_info_from_filename
import matplotlib.pyplot as plt
import numpy as np
graph_colors = [(218, 208, 184), (196, 187, 167), (173, 166, 151), (152, 146, 135), (130, 126, 122), (110, 108, 110), (90, 90, 97), (72, 73, 84)]
for i in range(len(graph_colors)):
    graph_colors[i] = (graph_colors[i][0]/255.0, graph_colors[i][1]/255.0, graph_colors[i][2]/255.0)

if __name__ == "__main__":    
    model = "GPT3_5_Turbo"
    data = [
        [],
        [],
        []
    ]
    components = ["ETG", "ET-", "E-G", "E--", "-TG", "-T-",  "--G", "---"]
    runs = [1, 2, 3]
    for r in runs:
        dirs = [
            f"evaluations/ablation/output/{model}/p100/r{r}",
        ]
        files = []
        for dir in dirs:
            files = files + [f"{dir}/{file}" for file in os.listdir(dir)]

        syntactically_valid_count = {}
        semantically_valid_count = {}
        total = {}
        for t in components:
            syntactically_valid_count[t] = 0
            semantically_valid_count[t] = 0
            total[t] = 0
        for file in files:
            example, tutorial, grammar = extract_info_from_filename(file.split('/')[-1])
            example = example.split("example-")[-1]
            if example == "0":
                example = "-"
            else:
                example = "E"
            
            if tutorial == "None":
                tutorial = "-"
            else:
                tutorial = "T"
            
            if grammar == "None":
                grammar = "-"
            else:
                grammar = "G"

            component = f"{example}{tutorial}{grammar}"
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
                    if object.get("semantically_valid", False):
                        semantically_valid_count[component] += 1
                    if object.get(f"syntactically_valid_0", False):
                        syntactically_valid_count[component] += 1
                    

        for component in components:
            data[r-1].append(float(format(syntactically_valid_count[component]*100/total[component], '.2f')))

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
    bar_width = 0.11
    bar_positions = np.arange(len(runs))

    for i in range(len(components)):
        ax.bar(bar_positions + i * bar_width, data[:, i], width=bar_width-0.01, label=components[i], color=graph_colors[i])
        for j, value in enumerate(data[:, i]):
            ax.text( j+i*bar_width, value + 0.5, str(int(value)), ha='center', va='bottom', rotation=0, fontsize=fontsize)


    # Customize the plot
    ax.set_xlabel('Runs', fontsize=fontsize)
    ax.set_ylabel('Syn. Validation \%', fontsize=fontsize)
    ax.set_xticks(bar_positions + (bar_width * (len(components) - 1)) / 2, runs, fontsize=fontsize)

    ax.set_yticks(np.arange(0, 101, 10), np.arange(0, 101, 10), fontsize=fontsize)
 
    ax.legend(bbox_to_anchor=(0.5,1.19), loc='upper center', ncol=4, fontsize=fontsize)
    fig.tight_layout()

    # Show the plot
    # plt.show()
    plt.savefig("img/rq2_ablation_component.pdf", format="pdf")

 