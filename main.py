# Requires 'requests' module
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import dictionary_api
import sys
import antlr4
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
app_id = dictionary_api.APP_ID
app_key = dictionary_api.APP_KEY
url = dictionary_api.API_URL

def main(argv):
    #input = InputStream("Tim is walking")

    sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))
    while sentence.getText(0, 1) != "q":
        lexer = ExprLexer(sentence)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        # url_copy = url
        stream.fill()
        
        # res = ExprVisitor().visitProg(tree)  # Evaluate the expression
        try:
            if parser.getNumberOfSyntaxErrors() == 0:
                print("Valid sentence")
                for token in stream.tokens:
                    print(token.text, token.type, token.line)
                # print([token.text for token in stream.tokens][:-1])
                stream.tokenSource
                # for child in tree.children:
                #     print(child.getText())
                    #if child.
                    # print(" is a Valid sentence\n")
            # print(parser.getInputStream().getText())
            # list = stream.getText().split(' ')
            # for i in list:
            #     try:
            #         url_copy += i.lower()
            #         r = requests.get(url_copy, headers = {'app_id': app_id, 'app_key': app_key})
            #         json_obj = json.loads(r.text)
                    
            #         print(json_obj["results"][0]["lexicalEntries"][0]["lexicalCategory"]["id"])
            #         url_copy = url
            #     except:
            #         print("Error")
            # #print(sentence)
            # for i in list:
            #         print(i)
            # handleSentence(tree)
            else:
                print("Invalid sentence\n")
        except(RecognitionException):
            RecognitionException.printStackTrace()
            print("Invalid sentence")
            RecognitionException.getExpectedTokens()
        sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))
        # print(parser.getErrorHeader())
        # print("Invalid sentence\n")
            

    print("Goodbye!\n")


if __name__ == '__main__':
    main(sys.argv)