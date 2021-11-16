# Generated from Expr.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\25\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\5\3\13\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\23\n\3\3\3\2\2\4\2\4\2\2\2\26\2\6")
        buf.write("\3\2\2\2\4\n\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2")
        buf.write("\2\t\13\7\17\2\2\n\t\3\2\2\2\n\13\3\2\2\2\13\f\3\2\2\2")
        buf.write("\f\r\7\3\2\2\r\22\7\4\2\2\16\23\7\16\2\2\17\23\7\20\2")
        buf.write("\2\20\21\7\17\2\2\21\23\7\20\2\2\22\16\3\2\2\2\22\17\3")
        buf.write("\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\5\3\2\2\2\4\n\22")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'are'", "'is'" ]

    symbolicNames = [ "<INVALID>", "SUBJECT", "VERB", "SUBJECT_PLURAL", 
                      "SUBJECT_SINGULAR", "SUBJECT_SELF", "NOUN_SELF", "VERB_SELF", 
                      "NOUN_S", "NOUN_P", "VERB_P", "VERB_S", "ACTION", 
                      "ARTICLE", "OBJECT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_sentence = 1

    ruleNames =  [ "prog", "sentence" ]

    EOF = Token.EOF
    SUBJECT=1
    VERB=2
    SUBJECT_PLURAL=3
    SUBJECT_SINGULAR=4
    SUBJECT_SELF=5
    NOUN_SELF=6
    VERB_SELF=7
    NOUN_S=8
    NOUN_P=9
    VERB_P=10
    VERB_S=11
    ACTION=12
    ARTICLE=13
    OBJECT=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(ExprParser.SentenceContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.sentence()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBJECT(self):
            return self.getToken(ExprParser.SUBJECT, 0)

        def VERB(self):
            return self.getToken(ExprParser.VERB, 0)

        def ARTICLE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ARTICLE)
            else:
                return self.getToken(ExprParser.ARTICLE, i)

        def ACTION(self):
            return self.getToken(ExprParser.ACTION, 0)

        def OBJECT(self):
            return self.getToken(ExprParser.OBJECT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = ExprParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExprParser.ARTICLE:
                self.state = 7
                self.match(ExprParser.ARTICLE)


            self.state = 10
            self.match(ExprParser.SUBJECT)
            self.state = 11
            self.match(ExprParser.VERB)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.ACTION]:
                self.state = 12
                self.match(ExprParser.ACTION)
                pass
            elif token in [ExprParser.OBJECT]:
                self.state = 13
                self.match(ExprParser.OBJECT)
                pass
            elif token in [ExprParser.ARTICLE]:
                self.state = 14
                self.match(ExprParser.ARTICLE)
                self.state = 15
                self.match(ExprParser.OBJECT)
                pass
            elif token in [ExprParser.EOF]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





