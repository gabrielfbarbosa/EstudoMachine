import pandas as pd

uriF = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"

# Usualmente chamdo de dataFrame até pela documentação do Pandas
# Utilizando como nome de variavel = 'filme' para ser mais especifico sobre o que esta sendo recebido
# 'pd.read_cvs' recebe os dados dos filmes da URI (URL)
filmes = pd.read_csv(uriF)

# Imprime todas as linhas
# print(filmes)

# imprime so os 5 primeiro com .head
# print(filmes.head())

# pegando os nomes das colunas
# print(filmes.columns)

# Renomenado nome das colunas
filmes.columns = ['FilmeId', 'Titulo', 'Generos']
# print(filmes.head())

# acessando as notas
uriN = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv'
notas = pd.read_csv(uriN)
# print(notas.head())
notas.columns = ['UsuarioId', 'FilmeId', 'Nota', 'Momento']
# print(notas.head())

# Chamando de 'series' para trazer uma serie de valores
# print(notas['Nota'].head())

# Para trazer os unicos valores existentes da coluna nota
# print(notas["Nota"].unique())

# Saber a media entre os valores de nota
# print(notas['Nota'].mean())

# Saber o valor MINiMO entre os valores de nota
# print(notas['Nota'].min())

# Ter varias estatisticas do data frame notas
print(notas.describe())