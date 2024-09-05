# --------------------------------------------------
# BIBLIOTECAS
# --------------------------------------------------
from datetime import datetime



# --------------------------------------------------
# LISTAS - TOLKIEN
# --------------------------------------------------
livros_tolkien = [
    'The Hobbit'
    , 'The Fellowship of the Ring'
    , 'The Two Towers'
    , 'The Return of the King'
    , 'The Silmarillion'
    , 'Unfinished Tales of Numenor and Middle-Earth'
    , 'The Children of Hurin'
    , 'Beren and Luthien'
]

anos_tolkien =[
    1937, 1954, 1954, 1955, 1977, 1980, 2007, 2017
]


# --------------------------------------------------
# LISTAS - LEWIS
# --------------------------------------------------
livros_lewis = [
    'The Lion, the Witch, and the Wardrobe'
    , 'Prince Caspian'
    , 'The Voyage of the Dawn Treader'
    , 'The Silver Chair'
    , 'The Horse and His Boy'
    , "The Magician's Nephew"
    , 'The Last Battle'
]

anos_lewis = [
    1950, 1951, 1952, 1953, 1954, 1955, 1956
]

# print (type (livros_tolkien))
# print(type(anos_tolkien))
# print(type(livros_lewis))
# print(type(anos_lewis))


# # --------------------------------------------------
# # ITERAÇÕES - FOR: NOME DO LIVRO
# # --------------------------------------------------
# for livro in livros_tolkien:
#     print(livro)


# # --------------------------------------------------
# # ITERAÇÕES - FOR: VINCULANDO LIVRO AO ANO TOLKIEN
# # --------------------------------------------------
# for index in range(len(livros_tolkien)):
#     print(livros_tolkien[index])
#     print(anos_tolkien[index])


# --------------------------------------------------
# CRIANDO DICIONÁRIO ATRAVÉS DAS ITERAÇÕES - FOR: VINCULANDO LIVRO AO ANO TOLKIEN
# --------------------------------------------------
dicionario_tolkien = {}
for index in range(len(livros_tolkien)):
    livro = { livros_tolkien[index] : anos_tolkien[index] }
    dicionario_tolkien.update(livro)

# print(dicionario_tolkien)


# --------------------------------------------------
# COMPREENSÃO DE DICIONÁRIO ATRAVÉS DAS ITERAÇÕES - FOR: VINCULANDO LIVRO AO ANO LEWIS
# --------------------------------------------------
# obs: aqui faz-se a diferença na hora de ler, dar manutenção e explicar o código
# --------------------------------------------------
dicionario_lewis = {
    livros_lewis[index] : anos_lewis[index] for index in range(len(livros_lewis))
}

# print(dicionario_lewis)



# --------------------------------------------------
# ARMAZENAMENTO DE DICIONÁRIOS
# --------------------------------------------------
# obs: aqui armazenamos os dicionários dentro de outro dicionário
# --------------------------------------------------
dicionario_livros = {
    'Tolkien'   :   dicionario_tolkien
    , 'Lewis' :   dicionario_lewis
}

print(dicionario_livros)


# --------------------------------------------------
# LIST COMPREHENSION - IDADE DOS LIVROS
# --------------------------------------------------
# obs: aqui armazenamos em uma lista os anos dos livros através da compreensão da lista
# --------------------------------------------------
ano_atual = datetime.now().year
idade_livro = [ano_atual - ano for ano in anos_tolkien]
print(idade_livro)