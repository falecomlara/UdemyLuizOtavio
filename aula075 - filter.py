from dados import produtos, pessoas, lista

print(lista)
nova_lista = filter(lambda x: x >5, lista) #Com o filte + Lambda, conseguimos filtrar uma lista
print(list(nova_lista))
print()

novos_dados = filter(lambda p: p['preco'] > 10, produtos)
print(list(novos_dados))
print()

nova_idade = filter(lambda i: i['idade'] > 40, pessoas)
print(list(nova_idade))
print()

