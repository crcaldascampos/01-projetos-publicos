
###################################################################
##  BLOCO DE IMPORTAÇÃO DAS BIBLIOTECAS INTERNAS DO PYTHON
###################################################################
import pprint       # 01
import string       # 02
import re           # 03- REGULAR EXPRESSION: usado para encontrar padrões: CPF, CNPJ, CELULAR, E-MAIL, ect... APROFUNDAR !
import unicodedata  # 04
import math         # 05
import random       # 06



###################################################################
##  BLOCO DE VARIÁVEIS
###################################################################
varPrint                  =   {'a':2, 'b':3}    # 01
varStringDigits           =   '2'               # 02
varStringPunctuation01    =   '2'               # 03
varStringPunctuation02    =   '#'               # 03



###################################################################
##  BLOCO DO CÓDIGO
###################################################################

print(f'''
###################################################################
##  BIBLIOTECAS INTERNAS DO PYTHON
###################################################################
    
    01- PPRINT
        Essa biblioteca exibe a saída de forma diferente da convêncional. Normalmente o PRINT tem a saída no formato HORIZONTAL, como o
    exemplo abaixo:

        print( -[ 'a':2, 'b':3' ]- )    resultará em    {varPrint}

        Já o PPRINT exibe a saída do dado de forma VERTICAL, conforme o exemplo abaixo:

        pprint.pprint( -[ 'a0':2, 'b0':3, 'a1':2, 'b1':3, 'a2':2, 'b2':3, 'a3':2, 'b3':3, 'a4':2, 'b4':3, 'a5':2, 'b5':3 ]- )    
        resultará em      
''' )
pprint.pprint( {'a0':2, 'b0':3, 'a1':2, 'b1':3, 'a2':2, 'b2':3, 'a3':2, 'b3':3, 'a4':2, 'b4':3, 'a5':2, 'b5':3} )


print(f'''
    02- STRING
        Essa biblioteca tem diversas funções, como uppercas, lowercase, porém 2 verificações importantes são, para saber 
    se a string é um dígito (STRING.DIGITS) e se é um caracter especial (STRING.PUNCTUATION).

        -------------------------
        02.01- STRING.DIGITS
            import string
            varStringDigits = {varStringDigits}
            varStringDigits in string.digits  retornará   {varStringDigits in string.digits}

        -------------------------
        02.02- STRING.PUNCTUATION
            import string
            varStringPunctuation01 = {varStringPunctuation01}
            varStringPunctuation01 in string.punctuation  retornará   {varStringPunctuation01 in string.punctuation}

            varStringPunctuation02 = {varStringPunctuation02}
            varStringPunctuation02 in string.punctuation    retornará   {varStringPunctuation02 in string.punctuation}
            OBS: print( string.punctuation )  retornará   {string.punctuation}

            
    03- RE ( REGULAR EXPRESSION )
        Usado para encontrar padrões: CPF, CNPJ, CELULAR, E-MAIL, ect... APROFUNDAR NO TEMA !
            import re

    
    04- UNICODEDATA
        Usado para trabalhar com UNICODE.   APROFUNDAR NO TEMA !
            import unicodedata

                
    05- MATH
        Possui algumas funções, por exemplo:

        -------------------------
        05.01- MATH.CEIL    => Arredonda o número INTEIRO para cima.
            import math
            print(math.ceil(5.8))   retornará   {math.ceil(5.8)}
        
        -------------------------
        05.02- MATH.FABS    =>  Retorna o valor ABSOLUTO, independente do sinal ( + / -).
            import math
            print(math.fabs(-7))    retornará   {math.fabs(-7)}

        -------------------------
        05.03- MATH.FACTORIAL(N)    =>  Retorna o N Fatorial como um número inteiro.
            import math
            print(mat.factorial(7)) retornará   {math.factorial(7)}

        -------------------------
        05.04- MATH.FLOOR    => Arredonda o número INTEIRO para baixo.
            import math
            print(math.floor(5.8))   retornará   {math.floor(5.8)}

        -------------------------
        05.05- MATH.SQRT    => Retorna a raiz quadrada de 1 valor passado por parâmetro, no formato float.
            import math
            print(math.sqrt(4))   retornará   {math.sqrt(4)}
    
            
    06. RANDOM, suas principais funções estão listadas abaixo. Mas antes devemos importar a sua BIBLIOTECA.
        import random

        -------------------------
        --Os 2 valores são INCLUSOS / CONSIDERADOS para a geração aleatória solicitada.
        06.01-  RANDOM.RANDINT(VALOR_INICIAL, VALOR_FINAL)
            import random
            print(random.randint(1,6))  retornará   {random.randint(1, 6)}

        -------------------------
        06.02- RANDOM.SEED  =>  Retornará um valor aleatório FIXO. O SEED tem a função de pegar a SEMENTE do intervalo, para que possa
    ser gerado um valor fixo a partir desse intervalo.
            import random
            random.seed(0)
            random.randint      retornará   {random.seed(0)} {random.randint(1,6)}




Continuar dos 05 minutos 30 segundos
''')
