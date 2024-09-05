
# Link da lista de exercícios:  https://wiki.python.org.br/EstruturaDeDecisao
#  05.01. Estrutura de decisão
#   05.01.01. se ..................... if: ... elif: ... else:


# 05.01. Faça um Programa que peça dois números e imprima o maior deles. 
n1 = float(input( '1º Número: '))   # Convertendo o valor da variável para float
n2 = float(input( '2º Número: '))   # Convertendo o valor da variável para float

# Contexto é iniciado por 2 pontos. A linha de baixo só é executada dependendo do
# resultado do contexto. O resultado é dado pela identação
if n1 >= n2:    # Contexto
    print(f'O maior número é {n1}')
else:           # Senão
    print(f'O maior número é {n2}')

