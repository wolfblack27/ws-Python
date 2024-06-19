"""
Pratica03
    Neste exemplo vamos utilizar> MAP, FILTER, REDUCE

Exercicios:

# Exercício 1 - Utilize map para imprimir o quadrado dos números abaixo com 3 casas decimais.
nums_float = [5.45, 2.57, 6.85, 9.77, 1.75, 8.88, 4.59]
res = map(lambda valor: round(valor ** 2, 3), nums_float)
print(list(res))


# Exercício 3 - Utilize filter para imprimir na tela nomes com menos de 5 letras
nomes = ["Caio", "Pedro", "José", "Maria", "Fernando"]
res = filter(lambda nome: len(nome) < 5, nomes)
print(list(res))



# Exercício 4 - Utilize map para mudar as letras abaixo. Se for minúscula deve retornar maiúscula e vice-versa
letras = ['a', 'b', 'C', 'd', 'E', 'F', 'g']
res = map(lambda letra: letra.upper() if letra == letra.lower() else letra.lower(), letras)
print(list(res))



# Exercício 5 - Utilize map com a lista de letras do exercíco anterior
# para retornar uma lista de tuplas com as letras em maiúsculas e minúsculas. Ex.: 'a' -> ('A', 'a')
letras = ['a', 'b', 'C', 'd', 'E', 'F', 'g']
res = map(lambda letra: (letra.upper(), letra.lower()), letras)
print(list(res))


# Exercício 7 - Utilize filter para imprimir na tela apenas os números positivos da lista abaixo
numeros = [5, -10, 55, 23, -16, -47, 20, -12]
res = filter(lambda valor: valor > 0, numeros)
print(list(res))



#Exemplo 9: Ordenando dicionario com sorted(que aplica filter)
from operator import itemgetter
meu_dicionario = {'b': 1, 'a': 2, 'c': 0}
dicionario_ordenado = sorted(meu_dicionario.items(), key=itemgetter(1))
print(dicionario_ordenado)


# Exercicio 8 - Utilizar map para plicar aumento em valores maiores de 6000
precos_produtos = [
    5000,
    9000,
    2000,
    15000
]

res = map(lambda valor: valor * 1.1 if valor > 6000 else valor, precos_produtos)
print(list(res))


"""
palavra = input('Palavra')
palavra = list(palavra.upper())
velha = ['_' for i in range(0, len(palavra))]
opc = 'S'
i = 0


def palpite_letra(letra):

    if letra in palavra:
        for i in range(0, len(palavra)):
            if letra == palavra[i]:
                velha[i] = letra
        print(velha)
    else:
        print('Letra errada')


while opc == 'S' :
    palpite = input('Digite letra palpite').upper()
    palpite_letra(palpite)
    opc = input('Deseja continuar (S)-> sim / (SAIR)-> qualquer letra').upper()
