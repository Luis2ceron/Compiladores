grammar MiGramatica;

program: statement* EOF;

statement
    : forStatement
    | assignmentStatement
    | expression
    ;

forStatement
    : 'for' '(' forControl ')' statement
    ;

forControl
    : forInit? ';' expression? ';' forUpdate?
    ;

forInit
    : ID '=' expression
    ;

forUpdate
    : ID '=' expression
    ;

assignmentStatement
    : ID '=' expression
    ;

expression
    : ID                            # IdentifierExpr
    | NUMBER                        # NumberExpr
    | expression MULT expression    # MultiplicationExpr
    | expression PLUS expression    # AdditionExpr
    | expression LT expression      # LessThanExpr
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;

MULT: '*';
PLUS: '+';
LT: '<';

WS: [ \t\r\n]+ -> skip;