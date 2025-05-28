grammar Geralt;

program: (structDecl | classDecl | functionDecl | statement)+ ;

statement
    : 'let' type ID indexes            # arrayDeclaration
    | 'let' type ID                    # declaration
    | 'set' ID indexes '=' expr        # arrayAssign
    | 'set' ID '=' expr                # assign
    | 'input' ID indexes               # arrayInput
    | 'input' ID                       # input
    | 'print' expr                     # output
    | 'print' booleanExpr              # outputBool
    | 'return' expr?                   # returnStatement
    | jezeliBlock                      # ifStatement
    | dopokiBlock                      # whileStatement
    | 'set' structAccess '=' expr      # structAsign
    | 'print' structAccess             # structFieldPrint
    ;

expr
    : expr 'Igni' expr      # subtraction
    | expr 'Aard' expr      # addition
    | expr 'Quen' expr      # multiplication
    | expr 'Yrden' expr     # dividing
    | INT                   # int
    | FLOAT                 # float
    | ID indexes            # arrayAccess
    | ID                    # var
    | STRING                # string
    | functionCall          # functionCallNum
    | 'true'                # exprTrue
    | 'false'               # exprFalse
    | '(' expr ')'          # parenthesis
    | structAccess          # structAccessExpr
    ;

indexes
    : '[' expr (',' expr)* ']' 
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

classDecl
    : 'klasa' ID ':' classBody 'koniec'
    ;

classBody
    : classMember*
    ;

classMember
    : visibility type ID                      
    | functionDecl                            
    ;

visibility
    : 'publiczne'
    | 'prywatne'
    ;
    
structDecl
    : 'struktura' ID ':' structFields 'koniec'
    ;

structFields
    : (type ID)+
    ;

structAccess
    : ID '.' ID         # structFieldAccess
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
    | 'Niedźwiedź'
    | 'Mantikora'
    | 'auto'
    | ID
    ;

ID: [a-zA-Z_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ][a-zA-Z0-9_ęóąśłżźćńĘÓĄŚŁŻŹĆŃ]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
COMMENT: 'Komentarz' ~[\r\n]* -> skip ;
WHITE_SPACE: [ \t\r\n]+ -> skip ;
STRING: '"' .*? '"';
