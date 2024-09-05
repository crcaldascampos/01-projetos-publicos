# --------------------------------------------------------------------------------------------------
# OBSERVAÇÕES SOBRE A LISTA
# --------------------------------------------------------------------------------------------------

# Lista é composta por 3 blocos:
    # VALORES:  são os dados armazenados nela efetivamente
    # ÍNDICE
        # POSITIVO
            # Utilizado para pegar o PRIMEIRP valor da lista, sendo referenciado pelo valor [0]
        # NEGATIVO
            # Utilizado para pegar o ÚLTIMO valor da lista, sendo referenciado pelo valor [-1]

    # Exemplo:
        #-----------------------------------------                x             #-----------------------------------------
        #      P   O   S   I   T   I   V   O                      x             #      N   E   G   A   T   I   V   O
        #-----------------------------------------                x             #-----------------------------------------
                # nome_lista[0]  =>  "João"                       x                     # nome_lista[-5]  =>  "João"
                # nome_lista[1]  =>  "Ana"                        x                     # nome_lista[-4]  =>  "Ana"
                # nome_lista[2]  =>  "Paulo"                      x                     # nome_lista[-3]  =>  "Paulo"
                # nome_lista[3]  =>  "Matheus"                    x                     # nome_lista[-2]  =>  "Matheus"
                # nome_lista[4]  =>  "Nasser"                     x                     # nome_lista[-1]  =>  "Nasser"

    # FATIAR / SLICE uma lista:
        # nome_lista[1:]        =>    ['Ana', 'Paulo', 'Matheus', 'Nasser']
        # nome_lista[:3]        =>    ['João', 'Ana', 'Paulo']
        # nome_lista[1:3]       =>    ['Ana', 'Paulo']
        # nome_lista[:]         =>    ['João', 'Ana', 'Paulo', 'Matheus', 'Nasser']
        # nome_lista[::-1]      =>    ['Nasser', 'Matheus', 'Paulo', 'Ana', 'João']   # inverte a ordem da lista
        # nome_lista[::2]       =>    ['João', 'Paulo', 'Nasser']                     # inicia a lista normalmente e salta de 2 em 2

    # obs_01: ao fatiar / slice uma lista, o tipo de saída também será uma lista, quando contiver mais de um retorno / valor.
    # obs_02: para saber quantos itens temos em uma lista, basta passar a função len na lista.
        # len(lista)
    
    # obs_03: ao efetuar o slice / fatiar uma lista, a referência final não importa se está ou não no range, se estiver com uma
        # quantidade maior que a contida na lista ele simplesmente ignorará, não gerando erro na aplicação.

#################################
# Início do HANDS-ON aos 07min  #
#################################

print()
lista = ['joao', 'ana', 'paulo', 'matheus', 'nasser']
print(lista)
print()

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print()

print(lista[-5])
print(lista[-4])
print(lista[-3])
print(lista[-2])
print(lista[-1])
print()

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
print()

# identifica quantos itens temos na lista
print(f'''Essa lista possui {len(lista)} itens!''')
print()

# Efetuando o slice na lista
print(lista[1:])    # pega do segundo registro e traz todos os registros
print(lista[:3])    # pega do primeiro registro, posição 0 da lista até a posição 2 da lista
print(lista[1:3])   # pega do segundo registro, posição 1 da lista até a posição 2 da lista
print(lista)        # traz a lista completa
print(lista[:])     # traz a lista completa
print(lista[::-1])  # traz a lista completa na ordem inversa
print(lista[::2])   # traz os valores da lista pulando de 2 em 2, observando desde o primeiro registro
print(lista[1::2])  # pula o primeiro registro e traz os registros de 2 em 2
print(lista[1::3])  # pula o primeiro registro e traz os registros de 3 em 3
print(lista[2::4])  # pula os 2 primeiros registros e traz os registros de 4 em 4
print()
