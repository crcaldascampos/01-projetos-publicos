##############################
# CRIAÇÃO DE FUNÇÕES
##############################

print('''
##############################
# CRIAÇÃO DE FUNÇÕES
##############################
==============================================================
    01- PARÂMETROS À:
        01.01- ESQUERDA são OBRIGATÓRIOS, estes NÃO POSSUEM sinal de =
        01.02- DIREITA são OPCIONAIS, eles POSSUEM o sinal de = e, caso nenhum valor for passado, eles 
            assumirão um valor PADRÃO / DEFAULT, passado explicitamente na CRIAÇÃO da FUNÇÃO.

==============================================================             
    02- ESTRUTURA DA FUNÇÃO
        
        def nome_funcao(parametro01, parametro02):
            lógica_negócio
        return  #opcional
        # return None #por padrão

==============================================================          
    03- CRIANDO A 1ª FUNÇÃO DE SOMA
        
        def soma(p1, p2):
            # print (p1 + p2) # Está comentado
            return (p1 + p2)
            
    
    OBS 03.01: Quando passado o PRINT ao tentar referenciar a saída, não nos retornará nada (NONE)!
    
    OBS 03.02: Já com o RETURN qualquer operação executada na FUNÇÃO carregará o valor, quando passarmos
      a FUNÇÃO em questão em alguma parte do código!
-----------------------------------------------------------------
''')

# 03- Criando a 1ª função de soma
def soma(
    p1= int(input('        1º Número (p1): '))
    , p2= int(input('      + 2º Número (p2): '))
):
    return(
        p1 
        + p2
    )

print(f'''-----------------------------------------------------------------
    Dessa forma o TOTAL entre os 2 Números / Parâmetros é de {soma()}.
''')
    