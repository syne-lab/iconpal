
import os
import json
import matplotlib.pyplot as plt
import numpy as np
from utils import graph_colors

retry_counts_mapping = {
    "0": "Retry-0",
    "1": "Retry-1",
    "2": "Retry-2",
}
if __name__ == "__main__":    
    model = "GPT3_5_Turbo"
    data = [
        [],
        [],
        []
    ]
    retry_counts = ["0", "1", "2"]
    runs = [1, 2, 3]
    for r in runs:
        dirs = [
            f"evaluations/custom/output/{model}/p100/r{r}",
        ]
        files = []
        for dir in dirs:
            files = files + [f"{dir}/{file}" for file in os.listdir(dir)]

        syntactically_valid_count = {}
        semantically_valid_count = {}
        total = 0
        for x in retry_counts:
            syntactically_valid_count[x] = 0
            semantically_valid_count[x] = 0
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
                
                    if object.get("syntactically_valid_0", False):
                        syntactically_valid_count["0"] +=1
                        if object.get("semantically_valid", False):
                            semantically_valid_count["0"] += 1
                    if object.get("syntactically_valid_1", False):
                        syntactically_valid_count["1"] +=1
                        if object.get("semantically_valid", False):
                            semantically_valid_count["1"] += 1
                    if object.get("syntactically_valid_2", False):
                        syntactically_valid_count["2"] +=1
                        if object.get("semantically_valid", False):
                            semantically_valid_count["2"] += 1

        syntactically_valid_count["1"] += syntactically_valid_count["0"]
        syntactically_valid_count["2"] += syntactically_valid_count["1"]

        semantically_valid_count["1"] += semantically_valid_count["0"]
        semantically_valid_count["2"] += semantically_valid_count["1"]

        for retry_count in retry_counts:
            data[r-1].append(float(format(syntactically_valid_count[retry_count]*100/total, '.2f')))

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

    for i in range(len(retry_counts)):
        plt.bar(bar_positions + i * bar_width, data[:, i], width=bar_width-0.02, label=retry_counts_mapping[retry_counts[i]], color=graph_colors[i])
        for j, value in enumerate(data[:, i]):
            plt.text( j+i*bar_width, value + 0.5, str(int(value)), ha='center', va='bottom', rotation=0, fontsize=fontsize)


    # Customize the plot
    ax.set_xlabel('Runs', fontsize=fontsize)
    ax.set_ylabel('Syn. Validation \%', fontsize=fontsize)
    ax.set_xticks(bar_positions + (bar_width * (len(retry_counts) - 1)) / 2, runs, fontsize=fontsize)
    ax.set_yticks(np.arange(0, 101, 10), np.arange(0, 101, 10), fontsize=fontsize)
    ax.legend(bbox_to_anchor=(0.5,1.12), loc='upper center', ncol=3, fontsize=fontsize)
    fig.tight_layout()

    # Show the plot
    plt.savefig("img/rq2_ablation_refinement.pdf", format="pdf")
