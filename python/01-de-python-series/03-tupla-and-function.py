# --------------------------------------------------
# TUPLA
# --------------------------------------------------
pessoa = ('Carlinhos', 40)
ano = 2023
# print(pessoa)
# print(type(pessoa[0]), type(pessoa[1]), type(ano))


# --------------------------------------------------
# ADICIONANDO UMA LISTA NA VERIFICAÇÃO DE TIPAGEM
# --------------------------------------------------
numeros = [1, 2, 3, '4']


# --------------------------------------------------
# 01-   CRIANDO UMA FUNÇÃO
# --------------------------------------------------
# obs: esse ponto deixa o código mais limpo e de fácil entendimento
# --------------------------------------------------
def descrever_variavel(variavel):
    print(variavel)
    print(type(variavel))
    # --------------------------------------------------
    # SE FOR UMA TUPLA APRESENTA OS DADOS E DEPOIS SEUS RESPECTIVOS TIPOS
    # --------------------------------------------------
    if type(variavel)   ==  tuple:
        print('É uma tupla!')
        print() # quebrando / saltando 1 linha

        for value in variavel:
            # abaixo usamos a mesma função para exibir a tipagem da tupla e a tipagem dos registros
            # da tupla, chamamos isso de recursividade
            descrever_variavel(value)

    print() # quebrando / saltando 1 linha

# --------------------------------------------------
# USANDO A FUNÇÃO CRIADA
# --------------------------------------------------
# obs: executa todo o código em cima dos parâmetros passados
# --------------------------------------------------
descrever_variavel(pessoa)
descrever_variavel(ano)

print('=' * 100) 
print('-' * 100) 
print('=' * 100)
print()






# --------------------------------------------------
# 02-   CRIANDO OUTRA FUNÇÃO
# --------------------------------------------------
# obs: aqui teremos a execução da função acima e a inclusão da listagem números
# --------------------------------------------------
def descrever_variavel_acrescentando_lista(variavel_e_lista):
    print(variavel_e_lista)
    print(type(variavel_e_lista))
    print() # quebrando / saltando 1 linha

    if type(variavel_e_lista) == tuple  or type(variavel_e_lista) == list:
        print() # quebrando / saltando 1 linha

        for value_com_lista in variavel_e_lista:
            descrever_variavel_acrescentando_lista(value_com_lista)
    
    return  (variavel_e_lista, type(variavel_e_lista))
    print() # quebrando / saltando 1 linha



descrever_variavel_acrescentando_lista(pessoa)
descrever_variavel_acrescentando_lista(ano)
descrever_variavel_acrescentando_lista(numeros)


print()
print('=' * 100) 
print('-' * 100) 
print('=' * 100)
print()


retorno = descrever_variavel_acrescentando_lista(ano)
print(retorno)
print(type(retorno))