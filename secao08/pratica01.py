""""
# Exercício  - Crie uma lista somente com pares a partir da  lista abaixo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [numero for numero in numeros if numero % 2 == 0]
print(res)



# Exercício 10 - Crie um dicionário a partir da lista abaixo, com a mesma chave e valor (exemplo: "x":"x")
estados = ['SP', 'RJ', 'BA']

res = {estados[i]: estados[i] for i in range(0, len(estados))}
res={estado: estado for estado in estados}
print(res)
"""

# Exercício 11 - Crie um dicionário com as chaves e valores abaixo e uuma lista com valores divididos.
keys = ['Inglês', 'Português', 'Matemática', 'Geografia']
values1 = [[7, 4, 9, 8], [5, 7, 10, 8], [8, 4, 7, 9]]
res = {chave: valor for (chave, valor) in zip(keys, values1)}
print(res)
#dividindo a nota por 2
list_poderada = [list(map(lambda v: v / 2, valor)) for valor in values1]
print(list_poderada)
dicionario_ponderado = {chave: valor for (chave, valor) in zip(keys, list_poderada)}
print(dicionario_ponderado)
