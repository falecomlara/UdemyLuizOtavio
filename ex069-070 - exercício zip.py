"""
Duas lista, some os valores
"""

lista_a = [1,2,3,4,5,6,7,8,9]
lista_b = [1,2,3,4]

lista_soma = [x + y for x, y in zip(lista_a,lista_b)]
print(list(lista_soma))


