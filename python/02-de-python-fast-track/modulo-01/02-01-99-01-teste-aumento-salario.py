
# 99.01. Programa teste de aumento de salario
print ()
salario_atual = float(input('Salário atual: '))
tarifa_antiga = salario_atual / 168
percentual_aumento_inteiro = float(input('Percentual de aumento: '))
percentual_aumento = percentual_aumento_inteiro / 100

valor_aumento = salario_atual * percentual_aumento
salario_novo = salario_atual + valor_aumento
tarifa_nova = salario_novo / 168

print (f'''
    O salário atual é de R$ {salario_atual:.2f}
    O % de aumento a ser aplicado é de {percentual_aumento:.2f}, o que equivale à {percentual_aumento_inteiro:.1f}% 
    O valor a ser acrescido ao salário atual é de R$ {valor_aumento:.2f}
    O seu novo salário passa a ser de R$ {salario_novo:.2f}
    Onde a sua tarifa antiga, na base de horas 168, era de R$ {tarifa_antiga:.4f}
    E sua tarifa nova, na base de horas 168, passa a ser de R$ {tarifa_nova:.4f}
''')
