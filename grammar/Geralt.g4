grammar Geralt;

program: statement+ ;

statement
    : 'let' type ID ('[' INT ']')?     # declaration
    | 'set' ID ('[' INT ']')? '=' expr # assign
    | 'input' ID ('[' INT ']')?        # input
    | 'print' expr                     # output
    | 'print' booleanExpr              # outputBool
    | jezeliBlock                      # ifStatement
    | dopokiBlock                      # whileStatement
    ;

expr
    : expr 'Igni' expr      # subtraction
    | expr 'Aard' expr      # addition
    | expr 'Quen' expr      # multiplication
    | expr 'Yrden' expr     # dividing
    | INT                   # int
    | FLOAT                 # float
    | ID                    # var
    | 'true'                # exprTrue
    | 'false'               # exprFalse
    | '(' expr ')'          # parenthesis
    ;

booleanExpr
    : booleanExpr 'AND' booleanExpr     # and
    | booleanExpr 'OR' booleanExpr      # or
    | booleanExpr 'XOR' booleanExpr     # xor
    | 'NEG' booleanExpr                 # neg
    | comparisonExpr                    # compare
    | 'true'                            # true
    | 'false'                           # false
    | ID                                # boolvar
    ;

comparisonExpr
    : expr '<' expr     # lessThan
    | expr '<=' expr    # lessEqual
    | expr '>' expr     # greaterThan
    | expr '>=' expr    # greaterEqual
    | expr '==' expr    # equal
    | expr '!=' expr    # notEqual
    ;
    
jezeliBlock
    : 'jeżeli' booleanExpr ':' block
      ('w_przeciwnym_wypadku' ':' block)?
      'koniec'
    ;

dopokiBlock
    : 'dopóki' booleanExpr ':' block 'koniec'
    ;

block
    : statement+
    ;

type: 'Wilk' | 'Kot' | 'Gryf' ;

ID: [a-zA-Z_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ][a-zA-Z0-9_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
COMMENT: 'Komentarz' ~[\r\n]* -> skip ;
WHITE_SPACE: [ \t\r\n]+ -> skip ;
LBRACK: '[' ;
RBRACK: ']' ;