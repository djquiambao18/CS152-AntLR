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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("*\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\5\3\r\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3(\n\3")
        buf.write("\3\3\2\2\4\2\4\2\2\2/\2\6\3\2\2\2\4\'\3\2\2\2\6\7\5\4")
        buf.write("\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\7\4\2\2\n\f\7\7\2\2\13")
        buf.write("\r\7\13\2\2\f\13\3\2\2\2\f\r\3\2\2\2\r(\3\2\2\2\16\17")
        buf.write("\7\4\2\2\17\20\7\7\2\2\20(\7\f\2\2\21\22\7\4\2\2\22\23")
        buf.write("\7\t\2\2\23\24\7\b\2\2\24(\7\13\2\2\25\26\7\3\2\2\26\27")
        buf.write("\7\n\2\2\27\30\7\b\2\2\30(\7\13\2\2\31\32\7\b\2\2\32\33")
        buf.write("\7\6\2\2\33\34\7\7\2\2\34\35\7\b\2\2\35(\7\13\2\2\36\37")
        buf.write("\7\b\2\2\37 \7\6\2\2 (\7\7\2\2!\"\7\b\2\2\"#\7\6\2\2#")
        buf.write("$\7\t\2\2$(\7\f\2\2%&\7\5\2\2&(\7\7\2\2\'\t\3\2\2\2\'")
        buf.write("\16\3\2\2\2\'\21\3\2\2\2\'\25\3\2\2\2\'\31\3\2\2\2\'\36")
        buf.write("\3\2\2\2\'!\3\2\2\2\'%\3\2\2\2(\5\3\2\2\2\4\f\'")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Smartphones'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'is'", "'are'" ]

    symbolicNames = [ "<INVALID>", "NOUN_PL", "NOUN_PROPER", "PRONOUN", 
                      "NOUN_COMMON", "ACTION_VERB_S", "ARTICLE", "LINKING_VERB_S", 
                      "LINKING_VERB_P", "OBJECT", "OBJECT_VERB", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_sentence = 1

    ruleNames =  [ "prog", "sentence" ]

    EOF = Token.EOF
    NOUN_PL=1
    NOUN_PROPER=2
    PRONOUN=3
    NOUN_COMMON=4
    ACTION_VERB_S=5
    ARTICLE=6
    LINKING_VERB_S=7
    LINKING_VERB_P=8
    OBJECT=9
    OBJECT_VERB=10
    NEWLINE=11
    WS=12

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

        def NOUN_PROPER(self):
            return self.getToken(ExprParser.NOUN_PROPER, 0)

        def ACTION_VERB_S(self):
            return self.getToken(ExprParser.ACTION_VERB_S, 0)

        def OBJECT(self):
            return self.getToken(ExprParser.OBJECT, 0)

        def OBJECT_VERB(self):
            return self.getToken(ExprParser.OBJECT_VERB, 0)

        def LINKING_VERB_S(self):
            return self.getToken(ExprParser.LINKING_VERB_S, 0)

        def ARTICLE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ARTICLE)
            else:
                return self.getToken(ExprParser.ARTICLE, i)

        def NOUN_PL(self):
            return self.getToken(ExprParser.NOUN_PL, 0)

        def LINKING_VERB_P(self):
            return self.getToken(ExprParser.LINKING_VERB_P, 0)

        def NOUN_COMMON(self):
            return self.getToken(ExprParser.NOUN_COMMON, 0)

        def PRONOUN(self):
            return self.getToken(ExprParser.PRONOUN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = ExprParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(ExprParser.NOUN_PROPER)
                self.state = 8
                self.match(ExprParser.ACTION_VERB_S)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ExprParser.OBJECT:
                    self.state = 9
                    self.match(ExprParser.OBJECT)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(ExprParser.NOUN_PROPER)
                self.state = 13
                self.match(ExprParser.ACTION_VERB_S)
                self.state = 14
                self.match(ExprParser.OBJECT_VERB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(ExprParser.NOUN_PROPER)
                self.state = 16
                self.match(ExprParser.LINKING_VERB_S)
                self.state = 17
                self.match(ExprParser.ARTICLE)
                self.state = 18
                self.match(ExprParser.OBJECT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.match(ExprParser.NOUN_PL)
                self.state = 20
                self.match(ExprParser.LINKING_VERB_P)
                self.state = 21
                self.match(ExprParser.ARTICLE)
                self.state = 22
                self.match(ExprParser.OBJECT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 23
                self.match(ExprParser.ARTICLE)
                self.state = 24
                self.match(ExprParser.NOUN_COMMON)
                self.state = 25
                self.match(ExprParser.ACTION_VERB_S)
                self.state = 26
                self.match(ExprParser.ARTICLE)
                self.state = 27
                self.match(ExprParser.OBJECT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.match(ExprParser.ARTICLE)
                self.state = 29
                self.match(ExprParser.NOUN_COMMON)
                self.state = 30
                self.match(ExprParser.ACTION_VERB_S)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 31
                self.match(ExprParser.ARTICLE)
                self.state = 32
                self.match(ExprParser.NOUN_COMMON)
                self.state = 33
                self.match(ExprParser.LINKING_VERB_S)
                self.state = 34
                self.match(ExprParser.OBJECT_VERB)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 35
                self.match(ExprParser.PRONOUN)
                self.state = 36
                self.match(ExprParser.ACTION_VERB_S)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





