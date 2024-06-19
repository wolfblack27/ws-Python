"""
Dictionary Comprenhension

Criar:
lista=[1,2,3,4]
tupla =(1,2,3,4)
dicionario={'a':1,'b':2,'c':3, 'd':4}

#Sintase para dictinary comprenhension
{chave:valor for in iteravel}

Exemplos:


#exemplo1: elevar os valores ao quadrado
#print(numeros.items())
#a função numero.items devolve uma lista de tuplas: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# e é sobre ela que iremos iterar

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)


#exemplo2: gerando a partir de uma lista

numeros = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)



#exemplo3: criando um dicionario a partir de duas variaveis diferentes
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)


#exemplo3: Usando condicional:

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

"""