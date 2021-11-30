grammar Expr;

prog: sentence EOF;

//Parser rules -> valid sentence structures

sentence: NOUN_PROPER ACTION_VERB_S (OBJECT)?
        | NOUN_PROPER ACTION_VERB_S OBJECT_VERB
        | NOUN_PROPER LINKING_VERB_S ARTICLE OBJECT
        | NOUN_PL LINKING_VERB_P ARTICLE OBJECT
        | ARTICLE NOUN_COMMON ACTION_VERB_S (ARTICLE OBJECT)?
        | PRONOUN ACTION_VERB_S
;


//Lexer rules
NOUN_PL: 'Smartphones';

NOUN_PROPER: 'Chris' | 'Ramanujan' | 'Gordon' | 'Hawaii'
           | 'Katie' | 'Tim' | 'Darwish' | 'Harry' | 'California'
           ;
PRONOUN: 'He' | 'She' | 'It' | 'it' | 'she' | 'he'
       ;

NOUN_COMMON: 'Man' | 'Woman' | 'man' | 'woman' | 'person' | 'professor'
           ;

ACTION_VERB_S: 'cooks' | 'loves' | 'cries' | 'moves' | 'teaches' | 'likes'
             ;
ARTICLE: 'a' | 'an' | 'the' | 'The'
        ;

LINKING_VERB_S: 'is';
LINKING_VERB_P: 'are';

OBJECT: 'spaghetti' | 'Mathematics' | 'State' | 'state' | 'class' | 'device'
        ;
OBJECT_VERB: 'walking' | 'eating' | 'sleeping' | 'running' | 'talking'
           | 'swimming' | 'playing' | 'dancing' | 'reading' | 'writing'
          ;

NEWLINE : [\r\n]+ ;
WS : [ \r\n\t] + -> channel(HIDDEN);