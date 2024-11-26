import ply.lex as lex

# Dicionário de palavras reservadas
reserved = {
    'FACA': 'FACA',
    'SER': 'SER',
    'MOSTRE': 'MOSTRE',
    'SOME': 'SOME',
    'COM': 'COM',
    'REPITA': 'REPITA',
    'VEZES': 'VEZES',
    'FIM': 'FIM',
    'SE': 'SE',
    'ENTAO': 'ENTAO',
    'SENAO': 'SENAO',
    'MULTIPLIQUE': 'MULTIPLIQUE',
    'POR': 'POR',
}

# Lista de tokens
tokens = [
    'VAR', 'NUM', 'PONTO', 'DOIS_PONTOS'
] + list(reserved.values())

# Definição de tokens específicos
t_PONTO = r'\.'
t_DOIS_PONTOS = r':'

# Definição de números
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificar palavras reservadas ou variáveis
def t_VAR(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value, 'VAR')  # Verifica palavras reservadas primeiro
    return t

# Ignorar espaços e quebras de linha
t_ignore = ' \t\n'

# Tratamento de erros léxicos
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Exportar o lexer
__all__ = ['lexer', 'tokens']