"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar. Criando uma nova lista

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados



#Exemplo01

numeros=[6,1,8,2]
tuple_numeros=(6,1,8,2)
print(sorted(numeros))
print(sorted(tuple_numeros)) #mesmo recebendo uma tupla ele retorna a lista


#Exemplo02: ordena do maior para o menor
numeros = [6, 1, 8, 2]
print(sorted(numeros,reverse=True))




#Exemplo03: sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
#Ordena por tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))




"""


#Exemplo04: ordenando a mais tocada

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

#menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

#mais tocada para menos tocada

print(sorted(musicas,key=lambda musica: musica['tocou'],reverse=True))