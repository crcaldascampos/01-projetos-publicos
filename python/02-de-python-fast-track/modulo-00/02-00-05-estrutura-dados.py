#   fazer uma receita de biscoito  para o almoço de domingo
receita = "cookies'n cream"
print (receita)

geladeira = None
print (geladeira)

#   verificar a tipagem de dados das variáveis
print( type(receita))


# ----------------------------------------------------------
# lista de ingredientes para a receita de biscoito
# ----------------------------------------------------------
    # 3 xícaras de chá de farinha de trigo
    # 1 xícara de chá de manteiga sem sal à temperatura ambiente
    # 1 xícara de chá de açúcar refinado
    # 1 e 1/2 colher de chá de fermento em pó
    # 1 ovo

# iniciar a lista de ingredientes para fazer o biscoito
ovos = 1
recheio = False
fermento = 1.5 * 3  # gramas
acucar = 100.0      # gramas
manteiga = 100.0    # gramas
farinha = 300.0

print(type(receita), type(ovos), type(recheio), type(fermento))



# ----------------------------------------------------------
# operadores
# ----------------------------------------------------------

# ----------------
# aritméticos
# ----------------
aritmetico = 2 + 3
print(aritmetico)
print(acucar * 2)
print(50 / 3)   #   dividindo 50 biscoitos pa 3 pessoas
print(50 // 3)  #   quantos biscoitos inteiros por pessoa
print(50 % 3)   #   quantos biscoitos sobram (módulo)
print(2 ** 3)   #   potência


# ----------------
# atribuição (como o nome diz, atribui o valor ajustado de acordo com a passagem de parâmetro:
#   +=  ||  -=  ||  *=  ||  /=  ||  **= ||  %=  ||  //=     ||)
# ----------------
variavel = 'valor'
ovos += 1
print(ovos)

ovos -= 1
print(ovos)

ovos *= 2
print(ovos)

ovos /= 3
print(ovos)

ovos **= 3
print(ovos)

ovos %= 3
print(ovos)

ovos //= 3
print(ovos)


# ----------------
# comparação
# ----------------
acucar_farinha = acucar == farinha
print(acucar_farinha)

acucar_farinha = acucar != farinha
print(acucar_farinha)

acucar_farinha = acucar > farinha
print(acucar_farinha)

acucar_farinha = acucar <= farinha
print(acucar_farinha)

print(acucar <= farinha)

# ----------------
# estrutura dados (tupla, variável, lista, dicionário)
# ----------------
    # dicionário    =   livro de receitas   =   indíces                 =   { }
    # lista         =   lista de compras    =   não importa a ordem     =   [ ]
    # tupla         =   sequência de passos =   a ordem importa         =   ( )


# dicionário    =   type( {} )  =   chave:valor
receitas_dicionario = {     # início dicionário externo 01
    'receita_01'    :   None
    , 'receita_02'  :   None
    , 'biscoitos "os melhores do mundo"'    :   {   # início do dicionário interno 01
        'ingredientes'  :     # início da lista geral = não importa a ordem
            [   # início da lista de ingredientes       = não importa a ordem
                'ovos'
                , 'recheio'
                , 'fermento'
                , 'acucar'
                , 'manteiga'
                , 'farinha'
            ]   # fim da lista de ingredientes          = não importa a ordem

            , 'modo-preparo'    :   ( # início da tupla do modo de preparo    = a ordem importa
                '1. Bata o açúcar e a manteiga na batedeira'
                , '2. Acrescente o ovo e bata mais um pouco. Junte a baunilha e misture na velocidade baixa'
                , '3. Vá acrescentando o fermento, misturando as 2 xícaras de farinha'
                , '4. Coloque a massa na mão e vá enfarinhando até a massa para de grudar nas mãos'
                , '5. Leve a massa à geladeira por 20 minutos'
                , '6. Sobre a mesa enfarinhada, abra-a com um rolo. Corte os biscoitos'
                , '7. Coloque em uma assadeira forrada com papel manteiga'
                , '8. Leve para assar, em fogo baixo, por aproximadamente 15 minutos'
            )   # fim da tupla do modo de preparo       = a ordem importa
    }   # fim do dicionário interno 01
}   # fim do dicionário externo 01

# print(receitas_dicionario['biscoitos "os melhores do mundo"'])
print(receitas_dicionario['biscoitos "os melhores do mundo"']['ingredientes'])

padaria = [
    receitas_dicionario['biscoitos "os melhores do mundo"']['ingredientes']
    , 'leite', 'queijo', 'presunto', 'água'
]

padaria_02 = [
    'ovos', 'recheio', 'fermento', 'acucar', 'manteiga', 'farinha'
    , 'leite', 'queijo', 'presunto', 'água'
]

print(padaria)
print('ovos' in padaria)
print(receitas_dicionario['biscoitos "os melhores do mundo"']['ingredientes'] in padaria)

print(padaria_02)
print('ovos' in padaria_02)

ingredientes = receitas_dicionario['biscoitos "os melhores do mundo"']['ingredientes']
print(ingredientes)

# geladeira = ingredientes    # add os dados de uma lista na outra independentemente de onde é add
geladeira = ingredientes.copy()     # cria 1 cópia literalmente da lista passada como parâmetro
print(geladeira)
print(geladeira is ingredientes)

geladeira.append('queijo')
# ingredientes.remove('queijo')
print(geladeira)
print(ingredientes)