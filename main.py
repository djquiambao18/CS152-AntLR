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
#!/usr/bin/env python3
app_id = dictionary_api.APP_ID
app_key = dictionary_api.APP_KEY
url = dictionary_api.API_URL

def handleRequest(list):
    status_code = 400
    fields = 'definitions'
    strictMatch = 'false'
    lexicalCategory = 'verb'
    root_words = []
    #inflections_id = []
    #inflections_text = []
    definitions_map = {}
    
    try:
        # get inflection of word (root form)
        for word in list:
            url_copy = url + 'lemmas/en' + '/' + word.lower() + '?lexicalCategory=' + lexicalCategory

            r = requests.get(url_copy, headers = {'app_id': app_id, 'app_key': app_key})
            json_obj = json.loads(r.text)

            status_code  = r.status_code
            if status_code == 200:
                root_words.append(json_obj["results"][0]["lexicalEntries"][0]["inflectionOf"][0]["text"])
                
            else:
                print("Error code: ", status_code)

        # get definition and lexical category of root word
        index = 0
        for word in root_words:
            url_copy = url + 'entries/en-us' + '/' + word.lower() + '?' + 'fields=' + fields + '&lexicalCategory=' + lexicalCategory +'&strictMatch=' + strictMatch
            
            r = requests.get(url_copy, headers = {'app_id': app_id, 'app_key': app_key})
            status_code  = r.status_code
            if status_code == 200:
                json_obj = json.loads(r.text)

                #load definition from json object
                definition = json_obj["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
                
                definitions_map.update({word : definition})
                
            else:
                print("No definition found for " + word)
                print("Error code: ", status_code)
        return definitions_map
    except(Exception) as e:
        print("Error handling request")

def main(argv):
    print("Welcome to the Simple Sentence Interpreter!\n")
    sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))

    while sentence.getText(0, 1) != "q":
        lexer = ExprLexer(sentence)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        stream.fill()
        
        dict = {
            "NOUN_PROPER": "Proper Noun",
            "NOUN_PL": "Plural Noun",
            "PRONOUN": "Pronoun",
            "NOUN_COMMON": "Common Noun",
            "ACTION_VERB_S": "Singular Action Verb",
            "ARTICLE": "Article",
            "LINKING_VERB_S": "Singular Linking Verb",
            "LINKING_VERB_P": "Plural Linking Verb",
            "OBJECT": "Object",
            "OBJECT_VERB": "Object Verb",
        }

        try:
            req_words = []
            if parser.getNumberOfSyntaxErrors() == 0:
                print("\nValid sentence")
                
                for token in stream.tokens:
                    tokenName = ExprParser.symbolicNames[token.type]
                    if tokenName == "WS":
                        continue
                    elif tokenName in dict:
                        print(dict[tokenName] + ": " + token.text)
                        if tokenName == "ACTION_VERB_S" or tokenName == "OBJECT_VERB":
                            req_words.append(token.text) 
                    else:
                        print("Not a valid token: " + token.text)
                if len(req_words) > 0:
                    print("\nDictionary definitions for the verb words in their root form\n")
                    definitions_map = handleRequest(req_words)
            
                    for key, value in definitions_map.items():
                        print(str(key) + ": " + str(value))
            else:
                print("Invalid sentence\n")
        except(Exception) as e:
            print("Error: Invalid sentence\n")
        sentence = InputStream(input('Please enter a sentence or "q" to exit: \n'))
            
    print("Thank you for using our program!\n")


if __name__ == '__main__':
    main(sys.argv)