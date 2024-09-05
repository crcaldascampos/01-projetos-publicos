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

