# Generated from Expr.g4 by ANTLR 4.9.2
from antlr4 import *
from antlr4.atn.ATNSimulator import ATNSimulator

from ExprLexer import ExprLexer
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass
        
    # Enter a parse tree produced by ExprParser#sentence.
    def enterSentence(self, ctx:ExprParser.SentenceContext):
        pass

    # Exit a parse tree produced by ExprParser#sentence.
    def exitSentence(self, ctx:ExprParser.SentenceContext):
        pass
        
        


del ExprParser