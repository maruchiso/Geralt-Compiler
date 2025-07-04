grammar Geralt;

program: (functionDecl | statement)+ ;

statement
    : 'let' type ID                    # declaration
    | 'set' ID  '=' expr               # assign
    | 'input' ID                       # input
    | 'print' expr                     # output
    | 'print' booleanExpr              # outputBool
    | 'return' expr?                   # returnStatement
    | jezeliBlock                      # ifStatement
    | dopokiBlock                      # whileStatement
    | tableDecl                        # tableDeclaration
    | tableAssign                      # tableAssignment
    | matrixDecl                       # matrixDeclaration
    | matrixAssign                     # matrixAssignment
    ;

matrixDecl
    : 'let' type '[' INT ']' '[' INT ']' ID
    ;

matrixAssign
    : 'set' ID '[' expr ']' '[' expr ']' '=' expr
    ;

tableDecl
    : 'let' type '[' INT ']' ID
    ;

tableAssign
    : 'set' ID '[' expr ']' '=' expr
    ;

expr
    : expr 'Igni' expr      # subtraction
    | expr 'Aard' expr      # addition
    | expr 'Quen' expr      # multiplication
    | expr 'Yrden' expr     # dividing
    | INT                   # int
    | FLOAT                 # float
    | ID                    # var
    | functionCall          # functionCallNum
    | 'true'                # exprTrue
    | 'false'               # exprFalse
    | '(' expr ')'          # parenthesis
    | ID '[' expr ']'       # arrayAccess
    | ID '[' expr ']' '[' expr ']'   # matrixAccess
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
    | functionCall                      # functionCallBool
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