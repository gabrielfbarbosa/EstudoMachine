from sklearn.svm import LinearSVC

# Pelo longo ?
# Perna curta?
# faz auau ?
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0]  # 1 porco 0 cachorro

# 'modelo' é como um cerebro vazio que sera treinado
# modelo = LinearSVC()

# '.fit' faz o 'modelo' ser é treinado com os dados.
# modelo.fit(treino_x, treino_y)

# Apos modelo treinado, testando com modelo 'misterioso'
# animal_misterioso = [1, 1, 1]

# O 'predict' recebe uma lista de animais por isso o '[]'
# if modelo.predict([animal_misterioso]) == 0:
#     print('Cachorro')
# else:
#     print('Porco')
# print('Resposta da maquina: ', modelo.predict([animal_misterioso]))

# misterio1 = [1, 1, 1]
# misterio2 = [1, 1, 0]
# misterio3 = [0, 1, 1]
#
# teste_x = [misterio1, misterio2, misterio3]
# teste_y = [0, 1, 1]
#
# previsoes = modelo.predict(teste_x)
#
# print('Resposta: ', previsoes)

# for r in previsoes:
#     if r == 0:
#         print(r, ' = Cachorro')
#     else:
#         print(r, ' = Porco')
#     print('=*'*20)

# Taxa de acerto 'accuracy' o quão certo a maquina esta
from sklearn.metrics import accuracy_score
import pandas as pd

# print('Taxa de acerto: ', accuracy_score(teste_y, previsoes))

uriS = 'https://raw.githubusercontent.com/guilhermesilveira/machine-learning/master/capitulo2/acesso.csv'
dados = pd.read_csv(uriS)
# print(dados.head())

x = dados[["home", " como_funciona", " contato"]]
y = dados[' comprou']

# print('\n', '-*'*20)
# print(x.head())
# print('\n', '-*'*20)
# print(y.head())

from sklearn.model_selection import train_test_split

modelo2 = LinearSVC()
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y)

modelo2.fit(treino_x, treino_y)

previsao = modelo2.predict(teste_x)
print(accuracy_score(teste_y, previsao) * 100)

