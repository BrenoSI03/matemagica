import ply.yacc as yacc
from lexer import lexer  # Supondo que o lexer foi importado de lexer.py
from parser import parser  # Supondo que o parser foi importado de parser.py

def gerar_codigo_c(input_code):
    try:
        # Analisa o código de entrada com o parser
        result = parser.parse(input_code)
        
        # Cria o arquivo output.c e escreve o código gerado
        with open("Python/output.c", "w") as output_file:
            output_file.write(result)
        
        print("Arquivo output.c gerado com sucesso!")
    except Exception as e:
        # Caso ocorra algum erro, captura a exceção e exibe no terminal
        print(f"Erro ao gerar o arquivo output.c: {e}")

def ler_entrada():
    try:
        # Lê o conteúdo do arquivo input.txt
        with open("Python/input.txt", "r") as input_file:
            input_code = input_file.read()
        return input_code
    except FileNotFoundError:
        print("Arquivo input.txt não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo input.txt: {e}")
        return None

if __name__ == "__main__":
    input_code = ler_entrada()
    if input_code:
        gerar_codigo_c(input_code)
