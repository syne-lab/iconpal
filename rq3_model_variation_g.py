
import os
import json
import matplotlib.pyplot as plt
import numpy as np
from rq3_model_variation import model_name_mapping
graph_colors = [(218, 208, 184), (196, 187, 167), (173, 166, 151), (152, 146, 135), (130, 126, 122), (110, 108, 110), (90, 90, 97), (72, 73, 84)]
for i in range(len(graph_colors)):
    graph_colors[i] = (graph_colors[i][0]/255.0, graph_colors[i][1]/255.0, graph_colors[i][2]/255.0)

if __name__ == "__main__":    
    data = [
        [],
        [],
        []
    ]
    models = ["GPT3_5_Turbo", "GPT4_1106_Preview", "Llama_2_70b_Chat_Quant", "Mistral_7b_0_1_Instruct", "Mixtral_8x7b_0_1_Instruct", "Llama_2_13b_Chat", "Yi_34b_Chat"]
    runs = [1, 2, 3]
    for r in runs:
        dirs = []
        for model in models:
            dirs.append(f"evaluations/custom/output/{model}/p100/r{r}")
     
        files = []
        for dir in dirs:
            try:
                files = files + [f"{dir}/{file}" for file in os.listdir(dir)]
            except:
                pass

        syntactically_valid_count = {}
        semantically_valid_count = {}
        total = {}
        for t in models:
            syntactically_valid_count[t] = 0
            semantically_valid_count[t] = 0
            total[t] = 0
        for file in files:
            folders = file.split('/')
            output_index = folders.index("output")
            model = folders[output_index+1]

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
                    total[model] +=1
                    if object.get("semantically_valid", False):
                        semantically_valid_count[model] += 1
                    syntactically_valid = False
                    for x in range(5):
                        if f"syntactically_valid_{x}" not in object:
                            break
                        else:
                            syntactically_valid = object[f"syntactically_valid_{x}"]
                    
                    if syntactically_valid:
                        syntactically_valid_count[model] += 1
                    

        for model in models:
            if not total[model]:
                syn_valid_percentage = 0
            else:
                syn_valid_percentage = float(format(syntactically_valid_count[model]*100/total[model], '.2f'))
            data[r-1].append(syn_valid_percentage)

    # Plotting
    # plt.figure(figsize=(60,50))
    # plt.style.use('grayscale')
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

    # colors = list(mcolors.BASE_COLORS) #these colors can be called with a single character

    # colors =  ['black', 'dimgray', 'gray', 'darkgray', 'silver', 'lightgray', 'whitesmoke']
    # colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta']
    # colors = ['#00429d', '#4771b2', '#73a2c6', '#a5d5d8', '#ffbcaf', '#f4777f', '#cf3759']
    for i in range(len(models)):
        plt.bar(bar_positions + i * bar_width , data[:, i], width=bar_width-0.01, label=model_name_mapping[models[i]], color=graph_colors[i])
        for j, value in enumerate(data[:, i]):
            plt.text( j+i*bar_width, value + 0.5, str(int(value)), ha='center', va='bottom', rotation=0, fontsize=fontsize)


    # Customize the plot
    ax.set_xlabel('Runs', fontsize=fontsize)
    ax.set_ylabel('Syn. Validation \%', fontsize=fontsize)
    ax.set_xticks(bar_positions + (bar_width * (len(models) - 1)) / 2, runs, fontsize=fontsize)
    ax.set_yticks(np.arange(0, 101, 10), np.arange(0, 101, 10), fontsize=fontsize)
    ax.legend(bbox_to_anchor=(0.5,1.2), loc='upper center', ncol=4, fontsize=fontsize-1)

    fig.tight_layout()

    plt.savefig("img/rq3_model_variation.pdf", format="pdf")

 