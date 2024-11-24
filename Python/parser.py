import ply.yacc as yacc
from lexer import tokens

# Regras de precedência (não é essencial aqui, mas pode ajudar com extensões)
precedence = ()

# Gramática
def p_programa(p):
    'programa : cmds'
    # Adiciona a estrutura básica de um programa em C
    cmds = '\n'.join(p[1])
    p[0] = f"#include <stdio.h>\n\nint main() {{\n{cmds}\n    return 0;\n}}"

def p_cmds(p):
    '''cmds : cmd cmds
            | cmd'''
    p[0] = [p[1]] + (p[2] if len(p) > 2 else [])

def p_cmd(p):
    '''cmd : atribuicao
           | impressao
           | operacao
           | repeticao'''
    p[0] = p[1]

def p_atribuicao(p):
    'atribuicao : FACA VAR SER NUM PONTO'
    p[0] = f"    int {p[2]} = {p[4]};"

def p_impressao(p):
    '''impressao : MOSTRE VAR PONTO
                 | MOSTRE operacao PONTO'''
    p[0] = f"    printf(\"%d\\n\", {p[2]});"

def p_operacao(p):
    '''operacao : SOME VAR COM VAR PONTO
                | SOME VAR COM NUM PONTO
                | SOME NUM COM VAR PONTO
                | SOME NUM COM NUM PONTO'''
    p[0] = f"    {p[2]} += {p[4]};"

def p_multiplique(p):
    '''cmd : MULTIPLIQUE VAR POR VAR PONTO
           | MULTIPLIQUE VAR POR NUM PONTO
           | MULTIPLIQUE NUM POR VAR PONTO
           | MULTIPLIQUE NUM POR NUM PONTO'''
    p[0] = f"    {p[2]} *= {p[4]};"


def p_repeticao(p):
    'repeticao : REPITA NUM VEZES DOIS_PONTOS cmds FIM'
    cmds = '\n'.join(p[5])
    p[0] = f"    for (int _ = 0; _ < {p[2]}; _++) {{\n{cmds}\n    }}"


def p_se_entao(p):
    '''cmd : SE VAR ENTAO cmds FIM
           | SE VAR ENTAO cmds FIM PONTO'''
    if len(p) == 6:  # SE VAR ENTAO cmds FIM
        cmds = '\n    '.join(p[4])
        p[0] = f"    if ({p[2]}) {{\n    {cmds}\n    }}"
    else:  # SE VAR ENTAO cmds FIM .
        cmds = '\n    '.join(p[4])
        p[0] = f"    if ({p[2]}) {{\n    {cmds}\n    }}"


def p_se_entao_ponto(p):
    '''cmd : SE VAR ENTAO cmd FIM PONTO
           | SE VAR ENTAO cmd SENAO cmd FIM PONTO'''
    if len(p) == 7:  # SE VAR ENTAO cmd FIM .
        p[0] = f"    if ({p[2]}) {{\n        {p[4]}\n    }}"
    else:  # SE VAR ENTAO cmd SENAO cmd FIM .
        p[0] = f"    if ({p[2]}) {{\n        {p[4]}\n    }} else {{\n        {p[6]}\n    }}"


def p_se_entao_senao(p):
    '''cmd : SE VAR ENTAO cmds SENAO cmds FIM
           | SE VAR ENTAO cmds SENAO cmds FIM PONTO'''
    if len(p) == 8:  # SE VAR ENTAO cmds SENAO cmds FIM
        cmds_entao = '\n    '.join(p[4])
        cmds_senao = '\n    '.join(p[6])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }} else {{\n    {cmds_senao}\n    }}"
    else:  # SE VAR ENTAO cmds SENAO cmds FIM .
        cmds_entao = '\n    '.join(p[4])
        cmds_senao = '\n    '.join(p[6])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }} else {{\n    {cmds_senao}\n    }}"


def p_error(p):
    print("Erro de sintaxe!")

# Construir o parser
parser = yacc.yacc(debug=True)
