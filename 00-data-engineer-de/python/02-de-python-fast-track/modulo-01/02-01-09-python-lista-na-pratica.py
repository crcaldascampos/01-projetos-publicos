##############################
# OPERAÇÕES COM LISTAS
##############################

# 01- O comando help( list ), traz a ajuda referente aos comandos vinculados à lista
# help (list)

# 02- Qualquer iterável como uma tupla por exemplo pode ser convertida para  1 lista, conforme abaixo
print()
print( (1, 2, 3, 4, 5))
print( type( (1, 2, 3, 4, 5)))
print()

##### 02.01- Transformando uma tupla em lista. Para isso devemos passar o comando list() antes da tupla = list( (1, 2, 3) )
print()
print( list( (1, 2, 3, 4, 5)))
print( type( list( (1, 2, 3, 4, 5))))
print()

# 03- Soma de listas gera 1 concatenação das listas envolvidas. NÃO é possível somar lista com valores soltos, sempre lista com lista.
lista_01 = [1, 2, 3]
lista_02 = [4, 5, 6]
lista_concatenada = lista_01 + lista_02
print(lista_01)
print(f'''A 1ª lista passada foi {lista_01}, a 2ª lista foi {lista_02}. Já a lista concatenada ficou assim: {lista_concatenada}.''')
print()

# 04- Verificar se o conteúdo está na lista com o comando IN
print(1 in lista_01)
print(1 in lista_02)
print()

# 05- Deletar iten da lista
del lista_01[1]
print(lista_01)
print()

# 06- Comparando listas
print(lista_01 == lista_02)
print(lista_01 != lista_02)
print()

# 07-Iteração em uma lista com o comando FOR
for item in lista_01:
    print(item)
print()

# 08- Multiplicação de uma LISTA por um VALOR
print(lista_02 * 5)
print()

# 09- Substituição de valores de uma lista
print(f'''ANTES a LISTA 01 estava com esses valores {lista_01}''')
lista_01[1] = 10
print(f'''AGORA a LISTA 01 está com esses valores {lista_01}''')
print()


##############################
# FUNÇÕES COM LISTAS
##############################
# 10- Copiar uma Lista, gerando uma lista independente
lista_01_copia = lista_01.copy()
print(f'''A cópia independente, denominada LISTA 01 CÓPIA possui os seguintes valores: {lista_01_copia}''')
print()

# 11- Adicionar itens à lista com a função APPEND
valor_add = int(input('Digite 1 valor para add à LISTA 01: '))
lista_01.append( valor_add)
print(f'''Nesse momento foi acrescentado à LISTA 01 o valor {valor_add} e, a LISTA 01 contém os valores: {lista_01}''')
print()
print(f'''A LISTA_01_COPIA agora possui os seguintes registros {lista_01_copia}''')
print()                                                 

# 12- Remover item da lista
lista_01_copia.remove(1)
print(f'''Após a utilização do comando "lista_01_copia.remove(1)", a lista_01_copia ficou assim {lista_01_copia}''')
print()

# 13- Contagem de itens dentro da lista
print(f'''Para sabermos QUANTOS "itens = 10" a "lista_01_copia" possui, que no caso é (são) {lista_01_copia.count(10)} item (itens),  
executamos o seguinte comando: "list_01_copia.count(10)", sem as aspas. Altere o valor do item para contar outros valores.''')
print()

# 14- Tornar a lista permanente usando a FUNÇÃo EXTEND. Ela trabalha de forma IMPLICITA sem que enxerguemos fazendo com que os
# valores sejam substituídos pelos valores unificados através da função EXTEND.
lista_03 = [7, 8, 9]
lista_01_copia.extend(lista_03)
print(f'''A LISTA 03 possui os seguintes valores: {lista_03}.''')
print(f'''Já a "LISTA 01 COPIA", possui os segiuntes valores: {lista_01_copia}''')
print()

# 15- Identificar o índice (index) de qualquer item da lista
lista_04 = list( ('joão', 'ana', 'paulo', 'joana', 'nasser', 'mateus') )
print(f'''A LISTA 04 possui os registros: {lista_04}''')
print()
print(f'''Para descobrir o índice do registro da "JOANA", que é o índice Nº: {lista_04.index('joana')}, devemos passar o 
seguinte comando: "lista_04.index('joana')", sem as aspas. Ao alterar o nome da "JOANA" por algum da lista, será identificado
o índice do registro mencionado.''')
print()

# 16- Inserir item em qualquer lugar da lista, utilizamos o INSERT(índice, item a ser adicionado)
lista_04.insert(0, 'marcos')
print(f'''Para adicionar um item em qualquer lugar da lista utilizamos a função INSERT. Dessa forma, adicionaremos o nome 
do 'MARCOS' ao início da lista. Para isso passamos o seguinte comando: "lista_04.insert(0, 'marcos')", sem as apas.
Ficando a LISTA 04 da seguinte forma: 

    {lista_04}

Lembrando apenas que a função APPEND, adiciona o item SEMPRE ao FINAL da LISTA, não deixando escolher a posição no qual será 
inserido o registro.''')
print()

# 17- Remover item por ÍNDICE
lista_05 = lista_04.copy()
print(f'''
    Para remover um item pelo índice utilizamos o seguinte comando: "lista_05.pop(0)", nesse caso excluíremos o 1º
da lista, que é o 'marcos'. Ficando a lista da seguinte forma:
    
    Essa é a LISTA 04 ............... : {lista_04}
    A LISTA 05 é uma CÓPIA da LISTA 04: {lista_05}

            O "{lista_05.pop(0)}" foi removido da LISTA 05.

    Agora a LISTA 05, está SEM o "{lista_04[0]}": {lista_05}

Lembando que, toda vez que utilizamos a função POP ele retorna o valor que foi EXCLUÍDO, como foi no caso do "{lista_04[0]}".
Já a função REMOVE, "lista_05.remove('marcos')", sem as aspas, tem como parâmetro o próprio ITEM a SER REMOVIDO e NÃO retorna 
o item removido.
''')

# 18- Ordenação de lista, SORT(INPLACE = PERMANENTE) e SORTED(temporariamente)
lista_06 = lista_04.copy()
lista_07 = list( (3, 2, 1) )

print(f'''Essa é a LISTA 06 que também é uma cópia da LISTA 04:
        
        LISTA 04: {lista_04}
        LISTA 06: {lista_06}

        Momento / status da ordenação com o comando "lista_06.sort()", sem as aspas: {lista_06.sort()}

    Essa lista foi criada para que pudéssemos executar a ordenação do seu conteúdo. Porém o comando utilizado para a ordenação:
"lista_06.sort()", sem as aspas, é uma função INPLÍCITA, ou seja, INPLACE, depois de executada ela permanece, guardando o status
de execução na memória.

        Aqui está a LISTA 04 ORIGINAL: {lista_04}
        Aqui está a LISTA 06 ORDENADA: {lista_06}

    Para efetuar a ordenação que NÃO É INPLACE devemos usar a função PYTHON chamada "sorted", serm aspas.
Ela executa a ordenação NÃO guardando o status da modificação.

        Aqui está a LISTA 07 ORIGINAL .......... : {lista_07}
        Aqui está a LISTA 07 ORDENADA .......... : {sorted(lista_07)}
        E aqui está a LISTA 07 ORIGINAL NOVAMENTE: {lista_07}
''')
print()


# 19- Inverter os valores da lista, REVERSE(INPLACE = PERMANENTE) e REVERSED(temporariamente)
lista_08 = lista_06.copy()
print(f''' ====================================================================================================
    Para inverter uma lista temos 2 opções: 1 IN PLACE que é a REVERSE, com o comando: "lista_08.reverse()", sem as aspas. 
E a que é TEMPORÁRIA e que fornece um iterador é a REVERSED, com o comando: "reversed(lista_06)"
      
        Aqui temos a LISTA 06 ORIGINAL ............................................... : {lista_06}
        Aqui temos a LISTA 08 ORIGINAL que é a CÓPIA da LISTA 06...................... : {lista_08}
        Momento / status da ordenação com o comando "lista_08.reverse()", sem as aspas : {lista_08.reverse()}
        Aqui temos a LISTA 08 INVERTIDA PERMANENTEMENTE .............................. : {lista_08}
        
    ============================================================================================================

        Aqui temos a LISTA 06 INVERTIDA TEMPORARIAMENTE, com o seu ID da operação .... : {reversed(lista_06)}
        Aqui temos a LISTA 06 ORIGINAL NOVAMENTE ..................................... : {lista_06}
        Para comprovar que a LISTA 08, realmente, está INVERTIDA PERMANENTEMENTE ..... : {lista_08}
''')
    
    
# 20- Limpar a lista com a função CLEAR
print(f'''======================================================================================================
Para apagarmos uma lista completa, devemos usar a função CLEAR, com o comando: "lista_01.clear()", sem as aspas.
    
    Aqui temos a LISTA 01 ........................................................................... : {lista_01}
    Momento / status da exclusão dos dados da LISTA 01 com o comando "lista_01.clear()", sem as aspas : {lista_01.clear()}
    Aqui temos a LISTA 01 APAGADA ................................................................... : {lista_01}

''')
print()


