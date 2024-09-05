
# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número 
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
#  A saída deve ser conforme o exemplo abaixo:

# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

##############################################################################################
print()
numero = int(input('Numero Inteiro de 0 à 10:   '))

while not( numero in range(11)):
    print(''' VALOR INVÁLIDO !!!
    
    ''')

    numero = int(input('Numero Inteiro de 0 à 10: '))

else:
    print(f'''    --------------------------    
    |      TABUADA DE {numero}      
    --------------------------''')
    for tabuada in range(11):
            print(f'''    |    {numero}    x   {tabuada}  =   {numero * tabuada}''')  
    