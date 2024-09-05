##############################
# OPERAÇÕES COM TUPLAS
##############################

# 01- O comando help( tuple ), traz a ajuda referente aos comandos vinculados à tupla
# help (tuple)


# 02- A tupla é IMUTÁVEL, ou seja, não pode sofrer alterações nos seus itens. Para "alterar" vc tem que construir 1 NOVA
print(f'''
##############################
# OPERAÇÕES COM TUPLAS
##############################
==============================================================
02- Podemos criar uma TUPLA passando o comando: "tuple( (1, 2, 3) )", sem as aspas e teremos o resultado: {tuple ( (1, 2, 3) )}
---------------------------------------------''')

tupla_01 = (1, 2, 3)
tupla_02 = (4, 5, 6)

print(f'''E também podemos criar uma TUPLA usando variáveis e passando seus registros entre PARÊNTESES.
    "tupla_01 = (1, 2, 3)", sem as aspas.
    "tupla_02 = (4, 5, 6)", sem as aspas.
---------------------------------------------     
    TUPLA 01 ....... : {tupla_01}
    TUPLA 02 ....... : {tupla_02}
    Tipo da TUPLA 01 : {type(tupla_01)}
    Tipo da TUPLA 02 : {type(tupla_02)}
''')


# 03- Adição de TUPLAS, segue a mesma lógica das LISTAS
print(f'''
==============================================================    
03- Aqui está o somatório da TUPLA 01 + TUPLA 02 : {tupla_01 + tupla_02}
    Lembrando que esse somatório, tem que ser OBRIGATORIAMENTE entre 2+ TUPLAS.
''')


# 04- Verificar se um item está dentro da TUPLA
print(f'''
==============================================================
04- É possível efetuar a verificação se um item está dentro de uma TUPLA, usando o comando: "1 in tupla_01", sem as aspas.
    Esse é exatamente o comando que está trazendo o resultado : {1 in tupla_01}
    Aqui verificamos se o item 1 está na TUPLA 02 ........... : {1 in tupla_02}
''')


# 05- Verificando se 2 TUPLAS são IGUAIS
resposta = (tupla_01 == tupla_02)

print(f'''
==============================================================
05- Verifica se 2 TUPLAS são IGUAIS, com o comando "tupla_01 == tupla_02", sem as aspas : 
    Aqui está a TUPLA 01 : {tupla_01}
    Aqui está a TUPLA 02 : {tupla_02}
    
    P: {tupla_01} = {tupla_02} ?
    R: {resposta}
''')


# 06- Pegar itens da TUPLA
print(f'''
==============================================================
06- Podemos pegar itens das TUPLAS, com o comando: "tupla_02[0]"
    TUPLA 02 [0]    : {tupla_02[0]}
    TUPLA 02 [1]    : {tupla_02[1]}
    TUPLA 02 [2]    : {tupla_02[2]}

    TUPLA 02 [-1]   : {tupla_02[-1]}
    TUPLA 02 [-2]   : {tupla_02[-2]}
    TUPLA 02 [-3]   : {tupla_02[-3]}

    TUPLA 02 [1:]   : {tupla_02[1:]}
    TUPLA 02 [:-1]  : {tupla_02[:-1]}
    TUPLA 02 [::2]  : {tupla_02[::2]}
    TUPLA 02 [::-1] : {tupla_02[::-1]}
    
''')


# 07- Fazer iteração dos itens com o FOR
print('==============================================================')
for item in tupla_01:
    print(f'''07- Aqui temos a iteração do comando FOR dentro da TUPLA 01 POSIÇÃO [{tupla_01.index(item)}] : {item}''')
print('--------------------------------------------------------------')

for item in tupla_02:
    print(f'''07- Aqui temos a iteração do comando FOR dentro da TUPLA 02 POSIÇÃO [{tupla_02.index(item)}] : {item}''')
print()


# 08- Fazer multiplicação de uma TUPLA
print(f'''
==============================================================
08- Aqui temos a TUPLA 02 MULTIPLICADA 2x: {tupla_02 * 2}
''')


# 09- Contar quantas vezes 1 item apareceu numa TUPLA
print(f'''
==============================================================
09- Aqui temos a QTD de VEZES que o item TUPLA 02 MULTIPLICADA 2x: {tupla_02 * 2}
''')    

# 10- Obs sobre as TUPLAS
print('''
==============================================================      
10- OBS: O entendimento aqui, é que as TUPLAS NUNCA sofrem ALTERAÇÕES. Isso ocorre, porque ela é IMUTÁVEL,
ou seja, a ordem que chega é a ordem gravada.
    
      Essa é uma bela observação para o armazenamento de dados proveniente de qualquer banco de dados, seja 
ele um realmente um banco estruturado, sql lite, sql server, postgress, ou um arquivo qualquer que tenha
algum armazenamento de dados, csv, xls, xslx, delta, parquet, orc.
''')