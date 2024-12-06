import ply.lex as lex

reserved = {
    'FACA': 'FACA',
    'SER': 'SER',
    'MOSTRE': 'MOSTRE',
    'REPITA': 'REPITA',
    'VEZES': 'VEZES',
    'FIM': 'FIM',
    'SE': 'SE',
    'ENTAO': 'ENTAO',
    'SENAO': 'SENAO',
    'MULTIPLIQUE': 'MULTIPLIQUE',
    'POR': 'POR',
    'DIVIDA': 'DIVIDA',
    'SUBTRAIA': 'SUBTRAIA',
    'ENQUANTO': 'ENQUANTO'
}

tokens = [
    'VAR', 'NUM', 'PONTO', 'DOIS_PONTOS',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE'
] + list(reserved.values())

t_PONTO = r'\.'
t_DOIS_PONTOS = r':'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value, 'VAR')
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
