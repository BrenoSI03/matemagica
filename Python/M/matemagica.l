%{
#include "y.tab.h"
%}

%%
"FACA"          { return FACA; }
"SER"           { return SER; }
"NUM"           { return NUM; }
"MOSTRE"        { return MOSTRE; }
"SOME"          { return SOME; }
"COM"           { return COM; }
"REPITA"        { return REPITA; }
"VEZES"         { return VEZES; }
"FIM"           { return FIM; }
"SE"            { return SE; }
"ENTAO"         { return ENTAO; }
"SENAO"         { return SENAO; }
"MULTIPLIQUE"   { return MULTIPLIQUE; }
"POR"           { return POR; }
[0-9]+          { yylval.ival = atoi(yytext); return NUM; }
[a-zA-Z]+       { yylval.sval = strdup(yytext); return VAR; }
[ \t\n]+        { /* Ignore espaços em branco */ }
.               { printf("Token desconhecido: %s\n", yytext); }
%%

int yywrap() { return 1; }
