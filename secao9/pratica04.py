texto_analise = """Adoniran era filho de Francesco Fernando Rubinato e Emma Ricchini,
 imigrantes italianos da comuna de Cavarzere, província de Veneza. Seus avós paternos eram Angelo Rubinato e Anna Manfrinato,
  e os maternos, Francesco Ricchini e Antonia Freddo. Seus pais casaram-se em Cavarzere em 23 de maio de 1895, 
  desembarcaram em Santos em 15 de setembro de 1895, passaram pela Hospedaria dos Imigrantes e foram trabalhar nas 
  lavouras do município de Tietê. Sua mãe morreu em 1939 e seu pai em 1943""".upper()


list_text = texto_analise.split()
list_text = list(filter(None, list_text))
print(list_text)

dados_comecados_A = filter(lambda dado: dado[0] == "F", list_text)
print(list(dados_comecados_A))
