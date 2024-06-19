"""
Pratica02
    Neste exemplo vamos usar map para converter dolar em reais

"""

cotacao = 5.42
valores_dolar = [
    {'moeda': 'BTC', 'preco': 66510},
    {'moeda': 'ETH', 'preco': 3519},
    {'moeda': 'CAKE', 'preco': 2.47},
    {'moeda': 'ADA', 'preco': 0.40}
]

valores_reais = list(map(lambda valor: valor['preco'] * cotacao, valores_dolar))
dicionario_valores_reais = {valores_dolar[i]['moeda']: valores_reais[i] for i in range(len(valores_dolar))}

print(dicionario_valores_reais)
