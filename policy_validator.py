import sys
import argparse
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from policy_parser import PolicyLexer, PolicyParser, CustomPolicyVisitor


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error at line " + str(line) + ":" + str(column) + " " + msg)

def is_valid_snippet(policy_snippet):
    policy = InputStream(policy_snippet)
    lexer = PolicyLexer(policy)
    lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)
    stream = CommonTokenStream(lexer)
  
    parser = PolicyParser(stream)
    parser.addErrorListener(CustomErrorListener())
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
    try:
        tree = parser.statements()
    except Exception as e:
        return False

    visitor = CustomPolicyVisitor(relaxed=True)
    try:
        visitor.visit(tree)
    except Exception as e:
        return False
    return True


def is_valid_policy(policy_string):
    policy = InputStream(policy_string)
    lexer = PolicyLexer(policy)
    lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)
    stream = CommonTokenStream(lexer)
  
    parser = PolicyParser(stream)
    parser.addErrorListener(CustomErrorListener())
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
    try:
        tree = parser.policy()
    except Exception as e:
        return False, str(e)

    visitor = CustomPolicyVisitor()
    try:
        visitor.visit(tree)
    except Exception as e:
        return False, str(e)
    return True, ""


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Policy validator. Validates a policy for syntax errors")
    parser.add_argument('-p', '--policy', type=str, required=False,
                        help='Policy string to validate')
    parser.add_argument('-f', '--policy-file', type=str, help="Policy file to validate", required=False)
    args = parser.parse_args()
    policy = args.policy
    policy_file = args.policy_file
    if policy is None and policy_file is None:
        print("Error: Must provide either a policy string or a policy file")
        sys.exit(1)
    if policy_file:
        with open(policy_file, 'r') as f:
            policy_stream = f.read()
    else:
        policy_stream = policy
    is_valid = is_valid_policy(policy_stream)
    print("Valid: ", is_valid)
