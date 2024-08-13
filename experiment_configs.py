
ablation_study_configs = [
    {"examples": examples, "tutorial": tutorial, "grammar": grammar, "temperature": tmp}
    for tutorial in ["policy_tutorial.md", None]
        for grammar in ["policy_grammar.ebnf", None]
            for examples in ["human-categorized", 0]
                for tmp in [0.5]
]


tutorial_variation_configs = [
    {"examples": examples, "tutorial": tutorial, "grammar": grammar, "temperature": tmp}
    for tutorial in ["policy_tutorial_summarized.md", "policy_tutorial_simplified.md"]
        for grammar in [None]
            for examples in ["human-categorized"]
                for tmp in [0.5]
]

example_count_variation_configs = [
    {"examples": examples, "tutorial": tutorial, "grammar": grammar, "temperature": tmp}
    for tutorial in ["policy_tutorial_simplified.md"]
        for grammar in [None]
            for examples in [0, 2, 3, 4]
                for tmp in [0.5]
]


example_type_variation_configs = [
    {"examples": examples, "tutorial": tutorial, "grammar": grammar, "temperature": tmp}
    for tutorial in ["policy_tutorial_simplified.md"]
        for grammar in [None]
            for examples in ["random", "llm-categorized"]
                for tmp in [0.5]
]

temperature_configs = [
    {"examples": examples, "tutorial": tutorial, "grammar": grammar, "temperature": tmp}
    for tutorial in ["policy_tutorial_simplified.md"]
        for grammar in [None]
            for examples in ["human-categorized"]
                for tmp in [0.0, 0.5, 1.0, 1.5]
]
custom_configs = [
    {"examples": examples, "tutorial": tutorial, "grammar": grammar, "temperature": tmp}
    for tutorial in ["policy_tutorial.md"]
        for grammar in [None]
            for examples in [3]
                for tmp in [0.5]
]

configs = {
    "ablation": ablation_study_configs,
    "tutorial": tutorial_variation_configs,
    "example-count": example_count_variation_configs,
    "example-type": example_type_variation_configs,
    "temperature": temperature_configs,
    "custom": custom_configs
}
