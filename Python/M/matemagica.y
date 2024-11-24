%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
int yylex();
FILE *output;

%}

%union {
    int ival;
    char *sval;
}

%token FACA SER NUM MOSTRE SOME COM REPITA VEZES FIM SE ENTAO SENAO MULTIPLIQUE POR
%type <sval> var
%type <ival> num

%%

programa:
    cmds { fprintf(output, "# Programa convertido\n"); }
    ;

cmds:
    cmd cmds
    | cmd
    ;

cmd:
    atribuicao
    | impressao
    | operacao
    | repeticao
    | selecao
    | multiplicacao
    ;

atribuicao:
    FACA var SER num '.' { fprintf(output, "%s = %d\n", $2, $4); }
    ;

impressao:
    MOSTRE var '.' { fprintf(output, "print(%s)\n", $2); }
    | MOSTRE operacao '.' { /* A operação já gera código */ }
    ;

operacao:
    SOME var COM var '.' { fprintf(output, "%s += %s\n", $2, $4); }
    | SOME var COM num '.' { fprintf(output, "%s += %d\n", $2, $4); }
    ;

repeticao:
    REPITA num VEZES ':' cmds FIM { 
        fprintf(output, "for _ in range(%d):\n", $2); 
    }
    ;

selecao:
    SE num ENTAO cmds FIM { 
        fprintf(output, "if %d:\n", $2); 
    }
    | SE num ENTAO cmds SENAO cmds FIM {
        fprintf(output, "if %d:\n", $2);
    }
    ;

multiplicacao:
    MULTIPLIQUE var POR var '.' { fprintf(output, "%s *= %s\n", $2, $4); }
    | MULTIPLIQUE var POR num '.' { fprintf(output, "%s *= %d\n", $2, $4); }
    ;

var:
    /* Identifique variáveis alfanuméricas no Flex */
    ;

num:
    NUM
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Erro: %s\n", s);
}

int main() {
    output = fopen("output.py", "w");
    if (!output) {
        perror("Não foi possível criar o arquivo de saída");
        return 1;
    }
    yyparse();
    fclose(output);
    return 0;
}
