%{
#include "matemagica.tab.h"
%}

%%
"FACA"              { return FACA; }
"SER"               { return SER; }
"MOSTRE"            { return MOSTRE; }
"SOME"              { return SOME; }
"COM"               { return COM; }
"REPITA"            { return REPITA; }
"VEZES"             { return VEZES; }
"FIM"               { return FIM; }
"SE"                { return SE; }
"ENTAO"             { return ENTAO; }
"SENAO"             { return SENAO; }
"MULTIPLIQUE"       { return MULTIPLIQUE; }
"POR"               { return POR; }
[0-9]+              { yylval.ival = atoi(yytext); return NUM; }
[a-zA-Z]+           { yylval.sval = strdup(yytext); return VAR; }
[ \t\n]+            { /* Ignorar espaços e quebras de linha */ }
"."                 { return '.'; }
":"                 { return ':'; }
%%

int yywrap() {
    return 1;
}
