"""
ZIP - Unidos iteráveis
ZIP_longest - Itertools
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados,cidades)
print(list(cidades_estados)) # como não tem mais elementos, ele elimina o valor sozinho

# Uma solução é importar o Itertools
from itertools import zip_longest
cidades_estados = zip_longest(estados, cidades)
print(list(cidades_estados))

