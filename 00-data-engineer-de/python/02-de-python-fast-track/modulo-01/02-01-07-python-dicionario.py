# --------------------------------------------------------------------------------------------------
# OBSERVAÇÕES SOBRE O DICIONÁRIO
# --------------------------------------------------------------------------------------------------

# Dicionário é composto por uma chave e um valor, conforme o exemplo abaixo.
# Para a criação de um dicionário escolhemos um nome para ele, que no caso abaixo é dicionario
# E para atribuir um valor a ele abrimos e fechamos chaves {  }

# Para pesquisar um valor dentro do dicionário passamos o nome dele e dentro dos colchetes
    # passamos o dado a ser buscado, por exemplo:
        # Se quisermos procurar a palavra verbete dentro do dicionário nomeado como dicionario,
            # devemos digitar o seguinte comando:
                # print(dicionario[verbete])
        # Assim passando a chave "verbete", será exibido o valor referente à "verbete"

# O comparativo entre 2 dicionários só retornará True se os 2 forem idênticos, se 1 chave ou
    # valor estiver fora da posição, então ele retornará False, por exemplo:
        # True =>   { 'a' : 0 } == { 'a' : 0 }
        # False =>  { 'a' : 0 } == { 'a' : 1 }

# Para identificarmos as palavras reservadas, funções internas, para o dicionário digitaremos:
    # dir(dict)

    # Para saber quantas chaves, verbetes, existem dentro do dicionário utilizamos ã função len
        # len(dicionario)

    # Pecorrer o dicionario com um iterador
        # for palavra in dicionario:
            # print('palavra encontrada')
        # else:
            # print('palavra não encontrada')

    # Para que o for entregue a chave e o valor na mesma saída devemos ecrever assim
         # for palavra, definicao in dicionario.items():
            # print(palavra, '=', definicao)
        # OU  print(f'''{palavra} = {definicao}''')

    # Para pegar só as chaves OU o valor do dicionário, devemos escrever
        # CHAVES .........  =>  dicionario.keys()
        # VALOR ..........  =>  dicionario.values()
        # CHAVE E VALOR ..  =>  dicionario.items()
            # Exemplo:
                # for palavra, definicao in dicionario.items():
                #     print(palavra, ' = ', definicao)

    # FUNÇÕES DE USO CONTÍNUO
        # Para saber o que a função faz executamos o seguinte comando
            # help(dict.clear)

        # DETALHANDO:
            # help: chama a função de ajuda
            # dict: é em qual local / objeto a ajuda vai ser executada
            # clear: é a função do objeto dicionário que a função help vai trazer a informação
            # fromkeys: é a função que cria um dicionario através de um iterável (range(qtd_range), lista, tupla, ...)
                # dict.fromkeys(range(10), 'vazio')
            # get: retorna o valor da chave se estiver no dicionário, senão, retorna um valor default
                # dicionario.get(palavra, '''PALAVRA NÃO ENCONTRADA! DIGITE UMA DAS PALARAS ABAIXO:  '''))
            # pop: remove uma chave do dicionário   
                # dicionario.pop('VERBETE')
            # popitem: retorna a última chave - valor
                # dicionario.popitem()
            # setdefault: adiciona uma chave caso ela não exista no dicionario com um valor default,
                # caso a chave exista o seu valor não sofrerá modificações
            # update: atualiza o dicionário com informações novas, proveniente(s) e outro(s) dicionário(s).
                # dicionario.update({
                #     'FATO' : 
                #     'Acontecimento acabado; evento, ocorrência: a fiscalização das barracas ilegais é agora um fato.'
                # })

# --------------------------------------------------------------------------------------------------
# v Inicando o programa v
# --------------------------------------------------------------------------------------------------
dicionario = {
    'DILIGENCIA'    :   'Zelo, cuidado e aplicação na realização de algo'
    , 'CORROBORAR'  :   'Confirmar a existência ou a verdade de; dar provas de; comprovar'
    , 'VERBETE'     :   'Conjunto que contém essas palavras com suas acepções, significados e explicações'
}

dicionario.update(
    {'FATO' :
        'Acontecimento acabado; evento, ocorrência: a fiscalização das barracas ilegais é agora um fato.'
    }
)


# Verificando o tipo
print( type(dicionario))
print(dir(dict))


print(f'''
{'-' * 80}
DIGITE UMA DAS PALAVRAS ABAIXO PARA EXIBIR O SEU SIGNIFICADO:
{'-' * 80}''')


for palavra in dicionario:
    print(palavra)

print('.' * 50)
palavra = input(f'''palavra: ''')
print('.' * 50)
print()

while not(palavra in dicionario):
    print('#' * 50)
    print(dicionario.get(palavra, '''PALAVRA NÃO ENCONTRADA !
    DIGITE UMA DAS PALARAS ABAIXO:  '''))
    # print('''PALAVRA NÃO ENCONTRADA !
    # DIGITE UMA DAS PALARAS ABAIXO:  ''')
    print('#' * 50)

    for palavra in dicionario:
        print(palavra)

    print()
    print('.' * 50)
    palavra = input('''digite uma palavra da lista: ''')
    print('.' * 50)
    print()

else:
    print(f'''{dicionario[palavra]}''')
    print()