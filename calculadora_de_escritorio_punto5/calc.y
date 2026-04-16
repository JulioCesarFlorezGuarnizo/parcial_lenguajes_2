%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token TRUE FALSE AND OR NOT
%left OR
%left AND
%right NOT

%%

input:
    | input line
    ;

line:
    exp '\n' { printf("Resultado: %d\n", $1); }
    ;

exp:
      exp AND exp   { $$ = $1 && $3; }
    | exp OR exp    { $$ = $1 || $3; }
    | NOT exp       { $$ = !$2; }
    | '(' exp ')'   { $$ = $2; }
    | TRUE          { $$ = 1; }
    | FALSE         { $$ = 0; }
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Ingrese expresiones booleanas:\n");
    return yyparse();
}
