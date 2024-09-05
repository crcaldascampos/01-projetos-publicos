################################################
#          PDE BIBLIOTECAS HANDS ON            #
################################################
#   CRIANDO 1 PASTA CHAMADA DE  geometria   PARA INCLUIR NELA OS ARQUIVOS:  
    # __init__.py       PARA INDICAR QUE ESSA PASTA É UMA BIBLIOTECA
    # areas.py          COM AS FUNÇÕES DAS ÁREAS DO: TRIÂNGULO, QUADRADO E RETÂNGULO


#   01- IMPORTANDO A BIBLIOTECA TODA CRIADA PARA DENTRO DESSE ARQUIVO
import  geometria.areas
# print( geometria )
# print( geometria.areas )
print( geometria.areas.area_quadrado (4) )
print( geometria.areas.area_triangulo (2, 4) )
print( geometria.areas.area_retangulo (2, 4) )


#   02- IMPORTANDO APENAS O CAPÍTULO NECESSÁRIO DA BIBLIOTECA PARA SUA UTILIZAÇÃO, VINDO DA BIBLIOTECA   geometria  .
from geometria.areas    import  area_quadrado
print(area_quadrado(2))


#   03- PASSANDO ALIAS
import geometria.areas  as  ars
print( ars.area_quadrado( 5 ) )

from geometria.areas    import  area_quadrado   as  arq
print( arq(2) )