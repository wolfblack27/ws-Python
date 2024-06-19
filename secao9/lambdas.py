""""utilizando Lambdas

 Expressoes lambdas: são funções sem nome,ou seja, funções anonimas


 #Função tipica em python

def funcao(x):
    return 3 * x + 1


"
#Exemplo1 funcao lambda

resultado = lambda x: 3 * x + 1
print(resultado(4))



#Exemplo2:Recebendo multiparametros

nome_completo = lambda nome, sobrenome: f'{nome.strip().title()} {sobrenome.strip().title()}'

print(nome_completo('thiago', 'Ventura'))


#Exemnplo3: ordenar pelo sobrenome

autores = ['Issac Asimov', 'Ray Brabury', 'Robert Heinlein', 'Arthur C Clarke', 'Frank Herbet',
           'Orson Scoth Card', 'Douglas Adans', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

indices_autores = {i+1: autores[i] for i in range(0, len(autores))}
print(indices_autores)



#Exemplo4: Retornando função lambda

def geradora_de_funcao(a, b, c):
    return lambda x: a * x ** 2 + b + c


print(geradora_de_funcao(a=2, b=3, c=-5)(x=0)) #Podemos passar os parametros de lambda junto com a função

"""



