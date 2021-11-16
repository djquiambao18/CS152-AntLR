# Requires 'requests' module
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import dictionary_api
import sys
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

        res = ExprVisitor().visitProg(tree)  # Evaluate the expression

        print(sentence)
        sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))

    print("Goodbye!\n")


if __name__ == '__main__':
    main(sys.argv)