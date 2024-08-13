import json
import os
from collections import defaultdict

def all_same(items):
    return all(x == items[0] for x in items)

if __name__ == "__main__":
    semantic_misclassification = defaultdict(int)
    policy_count_by_category = defaultdict(int)
    
    dirs = []
    for exp in ["custom" ]:
        for m in ["GPT4_1106_Preview"]:
            for r in range(1,4):
                dirs = dirs + [f"evaluations/{exp}/output/{m}/p100/r{r}"]
 
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
                print
                continue
            for object in objects:
                if "semantically_valid" in object:
                    if object["semantically_valid"] != object["valid"]:
                        semantic_misclassification[object["category"]] += 1
                    policy_count_by_category[object["category"]] += 1
    
    print("| Category | Policy Count | Misclassification Count | Misclassification Rate |")
    print("|----------|--------------|-------------------------|------------------------|")
    for category in semantic_misclassification:
        print(f"|{category} | {round(policy_count_by_category[category]/3)} | {round(semantic_misclassification[category]/3)} | {round(semantic_misclassification[category]/3)/round(policy_count_by_category[category]/3):.2f} |")