grammar Expr;

prog: sentence EOF;

//Parser rules -> valid sentence structures
sentence: (ARTICLE)? SUBJECT LINKING_VERB (ACTION | OBJECT | ARTICLE OBJECT)? ;
//    | SUBJECT VERB OBJECT
//    | SUBJECT VERB OBJECT
//    | SUBJECT VERB
//    | ARTICLE SUBJECT VERB ARTICLE OBJECT
//    | ARTICLE SUBJECT VERB OBJECT
//    | ARTICLE SUBJECT VERB VERB
//    | ARTICLE SUBJECT VERB ACTION
//    | SUBJECT VERB ACTION
//    | SUBJECT VERB ARTICLE OBJECT;

//Lexer rules:

SUBJECT :  SUBJECT_SINGULAR | SUBJECT_PLURAL;
LINKING_VERB : VERB_P | VERB_S;
SUBJECT_PLURAL : NOUN_P;
SUBJECT_SINGULAR : NOUN_S;
SUBJECT_SELF : NOUN_SELF VERB_SELF;
NOUN_SELF : 'I' | 'i';
VERB_SELF : 'am' | 'Am';
NOUN_S :  'He' | 'he' | 'she' | 'She'
     | 'Tim' | 'Mike' | 'Darwish' | 'man' | 'woman' | 'professor';

NOUN_P : 'They' | 'they';
VERB_P : 'are';
VERB_S : 'is';

ACTION : 'eats' | 'dances' | 'walks' | 'walking' | 'talking' | 'running'
     | 'cries' | 'crying' | 'moves' | 'teaches' | 'teaching';

ARTICLE : 'a' | 'A' | 'The' | 'the' | 'An' | 'an';
OBJECT : 'spoon' | 'food' | 'drink' | 'class';

NEWLINE : [\r\n]+ ;
WS : [ \r\n\t] + -> channel(HIDDEN);