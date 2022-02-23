# def mais_um_ano(idade):
#     print('Dentro: ')
#     idade += 3
#
#
# idd = 37
# mais_um_ano(idd)
# print(idd)
# print(mais_um_ano(idd))

filme1 = "Matrix"
filme2 = "Homem de ferro"
filme3 = "Dr. Strange"
filmes = ["Matrix 3",  "Homem de ferro 3", "Dr. Strange 2", "Vingadores"]
# filmes = [filme1, filme2, filme3]
# print(filmes)


def imprime_filmes(filmes):
    print('Lista de filmes:')
    print(filmes)


imprime_filmes(filmes)

print('\n\033[1;92mPegando o ultimo filme da lista \033[m')
print(filmes[-1])

print('\n\033[1;92mPegando a partir do segundo elemento pra frente \033[m')
print(filmes[1:])

print('\n\033[1;92mPegando a partir do penultimo elemento pra o fim \033[m')
print(filmes[-2:])

print('\n\033[1;92mColocando filmes em "coluna": \033[m')
for movie in filmes:
    print(movie)

print('\n\033[1;92mImprimindo filmes com a função: \033[m')


def imprime_filmes (list_filmes):
    print('Lista de filmes: ')
    for filme in list_filmes:
        print(filme)


imprime_filmes(filmes)

print('\n\033[1;92mArmazenando dados: \033[m')

dados = {
    "nome": "Gabriel",
    "idade": 28,
    "esporte": "Basquete",
         }

print(dados)
