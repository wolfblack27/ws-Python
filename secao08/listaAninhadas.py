"""
listas aninhadas:
 . algumas linguagens tem estruturas de dados chamadas Arrays
    .unidade dimensional (arryas/vetores)
    .Multidimensionais (matrizes)
"""

# Exemplo 1:

#             0          1          2
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for valor in listas:
    for numero in valor:
        print(numero)
