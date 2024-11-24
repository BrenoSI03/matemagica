%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*#define YYDEBUG 1
int yydebug = 1;*/


void yyerror(const char *s);
int yylex();
FILE *output;
%}

%union {
    int ival;
    char *sval;
}

%token FACA SER MOSTRE SOME COM REPITA VEZES FIM SE ENTAO SENAO MULTIPLIQUE POR
%token <ival> NUM
%token <sval> VAR
%type <sval> var
%type <ival> num
%%

programa:
    cmds { fprintf(output, "# Programa convertido de Matemágica para Python\n"); }
    ;

cmds:
    cmd cmds
    | cmd
    ;

cmd:
    atribuicao
    | repeticao
    | selecao
    | operacao
    | multiplicacao
    | impressao
    ;


atribuicao:
    FACA var SER num '.' { fprintf(output, "%s = %d\n", $2, $4); }
    ;

impressao:
    MOSTRE var '.' { fprintf(output, "print(%s)\n", $2); }
    | MOSTRE operacao '.' { /* A operação já gera código Python diretamente. */ }
    ;

operacao:
    SOME var COM var '.' { fprintf(output, "%s += %s\n", $2, $4); }
    | SOME var COM num '.' { fprintf(output, "%s += %d\n", $2, $4); }
    | SOME num COM num '.' { fprintf(output, "temp = %d + %d\nprint(temp)\n", $2, $4); }
    ;

repeticao:
    REPITA num VEZES ':' cmds FIM { 
        fprintf(output, "for _ in range(%d):\n", $2);
    }
    ;


selecao:
    SE var ENTAO cmds FIM { 
        fprintf(output, "if %s:\n", $2);
        // Processar cmds dentro do bloco "if".
    }
    | SE num ENTAO cmds FIM { 
        fprintf(output, "if %d:\n", $2);
        // Processar cmds dentro do bloco "if".
    }
    | SE var ENTAO cmds SENAO cmds FIM {
        fprintf(output, "if %s:\n", $2);
        // Processar cmds dentro do bloco "if".
        fprintf(output, "else:\n");
        // Processar cmds dentro do bloco "else".
    }
    | SE num ENTAO cmds SENAO cmds FIM {
        fprintf(output, "if %d:\n", $2);
        // Processar cmds dentro do bloco "if".
        fprintf(output, "else:\n");
        // Processar cmds dentro do bloco "else".
    }
    ;


multiplicacao:
    MULTIPLIQUE var POR var '.' { fprintf(output, "%s *= %s\n", $2, $4); }
    | MULTIPLIQUE var POR num '.' { fprintf(output, "%s *= %d\n", $2, $4); }
    | MULTIPLIQUE num POR num '.' { fprintf(output, "temp = %d * %d\nprint(temp)\n", $2, $4); }
    ;

var:
    VAR { $$ = $1; }
    ;

num:
    NUM { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Erro: %s\n", s);
}

int main() {
    output = fopen("output.py", "w");
    if (!output) {
        perror("Erro ao abrir arquivo de saída");
        return 1;
    }
    yyparse();
    fclose(output);
    return 0;
}
