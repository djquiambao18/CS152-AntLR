# Generated from Expr.g4 by ANTLR 4.9.2
from antlr4 import *
from antlr4.error.Errors import LexerNoViableAltException
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)
    # Visit a parse tree produced by ExprParser#sentence.
    def visitSentence(self, ctx:ExprParser.SentenceContext):
        return self.visitChildren(ctx)
        # if ctx.exception:
        #     return ctx.exception
        # if not ctx.exception:
        #         # ExprVisitor.visitErrorNode()
        #         # value = self.visit(ctx.expr())
        #         # print (value)
        #         # tokenRecognizer = ctx.expr().getText()
        #         print("\nValid sentence")
        #         # print(ctx.getTypedRuleContext)
        #         # print(ctx.expr().getText())
        #         # for i in range(ctx.getChildCount()):
        #         #     print(ctx.getChild(i))
        # else:
        #     print("\nError... Invalid sentence")
        # return not ctx.exception




del ExprParser