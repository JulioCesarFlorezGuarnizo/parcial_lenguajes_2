%{
#include "calc.tab.h"
%}

%%

"true"     { return TRUE; }
"false"    { return FALSE; }
"and"      { return AND; }
"or"       { return OR; }
"not"      { return NOT; }

"("        { return '('; }
")"        { return ')'; }

[ \t]      ;
\n         { return '\n'; }

.          { return yytext[0]; }

%%
int yywrap() {
    return 1;
}