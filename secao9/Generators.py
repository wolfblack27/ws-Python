"""
Generators:
        São tuples comprenhensions

"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

#Exemplo01: Gerando tuple

res = (dado[0] == "C" for dado in nomes)
print(tuple(res))
