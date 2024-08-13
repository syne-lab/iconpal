import sys
from utils import Example
from policy_validator import is_valid_policy

if __name__ == "__main__":
    dataset_examples = Example.load_data_from_json("dataset/processed_data/manually_categorized_dataset.json")
    total_count = len(dataset_examples)
    valid_count = len([example for example in dataset_examples if example.syntax_valid])
    invalid_count = total_count - valid_count
    print("Total: ", total_count)
    print("Valid: ", valid_count)
    print("Invalid: ", invalid_count)

    invalid_examples = [example for example in dataset_examples if not example.syntax_valid]
    if len(invalid_examples) == 0:
        print("All policies in dataset are syntactically valid")
        sys.exit(0)
    
    choice = input("Do you want to see the invalid examples? (y/n): ")
    show_example = choice in ["y", "Y", "yes", "Yes"]
    i = 0
    
    while show_example and i < len(invalid_examples):
        example = invalid_examples[i]
        if not example.syntax_valid:
            print("\nText:")
            print(example.text)
            print("\nPolicy:")
            print(example.policy)
            is_valid, reason = is_valid_policy(example.policy)
            print("\nReason: ", reason)
            choice = input("\nNext/Exit (n/e)?: ")
            if choice in ["n", "N", "next", "Next"]:
                i += 1
                continue
            else:
                break

