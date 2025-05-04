grammar Geralt;

program: statement+ ;

statement
    : functionDecl                     # functionDecleration
    | functionCall                     # functionCallStatement
    | 'let' type ID ('[' INT ']')?     # declaration
    | 'set' ID ('[' INT ']')? '=' expr # assign
    | 'input' ID ('[' INT ']')?        # input
    | 'print' expr                     # output
    | 'print' booleanExpr              # outputBool
    | 'return' expr                    # returnStatement
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

functionDecl
    : 'zaklęcie' type ID '(' parameters? ')' ':' block 'koniec'
    ;

parameters
    : parameter (',' parameter)*
    ;

parameter
    : type ID
    ;

functionCall
    : ID '(' arguments? ')'
    ;

arguments
    : expr (',' expr)*
    ;

type
    : 'Wilk'
    | 'Kot'
    | 'Gryf'
    ;

ID: [a-zA-Z_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ][a-zA-Z0-9_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
COMMENT: 'Komentarz' ~[\r\n]* -> skip ;
WHITE_SPACE: [ \t\r\n]+ -> skip ;
LBRACK: '[' ;
RBRACK: ']' ;