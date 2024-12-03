import ply.yacc as yacc
from lexer import tokens

# Regras de precedência (não é essencial aqui, mas pode ajudar com extensões)
precedence = ()

# Gramática
def p_programa(p):
    'programa : cmds'
    cmds = '\n'.join(p[1])
    p[0] = f"#include <stdio.h>\n\nint main() {{\n{cmds}\n    return 0;\n}}"

def p_cmds(p):
    '''cmds : cmd cmds
            | cmd'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_cmd(p):
    '''cmd : atribuicao
           | impressao
           | operacao
           | repeticao
           | se'''
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
    p[0] = f"{p[2]} + {p[4]}"  # Retorna a expressão para uso em impressao

def p_multiplique(p):
    '''cmd : MULTIPLIQUE VAR POR VAR PONTO
           | MULTIPLIQUE VAR POR NUM PONTO
           | MULTIPLIQUE NUM POR VAR PONTO
           | MULTIPLIQUE NUM POR NUM PONTO'''
    p[0] = f"    {p[2]} *= {p[4]};"

def p_repeticao(p):
    'repeticao : REPITA NUM VEZES DOIS_PONTOS cmds FIM'
    cmds = '\n    '.join(p[6])
    p[0] = f"    for (int i = 0; i < {p[2]}; i++) {{\n    {cmds}\n    }}"

def p_se(p):
    '''se : SE VAR ENTAO cmds FIM
          | SE VAR ENTAO cmds FIM PONTO
          | SE NUM ENTAO cmds FIM
          | SE NUM ENTAO cmds FIM PONTO
          | SE VAR ENTAO cmds SENAO cmds FIM
          | SE VAR ENTAO cmds SENAO cmds FIM PONTO
          | SE NUM ENTAO cmds SENAO cmds FIM
          | SE NUM ENTAO cmds SENAO cmds FIM PONTO'''
    
    # Verifica se há uma cláusula SENAO
    if 'SENAO' in p.slice:
        cmds_entao = '\n    '.join(p[4])
        cmds_senao = '\n    '.join(p[6])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }} else {{\n    {cmds_senao}\n    }}"
    else:
        cmds = '\n    '.join(p[4])
        p[0] = f"    if ({p[2]}) {{\n    {cmds}\n    }}"

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")

# Construir o parser
parser = yacc.yacc(debug=True)
