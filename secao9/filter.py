"""
Filter

Filter: serve para filtrar dados de uma determinada coleção
    Ela recebe dois parametros (função e iteravel)
    E somente retorna true ou false para integrar o dado



#Exemplo de media sem filter
valores = 1, 2, 3, 4, 5, 6

media = (sum(valores)/len(valores))
print(media)




#Exemplo2: Media e filtrando com o Filter


#biblioteca para trabalhar com dados
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)
res = list(filter(lambda x: x > media, dados))

print(res)




#Exemplo3: Eliminando dados faltantes com filter e none

paises = ['', 'Argentina', '', 'Brasil', 'chile', '', 'Colombia', 'Equador', '', '', 'Venezuela']

#1 forma
#res = filter(None, paises) #None retira os espaços vazios

#2Forma
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))


#Exemplo 4: Filtrando dicionario
usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': ['Eu adoro cachorros', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []},
]

res = filter(lambda usuario: len(usuario['tweets']) == 0, usuarios)  #filtrando somente os que não tem tweet
print(list(res))



"""

