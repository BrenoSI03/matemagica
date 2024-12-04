from lexer import lexer
from parser import parser

# Programa de entrada
codigo_matemagica = \
"""
FACA n SER 10.
FACA m SER 5.
FACA p SER 0.
SE n ENTAO
MOSTRE n .
SE m ENTAO
MOSTRE m .
SENAO
MOSTRE 0 .
FIM
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
