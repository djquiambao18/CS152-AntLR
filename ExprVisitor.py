# Generated from Expr.g4 by ANTLR 4.9.2
from antlr4 import *
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
        try:
                ctx.getTypedRuleContext
            # if not ctx.exception:
                print("\nValid sentence")
                ctx.getTypedRuleContext
                # for i in range(ctx.getChildCount()):
                #     print(ctx.getChild(i))
            # else:
            #     print("\nInvalid sentence")
        except:
            print("\nInvalid sentence")
        # return not ctx.exception




del ExprParser