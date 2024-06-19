#Exemplo 4: organizando com o sorted
usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': ['Eu adoro cachorros', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []},
]

res = sorted(usuarios, key=lambda usuario: len(usuario['tweets']))  # organiza pelo  tweets
print('Organizado pelo tweets do menor para o maior')
print(res)

res = sorted(usuarios, key=lambda usuario: usuario['username'])
print('Organizado pelo nome menor para o maior')
print(res)