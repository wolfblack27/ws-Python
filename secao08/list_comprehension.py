"""
Noção: List comprehension tem a finalidade de criar novas listas a partir de outro iteravel

Sintaxe da list comprehension
[dado for dado in iteravel]


#exemplo1 - neste exemplo pegamos cada elemento da lista numeros e multiplicamos por 10
numeros = [1,2,3,4,5]
res = [numero*10 for numero in numeros]
print(res)



#exemplo2 - Passamos a operação de cada numero para uma função. Vamos elevar cada element o ao quadrado
numeros = [1,2,3,4,5]

def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]
print(res)



#exemplo3 - Podemos trabalhar da mesma forma com string
nome = 'Thiago Ventura'

res = [letra.upper() for letra in nome]
print(res)



def media(m):
    if m >= 7:
        return 'Passou'

    elif 7 > m > 0:
        return 'Recuperacao'
    else:
        return 'Reprovado'


medias = [7, 5, 8, 2, 0]
res = [media(m) for m in medias]
print(res)


"""

veterinarios = [
    {'nome': "Thiago", "id": 1, "hora": "10:30"},
    {'nome': "Fernanda", "id": 3, "hora": "9:30"},
    {'nome': "Thiago", "id": 1, "hora": "5:30"},
    {'nome': "Marisa", "id": 2, "hora": "10:30"},
    {'nome': "Marisa", "id": 2, "hora": "11:40"},
    {'nome': "Fernanda", "id": 3, "hora": "10:30"},
    {'nome': "Thiago", "id": 1, "hora": "10:30"}
]

res = filter(lambda veterinario: veterinario.get('id') == 1, veterinarios)
thiago = [veterinario for veterinario in veterinarios if veterinario.get('id') == 1]
print(thiago)
print(list(res))
