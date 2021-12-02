grammar Expr;

prog: sentence EOF;

//Parser rules -> valid sentence structures

sentence: NOUN_PROPER ACTION_VERB_S (OBJECT)?
        | NOUN_PROPER ACTION_VERB_S OBJECT_VERB
        | NOUN_PROPER LINKING_VERB_S ARTICLE OBJECT
        | NOUN_PL LINKING_VERB_P ARTICLE OBJECT
        | ARTICLE NOUN_COMMON ACTION_VERB_S (ARTICLE OBJECT)?
        | ARTICLE NOUN_COMMON LINKING_VERB_S OBJECT_VERB
        | PRONOUN ACTION_VERB_S
;


//Lexer rules
NOUN_PL: 'Smartphones';

NOUN_PROPER: 'Chris' | 'Ramanujan' | 'Gordon' | 'Hawaii'
           | 'Katie' | 'Tim' | 'Darwish' | 'Harry' | 'California' | 'Mountain View'
           |'Google' | 'Googleplex' | 'Santa Clara' | 'Los Angeles' | 'Santa Monica' | 'Santa Barbara' | 'Santa Cruz'
           | 'San Diego' | 'San Jose' | 'San Mateo' | 'San Francisco'
           ;
PRONOUN: 'He' | 'She' | 'It' | 'it' | 'she' | 'he' | 'They' | 'they'
       ;

NOUN_COMMON: 'Man' | 'Woman' | 'man' | 'woman' | 'person' | 'professor'
           | 'Professor' | 'Teacher' | 'teacher' | 'Instructor' | 'instructor'
           | 'Student' | 'student'
           ;

ACTION_VERB_S: 'cooks' | 'loves' | 'cries' | 'moves' | 'teaches' | 'likes'
             | 'runs' | 'drinks' | 'eats' | 'studies' | 'works' | 'plays'
             | 'walks' | 'sings' | 'dances' | 'swims' | 'drives' | 'writes'
             | 'barks'
             ;
ARTICLE: 'a' | 'an' | 'the' | 'The'
        ;

LINKING_VERB_S: 'is';
LINKING_VERB_P: 'are';

OBJECT: 'spaghetti' | 'Mathematics' | 'State' | 'state' | 'class' | 'device'
        | 'coffee' | 'tea' | 'water' | 'food' | 'book' | 'computer' | 'table'
        | 'chair' | 'car' | 'house' | 'building' | 'school' | 'university'
        | 'pencil' | 'pen' | 'paper' | 'notebook'
        | 'note' | 'card' | 'cardboard' | 'box' | 'pasta' | 'ramen'
        | 'soup' | 'sushi' | 'rice' | 'bread' | 'sandwich' | 'burger'
        | 'pizza' | 'salad' | 'salmon' | 'fish' | 'chips' | 'chocolate'
        | 'mashed potato' | 'potato' | 'tomato' | 'sausage' | 'egg'
        | 'breakfast' | 'lunch' | 'dinner' | 'dessert' | 'brunch'
        ;
OBJECT_VERB: 'walking' | 'eating' | 'sleeping' | 'running' | 'talking'
           | 'swimming' | 'playing' | 'dancing' | 'reading' | 'writing' | 'cooking'
           | 'driving' | 'studying' | 'working' | 'moving' | 'baking' | 'roasting'
           | 'singing' | 'crying' | 'hugging' | 'drinking' | 'sitting' | 'barking'
           | 'focusing' | 'standing'
          ;

NEWLINE : [\r\n]+ ;
WS : [ \r\n\t] + -> channel(HIDDEN);