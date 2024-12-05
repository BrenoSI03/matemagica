from lexer import lexer
from parser import parser

# Programa de entrada
codigo_matemagica = \
"""
FACA d SER 0.
REPITA ENQUANTO d < 100:
    MOSTRE d.
    FACA d SER 5.
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
