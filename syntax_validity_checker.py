import argparse
import json
import os
from policy_validator import is_valid_policy

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Semantic Validity Checker")
    parser.add_argument('-d', '--directory', type=str, help='Directory contianing json files.')
    parser.add_argument('-f', '--file', type=str, help='Json file.')
    parser.add_argument('-a', '--attribute', required=True, type=str, help='Object attribute that indicates policy to validate')

    args = parser.parse_args()

    files = []
    if args.directory:
        files = [f"{args.directory}/{file}" for file in os.listdir(args.directory)]
    elif args.file:
        files = [args.file]
    
    for file in files:
        with open(file, 'r') as in_file:
            try:
                objects = json.load(in_file)
            except:
                continue
            for object in objects:
                if args.attribute not in object:
                    continue
                policy = object[args.attribute]
                for r in range(5, -1, -1):
                    if f"syntactically_valid_{r}" in object:
                        syntactically_valid, reason = is_valid_policy(policy)
                        object[f"syntactically_valid_{r}"] = syntactically_valid
                        break
        with open(file, 'w') as ouput_file:
            json.dump(objects, ouput_file, indent=4)

