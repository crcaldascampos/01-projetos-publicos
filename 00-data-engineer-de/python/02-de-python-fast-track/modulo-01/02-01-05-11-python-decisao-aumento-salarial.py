
# Link da lista de exercícios:  https://wiki.python.org.br/EstruturaDeDecisao

# 05.11. As Organizações Tabajara resolveram dar um aumento de salário aos seus
#  colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo 
# o seguinte critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento. 

print ()
salario_atual = float(input('Salário atual: '))
tarifa_antiga = salario_atual / 168

if (salario_atual <= 280):
    salario_novo = salario_atual * 1.2
elif (salario_atual <= 700): #elif (salario_atual > 280) and (salario_atual <= 700):
    salario_novo = salario_atual * 1.15
elif (salario_atual <= 1500):
    salario_novo = salario_atual * 1.1
else:
    salario_novo = salario_atual * 1.05

valor_aumento = salario_novo - salario_atual
percentual_aumento = (salario_novo / salario_atual)
percentual_aumento_inteiro = (percentual_aumento * 100) - 100
tarifa_nova = salario_novo / 168

print (f'''
    O salário atual é de R$ {salario_atual:.2f}
    O % a ser aplicado é de {percentual_aumento:.2f}, o que equivale ao aumento de {percentual_aumento_inteiro:.1f}% 
    O valor a ser acrescido ao salário atual é de R$ {valor_aumento:.2f}
    O seu novo salário passa a ser de R$ {salario_novo:.2f}
    Onde a sua tarifa antiga, na base de horas 168, era de R$ {tarifa_antiga:.4f}
    E sua tarifa nova, na base de horas 168, passa ser de R$ {tarifa_nova:.4f}
''')
