
## Installation

Install ANTLR4 tools using the following command:

```
pip install antlr4-tools==0.2.1
```

## Generate Parser, Listener, and Visitor

Run the following command to generate the parser, listener, and visitor classes.

```
antlr4 -visitor -Dlanguage=Python3 Policy.g4
```

`Note`: On each change in the grammar file (`Policy.g4`), you need to run the above command to regenerate the parser, listener, and visitor classes.

## Visualize parse tree

antlr4-parse Policy.g4 policy -gui ../policy.iconpal

## CustomPolicyVisitor

`CustomPolicyVisitor` is a custom visitor class that extends `PolicyVisitor` class. It overrides the `visitPolicy` method to apply custom logic on the parsed policy.
