# Carregue o conjunto de dados chamado kc_house_data.csv do hd para a memória
# Dados em https://www.kaggle.com/harlfoxem/housesalesprediction?select=kc_house_data.csv


# função - read .csv()
# biblioteca - pandas
# Digitar no terminal pip install pandas caso não tenha instalado

import pandas as pd

data = pd.read_csv( 'datasets/kc_house_data.csv' )

# Mostre na tela as 5 primeiras linhas do conjunto de dados
#print(data.head())

# Mostre o número de colunas e o número de linhas do conjunto de dados
#print(data.shape)

# Mostre na tela o nome das colunas do conjunto de dados
#print(data.columns)

#Mostre na tela o conjunto de dados ordenados pela coluna price
#Para exibir apenas pelas colunas relevantes usar [['exemplo1', 'exemplo2']]
#print(data[['id','price']].sort_values('price'))

#Mostra na tela o conjunto de dados ordenados pela coluna price do maior para o menor
#print(data[['id','price']].sort_values('price', ascending=False))

#NOVAS PERGUNTAS DO CEO

#1-Quantas casas disponíveis para a compra?
print(data.shape)
print(len(data.id))
#   print(data)
#   R:21613

#2 - Quantos atributos as casas possuem?
#   R:21

#3 - Quais são os atributos das casas?
print(data.columns)
#   R:'id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#        'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#        'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#        'lat', 'long', 'sqft_living15', 'sqft_lot15'],

#4 - Qual a casa mais cara com o maio valor de venda?
#   print(data[['id', 'price']].sort_values('price', ascending=False))
#   R: Casa 6762700020, linha 7252

#5 - Qual a casa com o maior número de quartos?
#   print(data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False))
#   R: Casa 2402100895, linha 15870

#6 - Qual a soma de quartos do conjunto de dados?
print(sum(data.bedrooms))
#   R:72854

#7 - Quantas casas possuem 2 banheiros?
#   print(data[data['bathrooms']==2]['bathrooms'])
print(len(data[data['bathrooms']==2]))
#   R:1930

#8 - Qual o preço médio de todas as casas do conjunto de dados?
#   soma_preco = sum(data.price)
#   n_casas = len(data)
#   print(soma_preco/n_casas)
print(sum(data.price)/len(data))  #Conta direta
#   R: $540000,14

#9 - Qual o preço médio de casas com 2 banheiros?
#   casas_2_banheiros = data[data['bathrooms']==2]
#   soma_casas_2_banheiros = sum(casas_2_banheiros.price)
#   n_casas_2_banheiros = len(casas_2_banheiros)
#   print(soma_casas_2_banheiros/n_casas_2_banheiros)
print(sum(data[data["bathrooms"]==2].price)/len(data[data["bathrooms"]==2]))    #Conta direta
#   R: 457889,72

#10 - Qual o preço mínimo entre casas com 3 quartos?
#casas_3_quartos = data[]
print(data[data['bedrooms']==3][['bedrooms', 'price']].sort_values('price', ascending=False)) #visualizando
print(min(data[data["bedrooms"]==3].price))
#   R: 82000

#11 - Quantas casas possuem mais de 300 m2 na sala de estar?
print(data[data['sqft_living']>3229.17]['sqft_living'])
print(len(data[data["sqft_living"]>3229.17]))
#   R:2258

#12 - Quantas casas ten nais de 2 andares?
print(len(data[data['floors']>2]))
#   R:782

#13 - Quantas casas tem vista para o mar?
print(len(data[data['waterfront']==1]))
#   R:163

#14 - Das casas com vista para o mar, quantas têm 3 quartos?
casas_com_waterfront = data[data['waterfront']==1]
print(len(casas_com_waterfront[casas_com_waterfront["bedrooms"]==3]))
#   R: 64

#15 - Das Salas com mais de 300 m2 na salar de estar, quantas tem mais de 2 banheiros?
mansoes = data[data["sqft_living"]>3229.17]
print(len(mansoes[mansoes['bathrooms']>2]))
#   R: 2201
