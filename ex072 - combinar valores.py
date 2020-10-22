"""
COMBINATIONS - Combinar valores (ordem não importa)
PERMUTATIONS - Combinar valores (ordem importa)
PRODUCTS     - Obter todas as combinações possíveis, repetindo o mesmo valor
"""
from itertools import combinations, permutations, product

nomes = ['eduardo', 'maria', 'joao', 'ricardo', 'flávio']
for c in combinations(nomes,2):
    print(c)
print('-='*20)

for c in permutations(nomes, 2):
    print(c)
print('-='*20)

for c in product(nomes, repeat=2):
    print(c)
print('-='*20)
