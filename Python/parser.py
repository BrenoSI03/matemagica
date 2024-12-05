import ply.yacc as yacc
from lexer import tokens

# Regras de precedência
precedence = (
    ('left', 'EQ', 'NEQ'),          # Igualdade e desigualdade
    ('left', 'GTE', 'LTE', 'GT', 'LT'),  # Comparações
    # Adicione precedência para outros operadores, se necessário
)

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
           | multiplique
           | divisao
           | subtracao
           | se
           | repeticao_enquanto'''  # Adicione esta linha
    p[0] = p[1]

def p_atribuicao(p):
    '''atribuicao : FACA VAR SER NUM PONTO
                  | FACA VAR SER VAR PONTO
                  | FACA VAR SER expressao PONTO'''  # Adicione esta linha
    if len(p) == 6:
        # Atribuição com número ou variável
        p[0] = f"    {p[2]} = {p[4]};"
    else:
        # Atribuição com expressão
        p[0] = f"    {p[2]} = {p[4]};"

def p_impressao(p):
    '''impressao : MOSTRE VAR PONTO
                 | MOSTRE NUM PONTO'''
    p[0] = f"    printf(\"%d\\n\", {p[2]});"

def p_operacao(p):
    '''operacao : SOME VAR COM VAR PONTO
                | SOME VAR COM NUM PONTO'''
    p[0] = f"    {p[2]} += {p[4]};"

def p_multiplique(p):
    '''multiplique : MULTIPLIQUE VAR POR VAR PONTO
           | MULTIPLIQUE VAR POR NUM PONTO'''
    p[0] = f"    {p[2]} *= {p[4]};"

def p_divisao(p):
    '''divisao : DIVIDA VAR POR NUM PONTO
           | DIVIDA VAR POR VAR PONTO'''
    p[0] = f"    {p[2]} /= {p[4]};"

def p_subtracao(p):
    '''subtracao : SUBTRAIA VAR POR NUM PONTO
           | SUBTRAIA VAR POR VAR PONTO'''
    p[0] = f"    {p[2]} -= {p[4]};"

def p_repeticao(p):
    'repeticao : REPITA NUM VEZES DOIS_PONTOS cmds FIM'
    cmds = '\n    '.join(p[6])
    p[0] = f"    for (int i = 0; i < {p[2]}; i++) {{\n    {cmds}\n    }}"

def p_repeticao_enquanto(p):
    'repeticao_enquanto : REPITA ENQUANTO expressao DOIS_PONTOS cmds FIM'
    cmds = '\n    '.join(p[5])
    p[0] = f"    while ({p[3]}) {{\n    {cmds}\n    }}"

def p_expressao_binaria(p):
    '''expressao : expressao EQ expressao
                | expressao NEQ expressao
                | expressao GTE expressao
                | expressao LTE expressao
                | expressao GT expressao
                | expressao LT expressao'''
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_expressao_basica(p):
    '''expressao : VAR
                | NUM'''
    p[0] = str(p[1])

def p_se(p):
    '''se : SE expressao ENTAO cmds FIM
          | SE expressao ENTAO cmds SENAO cmds FIM
          | SE expressao ENTAO cmds FIM PONTO
          | SE expressao ENTAO cmds SENAO cmds FIM PONTO'''
    
    # Determinar se a cláusula SENAO está presente
    if len(p) == 6 or (len(p) == 7 and p.slice[-1].type != 'SENAO'):
        # Forma sem SENAO
        cmds_entao = '\n    '.join(p[4])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }}"
        if len(p) == 7 and p.slice[-1].type == 'PONTO':
            p[0] += "."
    else:
        # Forma com SENAO
        cmds_entao = '\n    '.join(p[4])
        cmds_senao = '\n    '.join(p[6])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }} else {{\n    {cmds_senao}\n    }}"
        if len(p) == 8 and p.slice[-1].type == 'PONTO':
            p[0] += "."

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")

# Construir o parser
parser = yacc.yacc(debug=True)
