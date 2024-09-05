
# Link da lista de exercícios:  https://wiki.python.org.br/EstruturaDeRepeticao

# 06.06. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.


numero_lista_01 = []
numero_lista_02 = []

# Quando temos 1 limite, ponto de parada utilizamos o for
# A função reversed() inverte o valor da saída da lista passada entre parênteses.
for numero in reversed( range(1, 21)):     
    print(f'''
    {numero}
    ''')

    # Adicionando valores do for à lista.
    # 1ª forma de adicionar um valor a uma lista
    numero_lista_01.append(numero)

    # 2ª forma de adicionar um valor a uma lista. Ao passar a variável dentro do 
    # colchetes [variavel] ela entende como 1 acréscimo à lista, fazendo o mesmo papel
    # da função append(), ou seja, nome_lista.append(variavel_que_alimenta_a_lista)
    numero_lista_02 = numero_lista_02 + [numero]
    print( f''' 
        {numero_lista_01}
        {numero_lista_02}
          ''')
   