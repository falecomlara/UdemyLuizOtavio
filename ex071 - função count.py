"""
Contadores - count
"""

from itertools import count
contador = count(0,1)
for c in contador:
    print(c)
    if c >= 10:
        break

# Ele é útil para adicionar um indice em uma lista
indice = count(0,1)
nomes = ['eduardo', 'maria', 'joao', 'ricardo', 'flávio']
lista = zip(indice, nomes)
print(list(lista))