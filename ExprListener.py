# Generated from Expr.g4 by ANTLR 4.9.2
from antlr4 import *
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
        # for child in ctx.getChildren():
        #     print(child.getText())
        #     for i in range(len(ctx.getTokens())):
        #         print(ctx.getTokens()[i].getText())


    # Enter a parse tree produced by ExprParser#sentence.
    def enterSentence(self, ctx:ExprParser.SentenceContext):
        pass

    # Exit a parse tree produced by ExprParser#sentence.
    def exitSentence(self, ctx:ExprParser.SentenceContext):
        pass
        # for child in ctx.getChildren():
        #     print(child.getText())
        #     print(child.getToken())
        


del ExprParser