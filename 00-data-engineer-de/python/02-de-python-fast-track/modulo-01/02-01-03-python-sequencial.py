#   Faremos a lista de exercícios da própria página do python, com o link abaixo:
    #   wiki.python.org.br/ListaDeExercicios

# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela. 
print('Alô mundo')

# =====================================================================================================

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 
numero =  input('Digite um número: ')
# Para que a saída exiba o valor da vaiável dentro da própria mensagem, passamos o f colado à mensagem
# e no ponto em que devemos exibir o valor da variável, passamos a variável dentro das chaves { }
print(f'O número informado foi {numero}')

# =====================================================================================================

# 3. Faça um Programa que peça dois números e imprima a soma.
numero01 = float(input('Digite o 1º número: '))
numero02 = float(input('Digite o 2º número: '))
soma01 = numero01 + numero02
# Para definir a formatação da qtd das casas decimais do número formatado em float
# devemos passar os : dentro das chaves { } colado à variável, por exemplo: {variavel:3}
# dessa forma o valor final da variável será exibido com até 3 casas decimais.
print(f'O 1º número foi {numero01}, o 2º número foi {numero02} e a soma é {soma01:2}')


