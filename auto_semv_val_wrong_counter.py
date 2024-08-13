import argparse
import json
import os
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Semantic Validity Checker")
    parser.add_argument('-f', '--file', type=str, help='File contianing list of json objects.')
    parser.add_argument('-d', '--dir', type=str, help='Dir contianing list of json objects.')

    args = parser.parse_args()

    files = []
    if args.file:
        files = [args.file]

    if args.dir:
        for r in range(1,4):
            files = files + [f"{args.dir}/r{r}/{file}" for file in os.listdir(f"{args.dir}/r{r}")]

    wrong = 0
    
    for file in files:
        with open(file, 'r') as in_file:
            try:
                objects = json.load(in_file)
            except:
                continue
            for object in objects:
                if not "semantically_valid" in object:
                    continue
                if object["valid"] != object["semantically_valid"]:
                    wrong += 1
    print(f"Wrong: {wrong}")
