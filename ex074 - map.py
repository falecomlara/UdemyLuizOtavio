# USANDO A FUNÇÃO MAP
# Listar os produtos e aumentar os preços

from dados import pessoas, produtos, lista

def aumenta_preco(p):
    p['novo preco'] = p['preco']+round(p['preco']*0.10,2)
    return p

produtos = map(aumenta_preco, produtos)
for produtos in produtos:
    print(produtos)


"""
nova_lista = map(lambda x: x * 2, lista)
nova_lista2 = [x * 2 for x in lista]  # esse é um outro modo
print(lista)
print(nova_lista) #Volta como iterador. precisamos converter esta lista.
print()
print(list(nova_lista))
# outro modo de despacotar a lista, é:
print(nova_lista2)
"""

"""
novos_nomes = map(lambda p: p['nome'], pessoas)
for pessoas in novos_nomes:
    print(pessoas)
print('-='*30)
"""

