"""
 List Comprehensions 2
 Podemos adicionar estruturas condicionais nas nossas listcomprehensions

#exemplo1 - Criando uma lista somente com numeros pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print(pares)
print(impares)



#exemplo2 - Usando if else

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

"""


def calculaImposto(valores: list, alicota: float) -> list:
    alicota = (alicota / 100) + 1
    return [valor * alicota for valor in valores]


print(calculaImposto([100, 280, 410], 92))
