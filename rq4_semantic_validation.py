# Efficacy of LLM to perform semantic validation

import os
import json
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser("AutoSemVal Metrics")
    parser.add_argument('-d', '--dir', type=str, help='Directory of evaluation results')

    args = parser.parse_args()
    
    dirs = []
    if args.dir:
        for r in range(1,4):
            dirs.append(f"{args.dir}/r{r}")    
    else:
        for exp in ["ablation", "temperature", "tutorial", "example-count", "example-type", "custom" ]:
            
            for m in ["GPT4_1106_Preview", "GPT3_5_Turbo", "Llama_2_70b_Chat_Quant", "Mixtral_8x7b_0_1_Instruct", "Mistral_7b_0_1_Instruct", "Yi_34b_Chat", "Llama_2_13b_Chat"]:
                for r in range(1,4):
                    dirs = dirs + [f"evaluations/{exp}/output/{m}/p100/r{r}"]
    
    files = []
    for dir in dirs:
        try:
            files = files + [f"{dir}/{file}" for file in os.listdir(dir)]
        except:
            pass
    
    # print(files)
    # files = ["evaluations/temperature/output/GPT3_5_Turbo/p100/r2/exp-example-llm-categorized-tutorial-policy_tutorial_simplified.md-grammar-None-tmp-0.5.json"]
    total = 0
    true_positive = 0
    false_negative = 0
    false_positive = 0
    true_negative = 0
    positive = 0
    negative = 0
    for file in files:
        with open(file, 'r') as in_file:
            try:
                objects = json.load(in_file)
            except:
                continue
            
            total_count = len(objects)
            if total_count < 1:
                continue

            for object in objects:
                if "valid" in object and "semantically_valid" in object:
                    total+=1
                    if object["valid"]: # Actually true
                        positive +=1
                        if object["semantically_valid"]: # Predicted true
                            true_positive +=1
                        else: # Predicted false
                            false_negative +=1
                    else: # Actually false
                        negative +=1
                        if object["semantically_valid"]: # Predicted true
                            false_positive +=1
                        else: # Predicted false
                             true_negative +=1 


    precision = format(true_positive/(true_positive+false_positive), '0.2f') # positive predictive value
    recall = format(true_positive/(true_positive+false_negative), '0.2f')   # true positive rate or sensitivity
    true_negative_rate = format(true_negative/(true_negative+false_positive), '0.2f') # specificity
    accuracy =  format((true_positive+true_negative)/(positive+negative), '0.2f') 
    f1_score = format((2*true_positive)/(2*true_positive + false_positive + false_negative), '0.2f')

    print("True Positive: ", true_positive)
    print("True Negative: ", true_negative)
    print("False Positive: ", false_positive)
    print("False Negative: ", false_negative)
    print("Total: ", total)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("True Negative Rate: ", true_negative_rate)
    print("Accuracy: ", accuracy)
    print("F1 Score: ", f1_score)
