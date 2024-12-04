import ply.yacc as yacc
from lexer import tokens

# Pilha para rastrear o nível de indentação
indent_stack = [1]  # Inicia no nível 1 dentro da função main

def get_indent():
    return '    ' * indent_stack[-1]  # 4 espaços por nível

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
    indent = get_indent()
    p[0] = f"{indent}int {p[2]} = {p[4]};"

def p_impressao(p):
    '''impressao : MOSTRE VAR PONTO
                 | MOSTRE operacao PONTO
                 | MOSTRE NUM PONTO'''
    indent = get_indent()
    p[0] = f"{indent}printf(\"%d\\n\", {p[2]});"

def p_operacao(p):
    '''operacao : SOME VAR COM VAR PONTO
                | SOME VAR COM NUM PONTO
                | SOME NUM COM VAR PONTO
                | SOME NUM COM NUM PONTO'''
    # Retorna a expressão para uso em impressao
    p[0] = f"{p[2]} + {p[4]}"

def p_multiplique(p):
    '''cmd : MULTIPLIQUE VAR POR VAR PONTO
           | MULTIPLIQUE VAR POR NUM PONTO
           | MULTIPLIQUE NUM POR VAR PONTO
           | MULTIPLIQUE NUM POR NUM PONTO'''
    indent = get_indent()
    p[0] = f"{indent}{p[2]} *= {p[4]};"

def p_repeticao(p):
    'repeticao : REPITA NUM VEZES DOIS_PONTOS cmds FIM'
    indent = get_indent()
    loop_start = f"{indent}for (int i = 0; i < {p[2]}; i++) {{"
    
    indent_stack.append(indent_stack[-1] + 1)  # Incrementa para o bloco interno
    cmds = '\n'.join(p[5])
    indent_stack.pop()  # Decrementa após o bloco
    
    loop_end = f"{indent}}}"
    p[0] = f"{loop_start}\n{cmds}\n{loop_end}"

def p_expressao(p):
    '''expressao : VAR
                | NUM'''
    p[0] = p[1]

def p_se(p):
    '''se : SE expressao ENTAO cmds FIM
          | SE expressao ENTAO cmds SENAO cmds FIM
          | SE expressao ENTAO cmds FIM PONTO
          | SE expressao ENTAO cmds SENAO cmds FIM PONTO'''
    indent = get_indent()
    
    if len(p) in [6, 7] and p.slice[-1].type != 'SENAO':
        # Forma sem SENAO
        code = f"{indent}if ({p[2]}) {{\n"
        indent_stack.append(indent_stack[-1] + 1)  # Incrementa o nível de indentação
        cmds_entao = '\n'.join(p[4])
        code += f"{cmds_entao}\n"
        indent_stack.pop()  # Decrementa o nível de indentação
        code += f"{indent}}}"
        if len(p) == 7 and p.slice[-1].type == 'PONTO':
            code += "."
    elif 'SENAO' in p:
        # Forma com SENAO
        code = f"{indent}if ({p[2]}) {{\n"
        indent_stack.append(indent_stack[-1] + 1)  # Incrementa o nível de indentação
        cmds_entao = '\n'.join(p[4])
        code += f"{cmds_entao}\n"
        indent_stack.pop()  # Decrementa o nível de indentação
        code += f"{indent}}} else {{\n"
        indent_stack.append(indent_stack[-1] + 1)  # Incrementa o nível de indentação
        cmds_senao = '\n'.join(p[6])
        code += f"{cmds_senao}\n"
        indent_stack.pop()  # Decrementa o nível de indentação
        code += f"{indent}}}"
        if len(p) == 8 and p.slice[-1].type == 'PONTO':
            code += "."
    else:
        # Produções não cobertas
        code = ""
    
    p[0] = code

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")

# Construir o parser
parser = yacc.yacc(debug=True)
