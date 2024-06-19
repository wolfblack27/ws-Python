""""
Map:
    Map nos auxilia a fazer mapeamento de valores para função




#Exemplo1: Forma sem Map tradicional
import math
def area(r):
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []

for raio in raios:
    areas.append(area(raio))

print(areas)





#Exemplo 2: Usando Map para os raios

import math


def area(r):
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios) #recebe valores do tipo 'class map'

print(list(areas))




#Exemplo 3: Map com lambda

import math

raios = [2, 5, 7.1, 0.3, 10, 44]
print(list(map(lambda r: math.pi * (r ** 2), raios)))





#Exemplo 4: Recebendo parametros do tipo list[tuple]

cidades = [('Berlin', 29), ('Tokio', 27), ('Londres', 22)]
c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

"""
