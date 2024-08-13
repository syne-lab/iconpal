import os
import argparse
from utils import supported_models, get_file_content, get_number_of_tokens


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Count experiment token")
    parser.add_argument('-m', '--llm', type=str, default="Llama_2_7b",
                        choices=supported_models,
                        help='LLM model')
    parser.add_argument('-f', '--file', type=str, help="Specify the file for which you intend to calculate the token count.")
    parser.add_argument('-d', '--directory', type=str, help='Specify the directory for which you intend to calculate the token count' )
    args = parser.parse_args()

    files = []
    if args.directory:
        files = [f"{args.directory}/{file}" for file in os.listdir(args.directory)]
    elif args.file:
        files = [args.file]
    print(files)
    token_count = 0
    for file in files:
        token_count += get_number_of_tokens(get_file_content(file))
    print(f"Number of tokens: {token_count}")
