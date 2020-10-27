from dados import produtos, pessoas, lista
from functools import reduce

# Com o FOR é um meio de obter a soma dos valores de uma lista
acumula = 0
for item in lista:
    acumula+=item
print(acumula)

# Porém com o método reduce você pode retornar com o resultado em 01 ou 02 linha(s).

soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(f'Soma de todos os valores da lista é: {soma_lista}') #retornou com a soma da lista

soma_precos = reduce (lambda acumulador, produto: produto['preco'] + acumulador, produtos, 0)
print(f'Soma de todos os preços é: {soma_precos}') #retornou com a soma dos produtos

soma_idades = reduce(lambda acumulador, pessoas:pessoas['idade'] + acumulador, pessoas, 0)
print(f'Soma de todas as idades é: {soma_idades}')
print()

print(f'Para que isso é útil? Bem, se você quiser saber a média de um conjunto de valores,\n'
      'primeiro você precisa saber a soma total do conjunto de valores.\n')

print(f'A média dos valores na lista é: {soma_lista / len(lista)}')
print(f'A média dos preços é: {soma_precos / len(produtos)}')
print(f'A médida das idades é: {soma_idades / len(pessoas)}')