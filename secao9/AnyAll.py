""""
Any All

all()-> Retorna true se todos os elementos do iteravel são verdadeiros, ou se o iteravel esta vazio

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

#Exemplo1: Testando se todos são verdadeiros

res = all([0, 1, 2, 3, 4])  #Retorna false, pois tem o 0(false)
res = all([1, 2, 3, 4])  #Retorna true
res = all([0, 1, 2, 3, ])  #Retorna false, pois tem espaço vazio
print(res)


#Exemplo2:Verifica se a primeira letra é C, usando junto com comprenhensions
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
res = all([nome[0] == 'C' for nome in nomes]) #Usando comprehension
res = all(filter(lambda nome: nome[0] == "C", nomes)) #usando filter
print(res)


"""



print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))


print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))