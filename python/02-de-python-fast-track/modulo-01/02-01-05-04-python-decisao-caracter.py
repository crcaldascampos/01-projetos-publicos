
# Link da lista de exercícios:  https://wiki.python.org.br/EstruturaDeDecisao

# 05.04. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
# obs: parte extra => 
    # 04.01. adicione a verificação para classificar os número
    # 04.02. adicione a verificação para classificar os símbolos
# Definição de DICIONÁRIOS, LISTAS, TUPLAS E VARIÁVEIS
vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numero_string = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolo = [
    "'", '"', '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '=', '+'
    , '´', '`', '[', ']', '{', '}', '~', '^', 'ª', 'º', '/', '?', ';', ':', '.'
    , '>', ',', '<', '|'
]
# Entrada de dados
caracter = input('Digite um caracter: ')
# Verificação da entrada de dados se está dentro da lista
if (caracter in vogal):  # Verificar e ajustar a comparação. Add FOR ?
    print(f'O caracter digitado ( {caracter} ) é uma VOGAL!')
elif (caracter in numero) or (caracter in numero_string):
    print(f'O caracter digitado ( {caracter} ) é um NÚMERO!')
elif (caracter in simbolo):
    print(f'O caracter digitado ( {caracter} ) é um SIMBOLO!')
else:
    print(f'O caracter digitado ( {caracter} ) é uma CONSOANTE!')
