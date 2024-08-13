import json
import os
from collections import defaultdict

def all_same(items):
    return all(x == items[0] for x in items)

if __name__ == "__main__":
    syntax_validity = defaultdict(list)
    semantic_validity = defaultdict(list)
    
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
                if valid:
                    syntax_validity[object["id"]].append(1)
                else:
                    syntax_validity[object["id"]].append(0)
                    
                if "semantically_valid" in object:
                    if object["semantically_valid"]:
                        semantic_validity[object["id"]].append(1)
                    else:
                        semantic_validity[object["id"]].append(0)


    common_policy_ids = []
    for policy_id in syntax_validity:
        if len(syntax_validity[policy_id]) == 3:
            common_policy_ids.append(policy_id)

    syntax_consistent_results = 0
    semantic_consistent_results = 0

    for policy_id in common_policy_ids:
        if all_same(syntax_validity[policy_id]):
            syntax_consistent_results += 1
    
    for policy_id in common_policy_ids:
        if  all_same(semantic_validity[policy_id]):
            semantic_consistent_results += 1

    print(f"Total common policies across 3 runs: {len(common_policy_ids)}")
    print(f"Syntactically consistent count: {syntax_consistent_results}")
    print(f"Semantically consistent count: {semantic_consistent_results}")
