##############################
# OPERAÇÕES COM STRINGS
##############################

# 01- O comando help( tuple ), traz a ajuda referente aos comandos vinculados à tupla
# help (str)

print(f'''
##############################
# OPERAÇÕES COM STRINGS
##############################
==============================================================
01- Para verificarmos o help da função STRING ( str ), devemos passar o seguinte comando: 
    help( str )
''')



# 02- Concatenar STRINGS
string_01 = 'bom'
string_02 = 'dia'

print(f'''
==============================================================
02- Para CONCATENAR ( SOMAR ) 2+ STRINGS podemos executar o seguinte comando:
    
    STRING_01 + STRING_02

Sabemos que a STRING_01 : {string_01}
E a STRING_02 ......... : {string_02} 

Ao CONCATENAR a STRING_01 + STRING02 teremos, {string_01} + {string_02} = {string_01 + string_02}

Repare que as 2 STRINGS ficaram coladas, para separá-las devemos passar um ESPAÇO entre elas, ficando assim:
   "STRING_01" + " " + "STRING_02", sem as aspas, e o resultado é : {string_01 + ' ' + string_02}
''')



# 03- Verificar se 1 STRING CONTÉM outra
print(f'''
==============================================================
03- Para saber se 1 STRING CONTÉM outra, executamos o seguinte comando:      
        print("o" in string_01)

    Sabendo que a STRING_01 tem o conteúdo: {string_01}
        Logo o resultado é: {'o' in string_01}

    Mas e para a STRING_02 que tem o conteúdo: {string_02} ?
        O resultado é: {'o' in string_02}

    Ainda na questão das verificações é possível verificar se uma STRING ou ESPAÇO NÃO ESTÁ CONTIDO na STRING_01.
    O comando que devemos passar é:
        print(" " not in STRING_01), e como resultado temos: {' ' not in string_01}

    Também podemos efetuar essa verificação dentro da STRING_02.
        print(" " not in STRING_02), e o resultado é: {' ' not in string_02}
''')



# 04- Verificar se 1 STRING É IGUAL a outra
print(f'''
==============================================================
04- Para saber se 1 STRING = OUTRA, executamos o seguinte comando:      
        print(string_01 == string_02), assim temos: {string_01 == string_02}
    
    Se não são iguais, então as 2 STRINGS são diferentes?
        print(string_01 != string_02), e o resultado é: {string_01 != string_02}
''')



# 05- Formatação de STRING
print(f'''
==============================================================
05- Para formatar 1 STRING, executamos o seguinte comando:      
        print(f'Texto que não seja variável ou código "ABRE CHAVES" variável ou código python "FECHA CHAVES" ')
''')



# 06- Iteração de STRING, comando FOR
usuario_tupla = ('Matheus', 'Paulo', 'Ana', 'João', 'Carlos', 'Marilza', 'Evelyn', 'Bernardo')
print(f'''
==============================================================
06- Para iterar sobre 1 STRING numa lista / tupla, executamos o seguinte comando:      
        
    for usuario in lista_usuario:
        print(f'Bom dia "ABRE CHAVES" usuario "FECHA CHAVES" ')
      
    Dessa forma teremos os seguintes resultados quando iteramos pela tupla USUARIO_TUPLA: 
        {usuario_tupla}
''')    

for usuario in usuario_tupla:
    print(f'''          Bom dia {usuario}''')
print()



# 07- Buscar STRING pelo ÍNDICE e comando FOR
print(f'''
==============================================================
07- Para buscar 1 STRING pelo ÍNDICE, executamos o seguinte comando:      
    print(USUARIO_TUPLA [índice])
    
    Conforme podemos observar abaixo:''')

for usuario in usuario_tupla:
    print(f'''        USUARIO_TUPLA [ {usuario_tupla.index(usuario)} ] = {usuario}''')

print(f'''
    Assim temos as seguintes STRINGS quando referenciamos pelo índice: 
        USUARIO_TUPLA : {usuario_tupla[0]}
        USUARIO_TUPLA : {usuario_tupla[-1]}
        USUARIO_TUPLA : {usuario_tupla[1::]}
        USUARIO_TUPLA : {usuario_tupla[1:]}
        USUARIO_TUPLA : {usuario_tupla[:1]}
        USUARIO_TUPLA : {usuario_tupla[2:5]}
        USUARIO_TUPLA : {usuario_tupla[::2]}
        USUARIO_TUPLA : {usuario_tupla[::-1]}
''')



# 08- Verificar o tamanho da TUPLA / LISTA / VARIÁVEL
print(f'''
==============================================================
08- Para verificar o TAMANHO de uma LISTA / TUPLA / VARIAVEL, executamos o seguinte comando:      
    print( len( [USUARIO_TUPLA] ) ) que possui a qtd de {len(usuario_tupla)} registros que estão abaixo.
        
        {usuario_tupla}
''')



# 09- Multiplicação de STRINGS
print(f'''
==============================================================
09- Para MULTIPLICAR a STRING desejada, executamos o seguinte comando:      
        print( STRING_DESEJADA * QTD_DESEJADA  )

    Por exemplo, se quisermos MULTIPLICAR o sinal de cifrão ( $ ) 50 vezes, passamos o comando:
        print( '$' * 50  )
    
    E assim temos o resultado:  {'$' * 50}        
''')



# 10- FUNÇÕES: Colocando o Texto com a 1ª Maiúscula (CAPTALIZE), todas em MAIÚSCULAS (UPPER)
# e todas em minúsculas (LOWER)
nome_emabralhado = 'cArLos roBERto cALdAs camPoS'
print(f'''
==============================================================
10- FUNÇÕES
    Abaixo temos um "nOme eMbaRaLHAdO":
      
        "nOme eMbaRaLHAdO"  ........................ :  {nome_emabralhado}
      
    Para transformar a STRING :
        Com a 1ª Letra Maiúscula (CAPITALIZE)
            str.capitalize(nome_embaralhado) ....... :  {str.capitalize(nome_emabralhado)}

        Todas em MAIÚSCULAS (UPPER)      
            str.upper(nome_embaralhado) ............ :  {str.upper(nome_emabralhado)}

        Todas em MINÚSCULAS (LOWER)      
            str.lower(nome_embaralhado) ............ :  {str.lower(nome_emabralhado)}
''')



# 11- Centralizar STRINGS
print(f'''
==============================================================
11- Para CENTRALIZAR a STRING desejada, executamos o seguinte comando:      
        print( str.center(STRING, QTD ESPAÇO A SER ADICIONADO / CENTRALIZADO, CARACTER QUE ACOMPANHARÁ O TEXTO)  )
    
    OBS 01: Os espaços acrescentados antes e depois do "nOme eMbaRaLHAdO" é apenas para descolar o "-" do 
    início e fim do "nOme eMbaRaLHAdO".
    
    OBS 02: Para efetuar a centralização do "nOme eMbaRaLHAdO" em MAIÚSCULA e MINÚSCULA devemos passar as
    funções str.upper e str.lower antes da STRING, conforme abaixo:

    
    Dessa forma pegando o "nOme eMbaRaLHAdO" e se quisermos centralizá-lo dentro de 120 caracteres, faremos:
      
        11.01- "nOme eMbaRaLHAdO"
            print( str.center(" " + "nOme eMbaRaLHAdO" + " ", 120, '=') )
      
        11.02- MAIÚSCULAS
            print(str.center(" " + str.upper("nOme eMbaRaLHAdO") + " ", 120, "*" ) )
      
        11.03- MINÚSCULAS
            print(str.center(" " + str.lower("nOme eMbaRaLHAdO") + " ", 120, "#" ) )
      
        11.04- Title( Todas As Palavras Iniciam Com Letra Maiúscula )
            print(str.center(" " + str.title("nOme eMbaRaLHAdO") + " ", 120, "&" ) )
      
        11.05- Capitalize( Apenas a 1ª letra em maiúscla )
            print(str.center(" " + str.captalize("nOme eMbaRaLHAdO") + " ", 120, "%" ) )
      

    E o resultado será:
        11.01-    {str.center(' ' + nome_emabralhado + ' ', 120, '=')}
        11.02-    {str.center(' ' + str.upper(nome_emabralhado) + ' ', 120, '*' )}
        11.03-    {str.center(' ' + str.lower(nome_emabralhado) + ' ', 120, '#')}
        11.04-    {str.center(' ' + str.title(nome_emabralhado) + ' ', 120, '&')}
        11.05-    {str.center(' ' + str.capitalize(nome_emabralhado) + ' ', 120, '%')}     
''')



# 12- Contagem de STRINGS dentro     de outra
print(f'''
==============================================================
12- Para CONTAR 1 STRING dentro de outra STRING, executamos o seguinte comando:      
        print( STRING_A_SOFER_A_CONTAGEM.count(STRING_A_SER_CONTADA)  )
      
    Por exemplo, se quisermos CONTAR a letra "A" dentro do "nOme eMbaRaLHAdO", passamos o comando:
        print( nome_embaralhado.count('A') )
      
    E assim temos o resultado:  {nome_emabralhado.count('A')}
    
    OBS 12.01: Essa verificação DIFERENCIA letras MAIÚSCULAS de MINÚSCULAS.
''')
     


# 13- Prefixo (Começa Com) e Sufixo (Termina Com) de uma STRING
print(f'''
==============================================================
13- Para sabermos se uma STRING possui um PREFIXO (começa com), executamos o seguinte comando:
        print( STRING_A_SER_VERIFICADA.startwith( PREFIXO_A_SER_VERIFICADO)  )
      
    13.01- P R E F I X O
        Por exemplo, se quisermos saber se a STRING COMEÇA com "CAR", passamos o comando:
            print( str.upper(nome_embaralhado).startwith( 'CAR' ) )
        
                P1:  O nome "{str.upper(nome_emabralhado)}" COMEÇA com "CAR"?
                R1:  {str.upper(nome_emabralhado).startswith('CAR')}

 ---------------------------------------------------------------------------------------------------------

    13.02- S U F I X O
        Já para sabermos se uma STRTING possui um SUFIXO (termina Com), executamos o seguinte comando:
            print( STRING_A_SER_VERIFICADA.endwith( PREFIXO_A_SER_VERIFICADO)  )
                
        Por exemplo, se quisermos saber se a STRING TERMINA com "LOS", passamos o comando:
            print( str.upper(nome_embaralhado).endwith( 'LOS' ) )

                P2: O nome "{str.upper(nome_emabralhado)}" TERMINA com "LOS"?
                R2: {str.upper(nome_emabralhado).endswith('LOS')}

                P3: Então TERMINA com "POS"?
                R3: {str.upper(nome_emabralhado).endswith('POS')}

        OBS 13.01: Essa verificação DIFERENCIA letras MAIÚSCULAS de MINÚSCULAS.
''')



# 14- Encontrar a 1ª ocorrência de 1 letra na STRING
print(f'''
==============================================================
14- Para ENCONTRAR a 1ª ocorrência de 1 letra na STRING, executamos o seguinte comando:      
        print( STRING_A_SER_VERIFICADA.find(STRING_A_SER_ENCONTRADA)  )
      
    Por exemplo, se quisermos ENCONTRAR a letra "A" dentro do "nOme eMbaRaLHAdO", passamos o comando:
        print( str.upper(nome_embaralhado).find('A') )
      
    A letra "A" será procurada dentro da STRING "{str.upper(nome_emabralhado)}".
    E assim temos o resultado da POSIÇÃO:  {str.upper(nome_emabralhado).find('A')}
    
    Se quisermos trazer a letra correspondente ao ÍNDICE {str.upper(nome_emabralhado).find('A')}, faremos:
        print( str.upper( nome_embaralhado[1] ) ) )
    
    Assim teremos a letra: {str.upper(nome_emabralhado[1])}

    OBS 14.01: Essa verificação DIFERENCIA letras MAIÚSCULAS de MINÚSCULAS.
    OBS 14.02: Lembre-se que a contagem das posições inicia-se com "0".
''')



# 15- Verificação de STRINGS
print(f'''
==============================================================
15- Para VERIFICAR a STRING desejada, executamos o seguinte comando:      
        print( STRING_DESEJADA.função-de-verificação )

    Por exemplo, se quisermos VERIFICAR se é:
        15.01- Totalmente Numérico (ISALNUM) .......... :    print( STRING_DESEJADA.isalnum() )
        15.02- Decimal (ISDECIMAL) .................... :    print( STRING_DESEJADA.isdecimal() )
        15.03- Dígito (ISDIGIT) ....................... :    print( STRING_DESEJADA.isdigit() )
        15.04- Alfa / Letras (ISALPHA) ................ :    print( STRING_DESEJADA.isalpha() )
        15.05- Minúsculo (ISLOWER) .................... :    print( STRING_DESEJADA.islower() )
        15.06- Maiúsculo (ISUPPER) .................... :    print( STRING_DESEJADA.isupper() )
        15.07- Cada Palavra Em Maiúsculo (ISTITLE) .... :    print( STRING_DESEJADA.istitle() )
            
''')



# 16- Junção e Separação de STRINGS
print(f'''
==============================================================
16- JUNÇÃO E SEPARAÇÃO DE STRINGS
    16.01- Para JUNTAR STRINGS (JOIN), executamos o seguinte comando:
            print( ' '.join( [ "beija", "flor", "varias", "outras", "palavras" ] )
        
        E o resultado é: "{' '.join(['beija', 'flor', 'varias', 'outras', 'palavras']) }"
        
        OBS 16.01: Lembrando que para a função JOIN funcionar, precisaremos ter ao menos 1 lista.

--------------------------------------------------------------------------------------------------        

    16.02- Para SEPARAR STRINGS (SPLIT), executamos o seguinte comando:
            print("nOme eMbaRaLHAdO".split(" "))

        E o resultado é : {nome_emabralhado.split(' ')}

        OBS 16.02: Aqui a separação OBRIGATORIAMENTE é ARMAZENADA em 1 LISTA.      
''')



# 17- Remover Espaço em Branco da Esquerda e da Direita de 1 STRING
print(f'''
==============================================================
17- Para REMOVER espaço em branco de 1 STRING, executamos o seguinte comando:
    
    17.01- DIREITA
        print( STRING_A_ELIMINAR_ESPAÇO_EM_BRANCO_DO_LADO_DIREITO.rstrip() )
            {nome_emabralhado.rstrip()}

------------------------------------------------------------------------------------------

    17.02- ESQUERDA
        print( STRING_A_ELIMINAR_ESPAÇO_EM_BRANCO_DO_LADO_ESQUERDO.lstrip() )
            {nome_emabralhado.lstrip()}
    
''')



# 18- Substituir algum caracter em 1 STRING
print(f'''
==============================================================
18- Para SUBSTITUIR 1 caracter de 1 STRING, executamos o seguinte comando:

        print( STRING_A_SUBSTITUIR_CARACTER.replace(' ', '-') )

    Assim temos o "nOme eMbaRaLHAdO" com ESPAÇO ... :   {nome_emabralhado}
    E aqui o "nOme eMbaRaLHAdO" com HIFEN (-) ..... :   {nome_emabralhado.replace(' ', '-')}
      
''')



# 19- Preenchimento de números à ESQUERDA em 1 STRING
numero_a_esquerda = '1234'
print(f'''
==============================================================
19- Para PREENCHER 1 STRING com NÚMEROS À ESQUERDA, executamos o seguinte comando:

        print( STRING_A_SER_PREENCHIDA_COM_NUMEROS_A_ESQUERDA.zfill( QTD MÁXIMA DE CARACTERES ) )

    Assim temos o número como digitado .......... :   {numero_a_esquerda}
    E aqui o número com os zeros à esquerda ..... :   {numero_a_esquerda.zfill(10)}

    OBS 19.01: O valor entre parênteses do ZFILL deve ser INTEIRO, ou seja, SEM ASPAS, e indica quantos
        caracteres essa saída terá. Se colocarmos 10, serão 10 caracteres somando os ZEROS e os caracteres
        já presentes na variável.

            No nosso caso, como temos os caracteres 1234, já temos 4 caracteres, portanto serão acrescidos 6
        caracteres 0 para completarmos os 10 caracteres explicitados entre parênteses.
      
''')     
