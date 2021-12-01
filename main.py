# Requires 'requests' module
# http://docs.python-requests.org/en/master/user/install/#install
from antlr4.Lexer import TokenSource
import requests
import json
import dictionary_api
import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
#!/usr/bin/env python3
app_id = dictionary_api.APP_ID
app_key = dictionary_api.APP_KEY
url = dictionary_api.API_URL
def handleRequest(list):
    url_copy = url
    status_code = 400
    try:
        for i in list:
            url_copy = url + i.lower()
            r = requests.get(url_copy, headers = {'app_id': app_id, 'app_key': app_key})
            json_obj = json.loads(r.text)
            print(json_obj["results"][0]["lexicalEntries"][0]["lexicalCategory"]["id"])
            url_copy = url
    except:
        print("Error handling request: %d", status_code)

def main(argv):
    print("Welcome to the Simple Sentence Interpreter!\n")
    sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))
    while sentence.getText(0, 1) != "q":
        lexer = ExprLexer(sentence)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        # url_copy = url
        stream.fill()
        
        dict = {
            "NOUN_PROPER": "\033[1;34;40mProper Noun\033[0;37;40m",
            "NOUN_PL": "\033[1;33;40mPlural Noun\033[0;37;40m",
            "PRONOUN": "\033[1;31;40mPronoun\033[0;37;40m",
            "NOUN_COMMON": "\033[1;32;40mCommon Noun\033[0;37;40m",
            "ACTION_VERB_S": "\033[1;35;40mSingular Action Verb\033[0;37;40m",
            "ARTICLE": "\033[1;36;40mArticle\033[0;37;40m",
            "LINKING_VERB_S": "\033[1;34;40mSingular Linking Verb\033[0;37;40m",
            "LINKING_VERB_P": "\033[1;30;40mPlural Linking Verb\033[0;37;40m",
            "OBJECT": "\033[1;33;40mObject\033[0;37;40m",
            "OBJECT_VERB": "\033[1;30;40mObject Verb\033[0;37;40m",
        }
        # res = ExprVisitor().visitProg(tree)  # Evaluate the expression
        try:
            if parser.getNumberOfSyntaxErrors() == 0:
                print("Valid sentence")
                for token in stream.tokens:
                    
                    tokenName = ExprParser.symbolicNames[token.type]
                    if tokenName == "WS":
                        continue
                    elif tokenName in dict:
                        print(dict[tokenName] + ": " + token.text)
                    else:
                        print("Not a valid token: " + token.text)

                list = handleRequest(stream.getText().split(' '))
                for i in list:
                        print(i)
            else:
                print("Invalid sentence\n")
        except(RecognitionException):
            print("Recognition Exception\n")
        sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))
            
    print("Thank you for using our program!\n")


if __name__ == '__main__':
    main(sys.argv)