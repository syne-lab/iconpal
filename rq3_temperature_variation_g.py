
import os
import re
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
    temperatures = ["0.0", "0.5", "1.0", "1.5"]
    runs = [1, 2, 3]
    for r in runs:
        dirs = [
            f"evaluations/temperature/output/{model}/p100/r{r}",
        ]
        files = []
        for dir in dirs:
            try:
                files = files + [f"{dir}/{file}" for file in os.listdir(dir)]
            except:
                pass

        syntactically_valid_count = {}
        semantically_valid_count = {}
        total = {}
        for t in temperatures:
            syntactically_valid_count[t] = 0
            semantically_valid_count[t] = 0
            total[t] = 0
        for file in files:
            _, _, temperature = extract_info_from_filename(file.split('/')[-1])

            temperature = re.search(r'\d+\.\d+', temperature)

            if temperature:
                try:
                    temperature = temperature.group()
                except:
                    temperature = "0.5"
            else:
                temperature = "0.5"
            if temperature not in temperatures:
                continue
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
                    total[temperature] +=1
                    if object.get("semantically_valid", False):
                        semantically_valid_count[temperature] += 1
                    if object.get(f"syntactically_valid_0", False):
                        syntactically_valid_count[temperature] += 1
                    

        for temperature in temperatures:
            if not total[temperature]:
                syn_valid_percentage = 0
            else:
                syn_valid_percentage = float(format(syntactically_valid_count[temperature]*100/total[temperature], '.2f'))
            data[r-1].append(syn_valid_percentage)

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
    bar_width = 0.14
    bar_positions = np.arange(len(runs))

    for i in range(len(temperatures)):
        plt.bar(bar_positions + i * bar_width, data[:, i], width=bar_width-0.02, label=f"T: {temperatures[i]}", color=graph_colors[i])
        for j, value in enumerate(data[:, i]):
            plt.text( j+i*bar_width, value + 0.5, str(int(value)), ha='center', va='bottom', rotation=0, fontsize=fontsize)


    # Customize the plot
    ax.set_xlabel('Runs', fontsize=fontsize)
    ax.set_ylabel('Syn. Validation \%', fontsize=fontsize)
    ax.set_xticks(bar_positions + (bar_width * (len(temperature) - 1)) / 2, runs, fontsize=fontsize)
    ax.set_yticks(np.arange(0, 91, 10), np.arange(0, 91, 10), fontsize=fontsize)
    ax.legend(bbox_to_anchor=(0.5,1.12), loc='upper center', ncol=4, fontsize=fontsize)
    fig.tight_layout()

    # Show the plot
    plt.savefig("img/rq3_temperature_variation.pdf", format="pdf")

 