from lexer import lexer
from parser import parser

# Programa de entrada
codigo_matemagica = \
"""
FACA a SER 10.
FACA b SER 20.
FACA c SER 0.
SE a < b ENTAO
    MOSTRE a .
    SE b >= 15 ENTAO
        MOSTRE b .
    SENAO
        MOSTRE c .
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
