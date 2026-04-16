grammar CRUD;

prog: stmt+ ;

stmt
    : create
    | read
    | update
    | delete
    ;

create
    : 'CREATE' ID object
    ;

read
    : 'READ' ID where_clause?
    ;

update
    : 'UPDATE' ID 'SET' assignments where_clause?
    ;

delete
    : 'DELETE' ID where_clause?
    ;

where_clause
    : 'WHERE' condition
    ;

condition
    : ID '=' value
    ;

assignments
    : assignment (',' assignment)*
    ;

assignment
    : ID '=' value
    ;

object
    : '{' pair (',' pair)* '}'
    ;

pair
    : ID ':' value
    ;

value
    : STRING
    | NUMBER
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ;
STRING: '"' .*? '"' ;

WS: [ \t\r\n]+ -> skip ;
