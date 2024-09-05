
# Link da lista de exercícios:  https://wiki.python.org.br/EstruturaDeDecisao

# 05.05. Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada pelo aluno e apresentar:
    #     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    #     A mensagem "Reprovado", se a média for menor do que sete;
    #     A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota01 = float( input('1ª Nota: '))
nota02 = float( input('2ª Nota: '))
media = (nota01 + nota02) / 2

print(f'''
    A 1ª nota foi ( {nota01} ), já a 2ª foi ( {nota02} ).
    Resultando na média ( {media} )!
''')

if media == 10:
    print('''
        Desa forma você está APROVADO COM DISTINÇÃO !
    ''')
elif media >= 7:
    print(f'''
        Dessa forma você está APROVADO !
    ''')
else:
    print(f'''
        Dessa forma você está REPROVADO !
    ''')