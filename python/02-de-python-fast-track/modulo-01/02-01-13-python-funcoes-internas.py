##############################
#   FUNÇÕES INTERNAS
##############################

variavel    =   2
lista       =   [1, 'a', 2, 'b']
dicionario  =   {'nome' : 'Carlos', 'idade' : 40}
var_range   =   range(10)

print(f'''
###############################################
# FUNÇÕES INTERNAS  -   BUILT-IN FUNCTIONS
###############################################
==============================================================
    01- PARÂMETROS À:
        01.01- ESQUERDA são OBRIGATÓRIOS, estes NÃO POSSUEM sinal de =
        01.02- DIREITA são OPCIONAIS, eles POSSUEM o sinal de = e, caso nenhum valor for passado, eles 
            assumirão um valor PADRÃO / DEFAULT, passado explicitamente na CRIAÇÃO da FUNÇÃO.

==============================================================             
    02- ESTRUTURA DA FUNÇÃO
        
        def nome_funcao(parametro01, parametro02):
            lógica_negócio
            return  #opcional_01
            return  #opcional_02
            return  #opcional_03
                    .
                    .
                    .
            return  #opcional_N
        

        
    OBS 02.00: return None #por padrão

    OBS 02.01: Quando passado o PRINT ao tentar referenciar a saída, não nos retornará nada (NONE)!
        
    OBS 02.02: Já com o RETURN qualquer operação executada na FUNÇÃO carregará o valor, quando passarmos
      a FUNÇÃO em questão em alguma parte do código!
      
==============================================================          
    03- VERIFICANDO AS FUNÇÕES INTERNAS - BUILT-IN FUNCTIONS
        Lembrando que para todas as funções podemos utilizar a função help(nome_da_função)

        03.01- ABS()
            Transforma qualquer número, seja ele positivo ou negativo, em número positivo.
           
            Exemplo:
                O número 1 com a fução ABS(1) tem o resultado ......... :   {abs(1)}
                Já o número -1 com a função ABS(-1) tem o resultado ... :   {abs(-1)}

-----------------------------------------------------------------        
        03.02- ALL( [LISTA DE VALORES A SER VERIFICA SE SÃO TRUE OU FALSE] )
            Verifica 1 lista de valores booleanos para saber se essa lista é verdadeira (TRUE) ou falsa         (FALSE).
            Se TODOS os valores forem TRUE ele retorna TRUE, senão FALSE.
           
            Exemplo:
                lista-01= all([True, True, True]), retornará .......... :   {all([True, True, True])}
                lista-02= all([True, True, False]), retornará ......... :   {all([True, True, False])}

-----------------------------------------------------------------        
        03.03- ANY( [LISTA DE VALORES A SER VERIFICA SE SÃO TRUE OU FALSE] )
            Verifica se pelo menos 1 valor booleano da lista é verdadeiro (TRUE).
            Se 1 for, ele retorna TRUE, senão FALSE.

            Exemplo:
                lista-03= any([False, False, True]), retornará .......... :  {any([False, False, True])}
                lista-04= any([False, False, False]), retornará ......... :  {any([False, False, False])}

-----------------------------------------------------------------
        03.04- BOOL(VALOR A SER VERIFICADO)
            Por padrão ele assume o valor FALSE se não for especificado!
            Se digitar um valor a função verifica para determinar se é verdadeiro (TRUE) ou falso (FALSE).

            Exemplo:
                bool(), retornará ... : {bool()}
                bool(1), retornará .. : {bool(1)}
                
-----------------------------------------------------------------
        03.05-  DICT ()
            Retorna um dicionário vazio.
            
            Exemplo: 
                Ao passarmos a função dict (), retornará .............. :  {dict ()}
        
-----------------------------------------------------------------
        03.06-  DIR ()
            Retorna os argumentos e atributos de um objeto.

            Exemplo:
                A função dir(variável)      ou      dir(lista)      ou      dir(dicionário), retornará:
                        {dir(variavel)}     ou     {dir(lista)}     ou     {dir(dicionario)}

-----------------------------------------------------------------
        03.07-  DIVMOD ()
            Retorna o valor da divisão inteira e o módulo ao mesmo tempo.
            Dessa forma temos o seguinte resultado:
                
                divmod( 5, 2 ), retornará ............................... :    {divmod( 5, 2 )}
                
            OBS 03.07.01: Essa função traz o mesmo resultado, se passarmos os 2 cálculos em sequência:
                5//2, 5%2    que retornará ................................. :      {5//2, 5%2} 

            03.07.01-   E caso queira selecionar apenas o valor da divisão inteira ou o valor do módulo, devemos passar o índice dessa TUPLA,
            da seguinte forma:

                03.07.01.01-  Para pegarmos apenas o valor da divisão inteira, passaremos o índice [0] após a função:
                    divmod( 5, 2 )[0]   retornará ....................... :     {divmod( 5, 2 )[0]}

                03.07.01.02-  Para selecionarmos apenas o valor do módulo, passaremos o índice [1] após a função:
                    divmod( 5, 2 )[1]   retornará ...................... :      {divmod( 5, 2 )[1]}

-----------------------------------------------------------------
        03.08-  ENUMERATE( LISTA / DICIONÁRIO )
            Cria uma numeração para uma LISTA ou DICIONÁRIO, para efetuar possível refeência futura.

            Exemplo:
                03.08.01- Para criarmos uma LISTA utilizamos, 
                    
                    list( enumerate( [ "pão", "leite", "ovos", "manteiga" ]))    retornará  ..... : 

                    {list( enumerate( [ 'pão', 'leite', 'ovos', 'manteiga' ]))}
                
                03.08.02- Para criarmos um DICIONÁRIO utilizamos,
                    dict( enumerate( [ "pão", "leite", "ovos", "manteiga" ] ))  retornará ..... :
                    {dict( enumerate( [ 'pão', 'leite', 'ovos', 'manteiga' ]))}
                
                03.08.03- Para iniciarmos com um número diferente, devemos passar o parâmetro START após o ENUMERATE 
                e dentro da LISTA / DICIONÁRIO:
                    03.08.03.01-  LISTA:
                        list( enumerate( ["pão", "leite", "ovos", "manteiga"]), start = 80001 )
                        {list( enumerate( [ 'pão', 'leite', 'ovos', 'manteiga' ], start = 80001 ))}

                    03.08.03.02-  DICIONÁRIO:
                        dict( enumerate( ["pão", "leite", "ovos", "manteiga"]), start = 80001 )
                        {dict( enumerate( ['pão', 'leite', 'ovos', 'manteiga'], start = 80001 ))}

-----------------------------------------------------------------
        03.09-  FILTER + RANGE( LISTA )
            Seleciona apenas o que necessita ser filtrado dentro de 1 LISTA / DICIONÁRIO, por exemplo:
                Se passarmos a função range(10) ele trará uma informação do intervalo inicial e final. Para retornarmos com
                1 LISTA devemos passar a função respectiva antes do RANGE, ou seja:
                    
                    LIST( range(10) )

                Dessa forma teremos:
                    range(10)           retornará o primeiro e o último valor do range .......................... : {range(10)}
                    LIST( range(10) )   retornará a lista dos 10 valores passados dentro do parâmetro do RANGE .. : { list( var_range )}

            Para filtrar os valores pares por exemplo, devemos criar uma fução que retorne os valores separadamente nomeando-a como
            FILTRA_PAR, dessa forma teremos:

######################################################
##   SALTO PARA A EXECUÇÃO DA FUNÇÃO FILTRA_PAR
######################################################
''')


######################################################
##   FUNÇÃO FILTRA PAR
######################################################
def filtra_par(x):
    if  x % 2 == 0:
        return True        #Aqui passamos o TRUE para retornar o valor PAR.
    else:
        return  False      #Aqui passamos o FALSE para retornar o valor IMPAR.

for numero in var_range:
    print(filtra_par(numero))


print(f'''
######################################################
##   RETORNANDO APÓS A EXECUÇÃO DA FUNÇÃO FILTRA_PAR
######################################################

            Para efetuarmos o filtro dos pares após a execução da função FILTRA_PAR devemos, executar os comandos abaixo:
                FILTER(função_lista, iterável) retornará a posição da memória na qual o filtro foi alocado ... : 
                    
                    {filter(filtra_par, var_range)}
            
            
            Assim devemos passar a função LIST antes da função FILTER:
                LIST( FILTER(função_lista, iterável) )  retornará a lista filtrada ................... : 
                    
                    {list( filter( filtra_par, var_range) )}
                
                    
            OBS 03.09.01: Essa tratativa será MUITO IMPORTANTE quando olharmos para MÁSCARAS dentro do NUMPY.
        

-----------------------------------------------------------------
        03.10-  LEN (RETORNA O TAMANHO DE QUALQUER OBJETO PASSADO ENTRE OS PARENTESE)
            Qualquer objeto pode ser medido, ou seja contabilizando o número de itens dentro do objeto passado como parâmetro.

            Exemplo:
                len( [0, 2, 4, 6, 8] )    retorna .................................................... :  {len( [0, 2, 4, 6, 8] )}
        

-----------------------------------------------------------------
        03.11-  MAP ( )
            Funciona como o FILTER, só que ao invés de remover, ele aplica as modificações / alterações.

######################################################
##   SALTO PARA A EXECUÇÃO DA FUNÇÃO DOBRO
######################################################
''')

######################################################
##  INÍCIO DA FUNÇÃO DOBRO
######################################################
def fn_dobro (x):
    return  x * 2

######################################################
##  FINAL DA FUNÇÃO DOBRO
######################################################

print(f'''
######################################################
##   RETORNANDO APÓS A EXECUÇÃO DA FUNÇÃO DOBRO
######################################################
            
            Para eibir o resultado da função MAP, devemos passar o seguinte comando:
                map(função_lista, iterável) retorna a posição alocada na memória ............................ :    
                    
                        {map( fn_dobro, var_range )}
            
            Para exibir as alterações feitas, devemos passar a função LIST à frente do exemplo anterior:
                list( map(função_lista, iterável) ) retornará a lista com a aplicação da função FN_DOBRO ..... :

                        Lista Origem, list( var_range ) .................................... : {list( var_range )} 
                        Lista com a função FN_DOBRO, list( map( fn_dobro, var_range )) ..... : {list( map( fn_dobro, var_range ))}

                        
-----------------------------------------------------------------
        03.12-  MAX( ITERÁVEL )    E   MIN( ITERÁVEL )
            Seleciona o valor MÁXIMO e o valor MÍNIMO de um ITERÁVEL:
                max( lista / função_lista )  retornará  ............... :   {max( var_range )}
                min( lista / função_lista )  retornará  ............... :   {min( var_range )}

-----------------------------------------------------------------
        03.13-  POW( )
            Usado para definir a potência de um número ou lista.
            Sabemos que podemos utilizar 2 asteríscos para gerar a potência de 1 número, por exemplo: 
                
                2 ** 2 .................. retornará ........................... :   { 2 ** 2 }
            
            Porém usando a função POW também podemos obter o mesmo resultado:
                
                pow( base, expoente )
                pow(  2  ,     2    )    retornará  ........................... :   { pow( 2, 2 )}


-----------------------------------------------------------------
        03.14-  PRINT( )
            Podemos modificar algumas coisas nessa função, por exemplo alterar o separador, isso modifica a 
            apresentação da saída do texto, por exemplo:

                print("olá", "mundo")   retornará   ........................... :   ''', end= ' ')

print('olá', 'mundo', sep=', ')
print()

print(f'''
            Outra funcionalidade quando utilizamos a função PRINT é que para que ela não pule a linha devemos alterar
            o final, com o parâmetro END onde o END altera por exemplo para apenas um ESPAÇO de um print para o outro
            conforme foi utilizado acima.
    
-----------------------------------------------------------------
        03.15-  REVERSED( LISTA )   E   SORTED( LISTA )
            Utilizamos a função REVERSED( LISTA ) para invertermos a direção de uma LISTA, para trazermos de forma DECRESCENTE.
            Por exemplo:
      
                A lista é essa ........................................ :   {list( var_range )}
                list( reversed( lista / função_lista ) )    retornará   :   {list( reversed( var_range ))}

                
            Já a função SORTED( LISTA ) é utilizada para invertermos a direção de uma LISTA, para trazermos de forma CRESCENTE.
            Por exemplo:

                A lista é essa ........................................ :   {list( reversed( var_range ))}
                list( sorted( lista / função_lista ) )      retornará   :   {list( sorted( reversed( var_range )))}

-----------------------------------------------------------------
        03.16-  ROUND( VALOR )
            Utilizado para arredondar números.
            Por exmeplo:

                round( valor, qtd casas decimais)
                round( 3.14 ,        1          )   retornará .........  :   {round( 3.14, 1 )}


-----------------------------------------------------------------
        03.16-  SUM( VALOR / LISTA )
            Faz a soma de um valor / lista.
            Por exemplo:
                sum( lista )
                sum( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] )    retornará .............................. :  {sum( list( var_range ) )}


-----------------------------------------------------------------
        03.17-  ZIP( LISTA )    ==>     SAÍDA: LISTA( 2+ LISTAS )    |      DICIONÁRIO( 2 LISTAS )
            Faz a união de 2 ou mais LISTAS desde que elas possuam o mesmo tamanho, retornando a saída de 1 LISTA que possui várias TUPLAS.
            Por exemplo:
                
                zip( lista_01, lista_02)
                
                zip( [ '1', '2', '3' ], [ 'a', 'b', 'c' ] ) retornará a posição da memória . : {zip( [ '1', '2', '3' ], [ 'a', 'b', 'c' ], [ '!', '@', '#' ]  )}
                
                list( zip( [ '1', '2', '3' ], [ 'a', 'b', 'c' ] )) retornará ............... : {list( zip( [ '1', '2', '3' ], [ 'a', 'b', 'c' ], [ '!', '@', '#' ] ))}
                
            
            
            Já a saída como DICIONÁRIO, só podemos ter 2 LISTAS para combinar por conta de ser um armazenamento de CHAVE - VALOR.

                dict( zip( [ '1', '2', '3' ], [ 'a', 'b', 'c' ] )) retornará ............... : {dict( zip( [ '1', '2', '3' ], [ 'a', 'b', 'c' ] ))}

            
''')

######################################################
##  INÍCIO DA FUNÇÃO BÔNUS
######################################################

#   COM_001:    DEFINE O VALOR A SER ADIVINHADO
defina_valor_advinha = int( input( 'Digite um valor a ser alimentado na função advinha: '))

#   COM_002:    FUNÇÃO QUE VERIFICA SE O VALOR DIGITADO FOI IGUAL AO VALOR DEFINIDO NA ETAPA ANTERIOR
def adivinha(n):
    if n == defina_valor_advinha:
        return 'GANHOU'
    return 'PERDEU'

#   COM_003:    VALOR NO QUAL SERÁ VERIFICADO COM O VALOR DEFINIDO ANTERIORMENTE N TÓPICO COMENTARIO COM_001
valor_advinha = int(input(f'Digite o valor a ser verificado: '))

#   COM_004:    COMPARA O COM_003 COM O COM_001 E EMITE A RESPOSTA
if(valor_advinha != defina_valor_advinha):
    print(f'O valor da função advinha é {defina_valor_advinha} e, por isso você {adivinha(valor_advinha)}, pois digitou o valor {valor_advinha} para ser verificado!') 
else:
    print(f'O valor da função advinha é {defina_valor_advinha} e, por isso você {adivinha(valor_advinha)}, pois digitou o valor {valor_advinha} para ser verificado!')


print()

######################################################
##  FIM DA FUNÇÃO BÔNUS
######################################################

