# Generated from Policy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PolicyParser import PolicyParser
else:
    from PolicyParser import PolicyParser

# This class defines a complete listener for a parse tree produced by PolicyParser.
class PolicyListener(ParseTreeListener):

    # Enter a parse tree produced by PolicyParser#policy.
    def enterPolicy(self, ctx:PolicyParser.PolicyContext):
        pass

    # Exit a parse tree produced by PolicyParser#policy.
    def exitPolicy(self, ctx:PolicyParser.PolicyContext):
        pass


    # Enter a parse tree produced by PolicyParser#statements.
    def enterStatements(self, ctx:PolicyParser.StatementsContext):
        pass

    # Exit a parse tree produced by PolicyParser#statements.
    def exitStatements(self, ctx:PolicyParser.StatementsContext):
        pass


    # Enter a parse tree produced by PolicyParser#invariant.
    def enterInvariant(self, ctx:PolicyParser.InvariantContext):
        pass

    # Exit a parse tree produced by PolicyParser#invariant.
    def exitInvariant(self, ctx:PolicyParser.InvariantContext):
        pass


    # Enter a parse tree produced by PolicyParser#if_condition.
    def enterIf_condition(self, ctx:PolicyParser.If_conditionContext):
        pass

    # Exit a parse tree produced by PolicyParser#if_condition.
    def exitIf_condition(self, ctx:PolicyParser.If_conditionContext):
        pass


    # Enter a parse tree produced by PolicyParser#predicate.
    def enterPredicate(self, ctx:PolicyParser.PredicateContext):
        pass

    # Exit a parse tree produced by PolicyParser#predicate.
    def exitPredicate(self, ctx:PolicyParser.PredicateContext):
        pass


    # Enter a parse tree produced by PolicyParser#predicate_factor.
    def enterPredicate_factor(self, ctx:PolicyParser.Predicate_factorContext):
        pass

    # Exit a parse tree produced by PolicyParser#predicate_factor.
    def exitPredicate_factor(self, ctx:PolicyParser.Predicate_factorContext):
        pass


    # Enter a parse tree produced by PolicyParser#then_condition.
    def enterThen_condition(self, ctx:PolicyParser.Then_conditionContext):
        pass

    # Exit a parse tree produced by PolicyParser#then_condition.
    def exitThen_condition(self, ctx:PolicyParser.Then_conditionContext):
        pass


    # Enter a parse tree produced by PolicyParser#term.
    def enterTerm(self, ctx:PolicyParser.TermContext):
        pass

    # Exit a parse tree produced by PolicyParser#term.
    def exitTerm(self, ctx:PolicyParser.TermContext):
        pass


    # Enter a parse tree produced by PolicyParser#term_factor.
    def enterTerm_factor(self, ctx:PolicyParser.Term_factorContext):
        pass

    # Exit a parse tree produced by PolicyParser#term_factor.
    def exitTerm_factor(self, ctx:PolicyParser.Term_factorContext):
        pass


    # Enter a parse tree produced by PolicyParser#function_call.
    def enterFunction_call(self, ctx:PolicyParser.Function_callContext):
        pass

    # Exit a parse tree produced by PolicyParser#function_call.
    def exitFunction_call(self, ctx:PolicyParser.Function_callContext):
        pass


    # Enter a parse tree produced by PolicyParser#terms.
    def enterTerms(self, ctx:PolicyParser.TermsContext):
        pass

    # Exit a parse tree produced by PolicyParser#terms.
    def exitTerms(self, ctx:PolicyParser.TermsContext):
        pass


    # Enter a parse tree produced by PolicyParser#constant.
    def enterConstant(self, ctx:PolicyParser.ConstantContext):
        pass

    # Exit a parse tree produced by PolicyParser#constant.
    def exitConstant(self, ctx:PolicyParser.ConstantContext):
        pass


    # Enter a parse tree produced by PolicyParser#function.
    def enterFunction(self, ctx:PolicyParser.FunctionContext):
        pass

    # Exit a parse tree produced by PolicyParser#function.
    def exitFunction(self, ctx:PolicyParser.FunctionContext):
        pass


    # Enter a parse tree produced by PolicyParser#device.
    def enterDevice(self, ctx:PolicyParser.DeviceContext):
        pass

    # Exit a parse tree produced by PolicyParser#device.
    def exitDevice(self, ctx:PolicyParser.DeviceContext):
        pass


    # Enter a parse tree produced by PolicyParser#device_attribute.
    def enterDevice_attribute(self, ctx:PolicyParser.Device_attributeContext):
        pass

    # Exit a parse tree produced by PolicyParser#device_attribute.
    def exitDevice_attribute(self, ctx:PolicyParser.Device_attributeContext):
        pass


    # Enter a parse tree produced by PolicyParser#condition_assigned_variable.
    def enterCondition_assigned_variable(self, ctx:PolicyParser.Condition_assigned_variableContext):
        pass

    # Exit a parse tree produced by PolicyParser#condition_assigned_variable.
    def exitCondition_assigned_variable(self, ctx:PolicyParser.Condition_assigned_variableContext):
        pass


    # Enter a parse tree produced by PolicyParser#condition_assignment.
    def enterCondition_assignment(self, ctx:PolicyParser.Condition_assignmentContext):
        pass

    # Exit a parse tree produced by PolicyParser#condition_assignment.
    def exitCondition_assignment(self, ctx:PolicyParser.Condition_assignmentContext):
        pass



del PolicyParser