
from antlr4 import *
from .PolicyParser import PolicyParser
from .PolicyVisitor import PolicyVisitor

class CustomPolicyVisitor(PolicyVisitor):
    def __init__(self, relaxed=False):
        self.relaxed = relaxed
        self.condition_assignment_variables_declared = []
        self.condition_assignment_variables_used = []

    # Visit a parse tree produced by MaverickParser#policy.
    def visitPolicy(self, ctx:PolicyParser.PolicyContext):
        res = self.visitChildren(ctx)
        for var in self.condition_assignment_variables_used:
            if var not in self.condition_assignment_variables_declared and not self.relaxed:
                raise Exception(f"'{var}' condition assignment used but not declared")
        return res

    # Visit a parse tree produced by PolicyParser#predicate_factor.
    def visitPredicate_factor(self, ctx:PolicyParser.Predicate_factorContext):
        child_count = ctx.getChildCount()
        if child_count == 1:
            condition_assignment_variable = ctx.getChild(0).getText()
            if condition_assignment_variable != "true":
                self.condition_assignment_variables_used.append(condition_assignment_variable)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolicyParser#term_factor.
    def visitTerm_factor(self, ctx:PolicyParser.Term_factorContext):
        child = ctx.getChild(0)
        if isinstance(child, PolicyParser.Condition_assigned_variableContext):
            self.condition_assignment_variables_used.append(child.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#condition_assignment.
    def visitCondition_assignment(self, ctx:PolicyParser.Condition_assignmentContext):
        condition_assignment_variable = ctx.getChild(0).getText()
        self.condition_assignment_variables_declared.append(condition_assignment_variable)
        return self.visitChildren(ctx)
