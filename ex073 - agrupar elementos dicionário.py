# Groupby

from itertools import groupby

alunos = [
    {'nome':'Eduardo'  , 'nota': 'A'},
    {'nome':'Fernando' , 'nota': 'B'},
    {'nome':'Leonardo' , 'nota': 'C'},
    {'nome':'Ricardo'  , 'nota': 'D'},
    {'nome':'Cleiton'  , 'nota': 'E'},
    {'nome':'Marcio'   , 'nota': 'D'},
    {'nome':'Daniel'   , 'nota': 'F'},
    {'nome':'Marcelo'  , 'nota': 'B'},
    {'nome':'João'     , 'nota': 'C'},
]

print(alunos)
print('-='*30)

alunos_agrupados = groupby(alunos, lambda item:item['nota'])
print(dict(alunos_agrupados))
print('-='*30)

