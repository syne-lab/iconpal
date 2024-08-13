import argparse
from utils import (
    Example,
    report_usage, DataCategorizer
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Categorize policy dataset")
    parser.add_argument('-m', '--llm', type=str, default="GPT3_5_Turbo",
                        choices=["GPT3_5_Turbo", "GPT3_5_Turbo_16k", "GPT4_1106_Preview", "GPT4", "GPT4_32k"],
                        help='LLM model')
    parser.add_argument('--dry-run', action="store_true", help="Dry run mode")
    
    args = parser.parse_args()

    data_categorizer = DataCategorizer(args.llm, dry_run=args.dry_run, debug=False)
    all_data = Example.load_data_from_json("dataset/processed_data/manually_categorized_dataset.json")
    false_count = 0
    total= 0
    for data in all_data:
        total+=1
        category = data_categorizer.get_category(data.text)
        if category != data.category:
            false_count+=1
        data.category = category
    
    print(f"False: {false_count}, Total: {total}, %: {((total-false_count)*100/total)}")
    Example.dump_json(all_data, "dataset/processed_data/llm_categorized_dataset.json")

    report_usage(data_categorizer.input_tokens, data_categorizer.output_tokens)