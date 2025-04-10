grammar Geralt;

program: statement+ ;

statement
    : 'let' type ID         # declaration
    | 'set' ID '=' expr     # assign
    | 'input' ID            # input
    | 'print' expr          # output
    | 'print' booleanExpr   # outputBool
    ;

expr
    : expr 'Igni' expr      # subtraction
    | expr 'Aard' expr      # addition
    | expr 'Quen' expr      # multiplication
    | expr 'Yrden' expr     # dividing
    | INT                   # int
    | FLOAT                 # float
    | ID                    # var
    | '(' expr ')'          # parenthesis
    ;

booleanExpr
    : booleanExpr 'AND' booleanExpr     # and
    | booleanExpr 'OR' booleanExpr      # or
    | booleanExpr 'XOR' booleanExpr     # xor
    | 'NEG' booleanExpr                 # neg
    | 'true'                            # true
    | 'false'                           # false
    | ID                                # boolvar
    ;


type: 'Wilk' | 'Kot' ;

ID: [a-zA-Z_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ][a-zA-Z0-9_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
COMMENT: 'Komentarz' ~[\r\n]* -> skip ;
WHITE_SPACE: [ \t\r\n]+ -> skip ;