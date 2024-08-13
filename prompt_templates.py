system_learn_from_context = "\nYou are a plain text to formal policy translator. I will teach you how to translate a plain text to formal policy with a tutorial and some examples.\n"

user_query_text_to_policy = "\nTranslate the following natural text to formal policy. Only provide the translated formal policy itself without any explanations or extra words.\n"

user_query_policy_to_text = "\nTranslate the following formal policy to plain text. Only provide the translation itself in plain text without any explanations or extra words.\n"

user_query_statement_equivalency = "\nAre the following two policies equivalent? Consider only action and condition. Answer Yes or No\n\n"

simplify_tutorial = "Simplify following tutorial on Policy language. Try to minimize tokens. Ensure the simplified version retains sufficient information for a novice learner of Maverick Policy."

summarize_tutorial = "Summarize following tutorial on Policy language. Try to minimize tokens. Ensure the summarized version retains sufficient information for a novice learner of Maverick Policy."

use_category_definitions = "Your are a statement category identifier. Use the following category definitions to identify category of a statement. Use exact category from the definitions. Do not invent any new category. :\n"

categorize_dataset = "What is the category of following statement? Only state the category name.\n"
