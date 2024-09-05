
# Link da lista de exercícios:  https://wiki.python.org.br/EstruturaDeRepeticao

# 06.01. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
# valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
print()
# lista_nota = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #Inicialmente  começamos com uma lista pré-definida, porém é muito manual
lista_nota = range (11) # O número 11 não entra na listagem. Com o range podemos definir valores de limite / parada.
nota01 = int(input('Digite uma nota entre 0 e 10: '))


while not (nota01 in lista_nota):
    print('VALOR INVÁLIDO !')   
    print()
    nota01 = int(input('Digite uma nota válida entre 0 e 10: '))
else:
    print(f'''
        VALOR VÁLIDO !
        A sua nota é {nota01} !
    ''')