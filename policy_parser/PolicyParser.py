# Generated from Policy.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,224,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,1,1,1,3,1,52,8,1,1,2,
        1,2,1,2,1,2,1,2,1,3,3,3,60,8,3,1,3,1,3,3,3,64,8,3,1,3,3,3,67,8,3,
        1,3,1,3,1,3,1,3,3,3,73,8,3,1,3,3,3,76,8,3,1,3,1,3,1,3,1,3,3,3,82,
        8,3,1,3,1,3,3,3,86,8,3,1,3,1,3,3,3,90,8,3,3,3,92,8,3,1,4,3,4,95,
        8,4,1,4,1,4,3,4,99,8,4,1,4,3,4,102,8,4,1,4,1,4,1,4,1,4,3,4,108,8,
        4,1,4,1,4,1,4,1,4,3,4,114,8,4,1,4,1,4,3,4,118,8,4,1,4,1,4,3,4,122,
        8,4,3,4,124,8,4,1,5,3,5,127,8,5,1,5,1,5,1,5,1,5,3,5,133,8,5,1,5,
        1,5,3,5,137,8,5,1,6,3,6,140,8,6,1,6,1,6,3,6,144,8,6,1,6,3,6,147,
        8,6,1,6,1,6,1,6,1,6,3,6,153,8,6,1,6,1,6,1,6,1,6,3,6,159,8,6,1,6,
        1,6,3,6,163,8,6,3,6,165,8,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,173,8,7,
        10,7,12,7,176,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,185,8,8,1,9,1,
        9,1,9,1,9,1,9,1,10,3,10,193,8,10,1,10,1,10,1,10,1,10,3,10,199,8,
        10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,
        16,3,16,214,8,16,1,16,1,16,1,16,3,16,219,8,16,1,16,3,16,222,8,16,
        1,16,0,1,14,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,1,
        1,0,11,14,253,0,37,1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,91,1,0,0,
        0,8,123,1,0,0,0,10,136,1,0,0,0,12,164,1,0,0,0,14,166,1,0,0,0,16,
        184,1,0,0,0,18,186,1,0,0,0,20,198,1,0,0,0,22,200,1,0,0,0,24,202,
        1,0,0,0,26,204,1,0,0,0,28,206,1,0,0,0,30,208,1,0,0,0,32,210,1,0,
        0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,44,3,4,2,0,41,43,3,2,1,0,
        42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,
        0,0,0,46,44,1,0,0,0,47,48,5,0,0,1,48,1,1,0,0,0,49,52,3,4,2,0,50,
        52,3,32,16,0,51,49,1,0,0,0,51,50,1,0,0,0,52,3,1,0,0,0,53,54,5,3,
        0,0,54,55,3,6,3,0,55,56,5,4,0,0,56,57,3,12,6,0,57,5,1,0,0,0,58,60,
        5,21,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,63,3,8,4,0,
        62,64,5,22,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,92,1,0,0,0,65,67,5,
        21,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,3,8,4,0,69,
        70,5,5,0,0,70,72,3,6,3,0,71,73,5,22,0,0,72,71,1,0,0,0,72,73,1,0,
        0,0,73,92,1,0,0,0,74,76,5,21,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,
        77,1,0,0,0,77,78,3,8,4,0,78,79,5,6,0,0,79,81,3,6,3,0,80,82,5,22,
        0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,92,1,0,0,0,83,85,5,7,0,0,84,86,
        5,21,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,89,3,6,3,0,
        88,90,5,22,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,59,1,
        0,0,0,91,66,1,0,0,0,91,75,1,0,0,0,91,83,1,0,0,0,92,7,1,0,0,0,93,
        95,5,21,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,98,3,10,
        5,0,97,99,5,22,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,124,1,0,0,0,100,
        102,5,21,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,
        104,3,10,5,0,104,105,5,5,0,0,105,107,3,8,4,0,106,108,5,22,0,0,107,
        106,1,0,0,0,107,108,1,0,0,0,108,124,1,0,0,0,109,110,3,10,5,0,110,
        111,5,6,0,0,111,113,3,8,4,0,112,114,5,22,0,0,113,112,1,0,0,0,113,
        114,1,0,0,0,114,124,1,0,0,0,115,117,5,7,0,0,116,118,5,21,0,0,117,
        116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,121,3,8,4,0,120,
        122,5,22,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,
        94,1,0,0,0,123,101,1,0,0,0,123,109,1,0,0,0,123,115,1,0,0,0,124,9,
        1,0,0,0,125,127,5,21,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,
        1,0,0,0,128,129,3,14,7,0,129,130,5,19,0,0,130,132,3,14,7,0,131,133,
        5,22,0,0,132,131,1,0,0,0,132,133,1,0,0,0,133,137,1,0,0,0,134,137,
        3,30,15,0,135,137,5,8,0,0,136,126,1,0,0,0,136,134,1,0,0,0,136,135,
        1,0,0,0,137,11,1,0,0,0,138,140,5,21,0,0,139,138,1,0,0,0,139,140,
        1,0,0,0,140,141,1,0,0,0,141,143,3,6,3,0,142,144,5,22,0,0,143,142,
        1,0,0,0,143,144,1,0,0,0,144,165,1,0,0,0,145,147,5,21,0,0,146,145,
        1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,3,6,3,0,149,150,
        5,9,0,0,150,152,3,12,6,0,151,153,5,22,0,0,152,151,1,0,0,0,152,153,
        1,0,0,0,153,165,1,0,0,0,154,155,5,10,0,0,155,165,3,12,6,0,156,158,
        5,7,0,0,157,159,5,21,0,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,
        1,0,0,0,160,162,3,12,6,0,161,163,5,22,0,0,162,161,1,0,0,0,162,163,
        1,0,0,0,163,165,1,0,0,0,164,139,1,0,0,0,164,146,1,0,0,0,164,154,
        1,0,0,0,164,156,1,0,0,0,165,13,1,0,0,0,166,167,6,7,-1,0,167,168,
        3,16,8,0,168,174,1,0,0,0,169,170,10,1,0,0,170,171,5,20,0,0,171,173,
        3,16,8,0,172,169,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,
        1,0,0,0,175,15,1,0,0,0,176,174,1,0,0,0,177,185,3,30,15,0,178,179,
        3,26,13,0,179,180,5,1,0,0,180,181,3,28,14,0,181,185,1,0,0,0,182,
        185,3,22,11,0,183,185,3,18,9,0,184,177,1,0,0,0,184,178,1,0,0,0,184,
        182,1,0,0,0,184,183,1,0,0,0,185,17,1,0,0,0,186,187,3,24,12,0,187,
        188,5,21,0,0,188,189,3,20,10,0,189,190,5,22,0,0,190,19,1,0,0,0,191,
        193,3,16,8,0,192,191,1,0,0,0,192,193,1,0,0,0,193,199,1,0,0,0,194,
        195,3,16,8,0,195,196,5,23,0,0,196,197,3,20,10,0,197,199,1,0,0,0,
        198,192,1,0,0,0,198,194,1,0,0,0,199,21,1,0,0,0,200,201,7,0,0,0,201,
        23,1,0,0,0,202,203,5,18,0,0,203,25,1,0,0,0,204,205,5,18,0,0,205,
        27,1,0,0,0,206,207,5,18,0,0,207,29,1,0,0,0,208,209,5,18,0,0,209,
        31,1,0,0,0,210,211,3,30,15,0,211,213,5,2,0,0,212,214,5,21,0,0,213,
        212,1,0,0,0,213,214,1,0,0,0,214,218,1,0,0,0,215,219,3,8,4,0,216,
        219,3,22,11,0,217,219,3,18,9,0,218,215,1,0,0,0,218,216,1,0,0,0,218,
        217,1,0,0,0,219,221,1,0,0,0,220,222,5,22,0,0,221,220,1,0,0,0,221,
        222,1,0,0,0,222,33,1,0,0,0,37,37,44,51,59,63,66,72,75,81,85,89,91,
        94,98,101,107,113,117,121,123,126,132,136,139,143,146,152,158,162,
        164,174,184,192,198,213,218,221
    ]

class PolicyParser ( Parser ):

    grammarFileName = "Policy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'='", "'If'", "'Then'", "'and'", 
                     "'or'", "'not'", "'true'", "'since'", "'yesterday'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "THEN", 
                      "AND", "OR", "NOT", "TRUE", "SINCE", "YESTERDAY", 
                      "INTEGER", "REAL_NUMBER", "STRING", "TIME", "HOUR", 
                      "MINUTE", "SECOND", "IDENTIFIER", "RELATIONAL_OP", 
                      "ARITHMATIC_OP", "OPEN_PAREN", "CLOSED_PAREN", "COMMA", 
                      "WHITESPACE", "NEWLINE", "COMMENTS" ]

    RULE_policy = 0
    RULE_statements = 1
    RULE_invariant = 2
    RULE_if_condition = 3
    RULE_predicate = 4
    RULE_predicate_factor = 5
    RULE_then_condition = 6
    RULE_term = 7
    RULE_term_factor = 8
    RULE_function_call = 9
    RULE_terms = 10
    RULE_constant = 11
    RULE_function = 12
    RULE_device = 13
    RULE_device_attribute = 14
    RULE_condition_assigned_variable = 15
    RULE_condition_assignment = 16

    ruleNames =  [ "policy", "statements", "invariant", "if_condition", 
                   "predicate", "predicate_factor", "then_condition", "term", 
                   "term_factor", "function_call", "terms", "constant", 
                   "function", "device", "device_attribute", "condition_assigned_variable", 
                   "condition_assignment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    THEN=4
    AND=5
    OR=6
    NOT=7
    TRUE=8
    SINCE=9
    YESTERDAY=10
    INTEGER=11
    REAL_NUMBER=12
    STRING=13
    TIME=14
    HOUR=15
    MINUTE=16
    SECOND=17
    IDENTIFIER=18
    RELATIONAL_OP=19
    ARITHMATIC_OP=20
    OPEN_PAREN=21
    CLOSED_PAREN=22
    COMMA=23
    WHITESPACE=24
    NEWLINE=25
    COMMENTS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def invariant(self):
            return self.getTypedRuleContext(PolicyParser.InvariantContext,0)


        def EOF(self):
            return self.getToken(PolicyParser.EOF, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolicyParser.StatementsContext)
            else:
                return self.getTypedRuleContext(PolicyParser.StatementsContext,i)


        def getRuleIndex(self):
            return PolicyParser.RULE_policy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy" ):
                listener.enterPolicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy" ):
                listener.exitPolicy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicy" ):
                return visitor.visitPolicy(self)
            else:
                return visitor.visitChildren(self)




    def policy(self):

        localctx = PolicyParser.PolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.statements() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 40
            self.invariant()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==18:
                self.state = 41
                self.statements()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(PolicyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def invariant(self):
            return self.getTypedRuleContext(PolicyParser.InvariantContext,0)


        def condition_assignment(self):
            return self.getTypedRuleContext(PolicyParser.Condition_assignmentContext,0)


        def getRuleIndex(self):
            return PolicyParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = PolicyParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.invariant()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.condition_assignment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvariantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PolicyParser.IF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(PolicyParser.If_conditionContext,0)


        def THEN(self):
            return self.getToken(PolicyParser.THEN, 0)

        def then_condition(self):
            return self.getTypedRuleContext(PolicyParser.Then_conditionContext,0)


        def getRuleIndex(self):
            return PolicyParser.RULE_invariant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvariant" ):
                listener.enterInvariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvariant" ):
                listener.exitInvariant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvariant" ):
                return visitor.visitInvariant(self)
            else:
                return visitor.visitChildren(self)




    def invariant(self):

        localctx = PolicyParser.InvariantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_invariant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PolicyParser.IF)
            self.state = 54
            self.if_condition()
            self.state = 55
            self.match(PolicyParser.THEN)
            self.state = 56
            self.then_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(PolicyParser.PredicateContext,0)


        def OPEN_PAREN(self):
            return self.getToken(PolicyParser.OPEN_PAREN, 0)

        def CLOSED_PAREN(self):
            return self.getToken(PolicyParser.CLOSED_PAREN, 0)

        def AND(self):
            return self.getToken(PolicyParser.AND, 0)

        def if_condition(self):
            return self.getTypedRuleContext(PolicyParser.If_conditionContext,0)


        def OR(self):
            return self.getToken(PolicyParser.OR, 0)

        def NOT(self):
            return self.getToken(PolicyParser.NOT, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_if_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_condition" ):
                listener.enterIf_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_condition" ):
                listener.exitIf_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = PolicyParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_condition)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 61
                self.predicate()
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 65
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 68
                self.predicate()
                self.state = 69
                self.match(PolicyParser.AND)
                self.state = 70
                self.if_condition()
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 71
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 74
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 77
                self.predicate()
                self.state = 78
                self.match(PolicyParser.OR)
                self.state = 79
                self.if_condition()
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 80
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.match(PolicyParser.NOT)
                self.state = 85
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 84
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 87
                self.if_condition()
                self.state = 89
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 88
                    self.match(PolicyParser.CLOSED_PAREN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate_factor(self):
            return self.getTypedRuleContext(PolicyParser.Predicate_factorContext,0)


        def OPEN_PAREN(self):
            return self.getToken(PolicyParser.OPEN_PAREN, 0)

        def CLOSED_PAREN(self):
            return self.getToken(PolicyParser.CLOSED_PAREN, 0)

        def AND(self):
            return self.getToken(PolicyParser.AND, 0)

        def predicate(self):
            return self.getTypedRuleContext(PolicyParser.PredicateContext,0)


        def OR(self):
            return self.getToken(PolicyParser.OR, 0)

        def NOT(self):
            return self.getToken(PolicyParser.NOT, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = PolicyParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_predicate)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 96
                self.predicate_factor()
                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 100
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 103
                self.predicate_factor()
                self.state = 104
                self.match(PolicyParser.AND)
                self.state = 105
                self.predicate()
                self.state = 107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.predicate_factor()
                self.state = 110
                self.match(PolicyParser.OR)
                self.state = 111
                self.predicate()
                self.state = 113
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 112
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                self.match(PolicyParser.NOT)
                self.state = 117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 116
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 119
                self.predicate()
                self.state = 121
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 120
                    self.match(PolicyParser.CLOSED_PAREN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolicyParser.TermContext)
            else:
                return self.getTypedRuleContext(PolicyParser.TermContext,i)


        def RELATIONAL_OP(self):
            return self.getToken(PolicyParser.RELATIONAL_OP, 0)

        def OPEN_PAREN(self):
            return self.getToken(PolicyParser.OPEN_PAREN, 0)

        def CLOSED_PAREN(self):
            return self.getToken(PolicyParser.CLOSED_PAREN, 0)

        def condition_assigned_variable(self):
            return self.getTypedRuleContext(PolicyParser.Condition_assigned_variableContext,0)


        def TRUE(self):
            return self.getToken(PolicyParser.TRUE, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_predicate_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate_factor" ):
                listener.enterPredicate_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate_factor" ):
                listener.exitPredicate_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_factor" ):
                return visitor.visitPredicate_factor(self)
            else:
                return visitor.visitChildren(self)




    def predicate_factor(self):

        localctx = PolicyParser.Predicate_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predicate_factor)
        self._la = 0 # Token type
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 125
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 128
                self.term(0)
                self.state = 129
                self.match(PolicyParser.RELATIONAL_OP)
                self.state = 130
                self.term(0)
                self.state = 132
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 131
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.condition_assigned_variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(PolicyParser.TRUE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Then_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_condition(self):
            return self.getTypedRuleContext(PolicyParser.If_conditionContext,0)


        def OPEN_PAREN(self):
            return self.getToken(PolicyParser.OPEN_PAREN, 0)

        def CLOSED_PAREN(self):
            return self.getToken(PolicyParser.CLOSED_PAREN, 0)

        def SINCE(self):
            return self.getToken(PolicyParser.SINCE, 0)

        def then_condition(self):
            return self.getTypedRuleContext(PolicyParser.Then_conditionContext,0)


        def YESTERDAY(self):
            return self.getToken(PolicyParser.YESTERDAY, 0)

        def NOT(self):
            return self.getToken(PolicyParser.NOT, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_then_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThen_condition" ):
                listener.enterThen_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThen_condition" ):
                listener.exitThen_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThen_condition" ):
                return visitor.visitThen_condition(self)
            else:
                return visitor.visitChildren(self)




    def then_condition(self):

        localctx = PolicyParser.Then_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_then_condition)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 138
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 141
                self.if_condition()
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 142
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 145
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 148
                self.if_condition()
                self.state = 149
                self.match(PolicyParser.SINCE)
                self.state = 150
                self.then_condition()
                self.state = 152
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 151
                    self.match(PolicyParser.CLOSED_PAREN)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.match(PolicyParser.YESTERDAY)
                self.state = 155
                self.then_condition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(PolicyParser.NOT)
                self.state = 158
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 157
                    self.match(PolicyParser.OPEN_PAREN)


                self.state = 160
                self.then_condition()
                self.state = 162
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 161
                    self.match(PolicyParser.CLOSED_PAREN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_factor(self):
            return self.getTypedRuleContext(PolicyParser.Term_factorContext,0)


        def term(self):
            return self.getTypedRuleContext(PolicyParser.TermContext,0)


        def ARITHMATIC_OP(self):
            return self.getToken(PolicyParser.ARITHMATIC_OP, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PolicyParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.term_factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PolicyParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 169
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 170
                    self.match(PolicyParser.ARITHMATIC_OP)
                    self.state = 171
                    self.term_factor() 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_assigned_variable(self):
            return self.getTypedRuleContext(PolicyParser.Condition_assigned_variableContext,0)


        def device(self):
            return self.getTypedRuleContext(PolicyParser.DeviceContext,0)


        def device_attribute(self):
            return self.getTypedRuleContext(PolicyParser.Device_attributeContext,0)


        def constant(self):
            return self.getTypedRuleContext(PolicyParser.ConstantContext,0)


        def function_call(self):
            return self.getTypedRuleContext(PolicyParser.Function_callContext,0)


        def getRuleIndex(self):
            return PolicyParser.RULE_term_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_factor" ):
                listener.enterTerm_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_factor" ):
                listener.exitTerm_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_factor" ):
                return visitor.visitTerm_factor(self)
            else:
                return visitor.visitChildren(self)




    def term_factor(self):

        localctx = PolicyParser.Term_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term_factor)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.condition_assigned_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.device()
                self.state = 179
                self.match(PolicyParser.T__0)
                self.state = 180
                self.device_attribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(PolicyParser.FunctionContext,0)


        def OPEN_PAREN(self):
            return self.getToken(PolicyParser.OPEN_PAREN, 0)

        def terms(self):
            return self.getTypedRuleContext(PolicyParser.TermsContext,0)


        def CLOSED_PAREN(self):
            return self.getToken(PolicyParser.CLOSED_PAREN, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = PolicyParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.function()
            self.state = 187
            self.match(PolicyParser.OPEN_PAREN)
            self.state = 188
            self.terms()
            self.state = 189
            self.match(PolicyParser.CLOSED_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_factor(self):
            return self.getTypedRuleContext(PolicyParser.Term_factorContext,0)


        def COMMA(self):
            return self.getToken(PolicyParser.COMMA, 0)

        def terms(self):
            return self.getTypedRuleContext(PolicyParser.TermsContext,0)


        def getRuleIndex(self):
            return PolicyParser.RULE_terms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerms" ):
                listener.enterTerms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerms" ):
                listener.exitTerms(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerms" ):
                return visitor.visitTerms(self)
            else:
                return visitor.visitChildren(self)




    def terms(self):

        localctx = PolicyParser.TermsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_terms)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 292864) != 0):
                    self.state = 191
                    self.term_factor()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.term_factor()
                self.state = 195
                self.match(PolicyParser.COMMA)
                self.state = 196
                self.terms()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME(self):
            return self.getToken(PolicyParser.TIME, 0)

        def INTEGER(self):
            return self.getToken(PolicyParser.INTEGER, 0)

        def REAL_NUMBER(self):
            return self.getToken(PolicyParser.REAL_NUMBER, 0)

        def STRING(self):
            return self.getToken(PolicyParser.STRING, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = PolicyParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PolicyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = PolicyParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(PolicyParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PolicyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_device

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDevice" ):
                listener.enterDevice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDevice" ):
                listener.exitDevice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDevice" ):
                return visitor.visitDevice(self)
            else:
                return visitor.visitChildren(self)




    def device(self):

        localctx = PolicyParser.DeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_device)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(PolicyParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Device_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PolicyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_device_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDevice_attribute" ):
                listener.enterDevice_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDevice_attribute" ):
                listener.exitDevice_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDevice_attribute" ):
                return visitor.visitDevice_attribute(self)
            else:
                return visitor.visitChildren(self)




    def device_attribute(self):

        localctx = PolicyParser.Device_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_device_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(PolicyParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_assigned_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PolicyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_condition_assigned_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_assigned_variable" ):
                listener.enterCondition_assigned_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_assigned_variable" ):
                listener.exitCondition_assigned_variable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_assigned_variable" ):
                return visitor.visitCondition_assigned_variable(self)
            else:
                return visitor.visitChildren(self)




    def condition_assigned_variable(self):

        localctx = PolicyParser.Condition_assigned_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condition_assigned_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(PolicyParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_assigned_variable(self):
            return self.getTypedRuleContext(PolicyParser.Condition_assigned_variableContext,0)


        def predicate(self):
            return self.getTypedRuleContext(PolicyParser.PredicateContext,0)


        def constant(self):
            return self.getTypedRuleContext(PolicyParser.ConstantContext,0)


        def function_call(self):
            return self.getTypedRuleContext(PolicyParser.Function_callContext,0)


        def OPEN_PAREN(self):
            return self.getToken(PolicyParser.OPEN_PAREN, 0)

        def CLOSED_PAREN(self):
            return self.getToken(PolicyParser.CLOSED_PAREN, 0)

        def getRuleIndex(self):
            return PolicyParser.RULE_condition_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_assignment" ):
                listener.enterCondition_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_assignment" ):
                listener.exitCondition_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_assignment" ):
                return visitor.visitCondition_assignment(self)
            else:
                return visitor.visitChildren(self)




    def condition_assignment(self):

        localctx = PolicyParser.Condition_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.condition_assigned_variable()
            self.state = 211
            self.match(PolicyParser.T__1)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 212
                self.match(PolicyParser.OPEN_PAREN)


            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 215
                self.predicate()
                pass

            elif la_ == 2:
                self.state = 216
                self.constant()
                pass

            elif la_ == 3:
                self.state = 217
                self.function_call()
                pass


            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 220
                self.match(PolicyParser.CLOSED_PAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




