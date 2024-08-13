import json
import os
from collections import defaultdict

if __name__ == "__main__":
    sem_invalid_by_category = defaultdict(int)
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
                if "valid" in object:
                    if not object["valid"]:
                        sem_invalid_by_category[object["category"]] += 1
                    policy_count_by_category[object["category"]] += 1
    
    print("| Category | Policy Count | Misclassification Count | Misclassification Rate |")
    print("|----------|--------------|-------------------------|------------------------|")
    for category in sem_invalid_by_category:
        print(f"|{category} | {round(policy_count_by_category[category]/3)} | {round(sem_invalid_by_category[category]/3)} | {round(sem_invalid_by_category[category]/3)/round(policy_count_by_category[category]/3):.2f} |")