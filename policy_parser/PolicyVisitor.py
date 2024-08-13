# Generated from Policy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PolicyParser import PolicyParser
else:
    from PolicyParser import PolicyParser

# This class defines a complete generic visitor for a parse tree produced by PolicyParser.

class PolicyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolicyParser#policy.
    def visitPolicy(self, ctx:PolicyParser.PolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#statements.
    def visitStatements(self, ctx:PolicyParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#invariant.
    def visitInvariant(self, ctx:PolicyParser.InvariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#if_condition.
    def visitIf_condition(self, ctx:PolicyParser.If_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#predicate.
    def visitPredicate(self, ctx:PolicyParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#predicate_factor.
    def visitPredicate_factor(self, ctx:PolicyParser.Predicate_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#then_condition.
    def visitThen_condition(self, ctx:PolicyParser.Then_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#term.
    def visitTerm(self, ctx:PolicyParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#term_factor.
    def visitTerm_factor(self, ctx:PolicyParser.Term_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#function_call.
    def visitFunction_call(self, ctx:PolicyParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#terms.
    def visitTerms(self, ctx:PolicyParser.TermsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#constant.
    def visitConstant(self, ctx:PolicyParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#function.
    def visitFunction(self, ctx:PolicyParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#device.
    def visitDevice(self, ctx:PolicyParser.DeviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#device_attribute.
    def visitDevice_attribute(self, ctx:PolicyParser.Device_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#condition_assigned_variable.
    def visitCondition_assigned_variable(self, ctx:PolicyParser.Condition_assigned_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#condition_assignment.
    def visitCondition_assignment(self, ctx:PolicyParser.Condition_assignmentContext):
        return self.visitChildren(ctx)



del PolicyParser