from lexer import lexer
from parser import parser

# Programa de entrada
codigo_matemagica = """
FACA num SER 0.
SE num ENTAO
MOSTRE num .
SENAO
MOSTRE 10.
FIM
"""

# Etapa 1: Análise léxica
print("Tokens:")
lexer.input(codigo_matemagica)
for token in lexer:
    print(token)

# Etapa 2: Análise sintática e geração de código
print("\nCódigo Python Gerado:")
resultado = parser.parse(codigo_matemagica)
print(resultado)
