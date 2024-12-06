import ply.yacc as yacc
from lexer import tokens

# Precedência (opcional, se desejar)
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

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
           | repeticao
           | se
           | multiplique
           | divisao
           | subtracao
           '''
    # Aqui você pode manter outras regras se necessário,
    # mas removendo a antiga `operacao` se não for mais usar.
    p[0] = p[1]

def p_atribuicao(p):
    '''atribuicao : FACA VAR SER NUM PONTO
                  | FACA VAR SER VAR PONTO
                  | FACA VAR SER expressao_arit PONTO'''
    p[0] = f"    {p[2]} = {p[4]};"

def p_impressao(p):
    '''impressao : MOSTRE expressao_arit PONTO'''
    # Agora, p[2] pode ser algo como (2 + a), (a * 3), etc.
    p[0] = f"    printf(\"%d\\n\", {p[2]});"

def p_repeticao(p):
    'repeticao : REPITA NUM VEZES DOIS_PONTOS cmds FIM'
    cmds = '\n    '.join(p[5])
    p[0] = f"    for (int i = 0; i < {p[2]}; i++) {{\n    {cmds}\n    }}"

def p_se(p):
    '''se : SE expressao_arit ENTAO cmds FIM
          | SE expressao_arit ENTAO cmds SENAO cmds FIM'''
    if len(p) == 6:
        cmds_entao = '\n    '.join(p[4])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }}"
    else:
        cmds_entao = '\n    '.join(p[4])
        cmds_senao = '\n    '.join(p[6])
        p[0] = f"    if ({p[2]}) {{\n    {cmds_entao}\n    }} else {{\n    {cmds_senao}\n    }}"

# Caso tenha operações específicas de MULTIPLIQUE, DIVIDA, SUBTRAIA (como antes), mantenha, 
# caso contrário, remova se não forem mais necessárias.
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

# Regra para expressões aritméticas genéricas
def p_expressao_arit_binaria(p):
    '''expressao_arit : expressao_arit PLUS expressao_arit
                      | expressao_arit MINUS expressao_arit
                      | expressao_arit TIMES expressao_arit
                      | expressao_arit DIVIDE expressao_arit'''
    # Constrói a expressão em C
    p[0] = f"({p[1]} {p[2]} {p[3]})"

def p_expressao_arit_basica(p):
    '''expressao_arit : NUM
                      | VAR'''
    p[0] = str(p[1])

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")

parser = yacc.yacc(debug=True)
