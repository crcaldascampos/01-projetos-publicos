
#  01. Operadores matemáticos
#   01.01. soma ..................... +
#   01.02. subtração ................ -
#   01.03. multiplicação ............ *
#   01.04. potência ................. **
#   01.05. divisão .................. /
#   01.06. divisão de inteiros ...... //
#   01.07. resto da divisão ......... %

print(5 + 10)               # 01.01
print(5 - 10)               # 01.02
print(5 * 10)               # 01.03
print(5 ** 10)              # 01.04
print(5 / 10)               # 01.05
print(5 // 10)              # 01.06
print(5 % 10)               # 01.07



# 02. Operadores relativos
#   02.01. igual ..................... ==
#   02.02. diferente ................. !=
#   02.03. maior que ................. >
#   02.04. menor que ................. <
#   02.05. maior ou igual a .......... >=
#   02.06. menor ou igual a .......... <=

print(5 == 10)              # 02.01
print(5 != 10)              # 02.02
print(5 > 10)               # 02.03
print(5 < 10)               # 02.04
print(5 >= 10)              # 02.05
print(5 <= 10)              # 02.06



# 03. Operadores lógicos
#   03.01. não ..................... not
#   03.02. ou ...................... or
#   03.03. e ....................... and

print( not 10 > 5)          # 03.01
print( 10 > 5 or 10 < 5)    # 03.02
print( 10 > 5 and 10 < 5)   # 03.03



# 04. Verificar tipagem de alguma operação ou variável
print( type( 5 / 10))
print( type( 5 == 10))
print( type( 10 > 5 and 10 < 5))