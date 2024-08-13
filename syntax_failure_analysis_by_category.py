import json
import os
from collections import defaultdict

def all_same(items):
    return all(x == items[0] for x in items)

if __name__ == "__main__":
    syntax_failure = defaultdict(int)
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
                valid = False
                for i in range(3):
                    if f"syntactically_valid_{i}" in object:
                        valid = object[f"syntactically_valid_{i}"]
                if not valid:
                    syntax_failure[object["category"]] += 1
                policy_count_by_category[object["category"]] += 1
    
    print("| Category | Policy Count | Failed translation count | Failure Rate |")
    print("|----------|--------------|--------------------------|--------------|")
    for category in syntax_failure:
        print(f"|{category} | {policy_count_by_category[category]} | {syntax_failure[category]} | {syntax_failure[category]/policy_count_by_category[category]:.2f} |")
        
        