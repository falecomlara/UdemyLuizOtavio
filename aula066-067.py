carrinho =[]
carrinho.append(('Camisa 1', 30))
carrinho.append(('Camisa 2', 20))
carrinho.append(('Camisa 3', 50))

#print(carrinho)

soma=float(0)
for c,v in carrinho:
    print(f'O produto {c} adicionado. Valor: {v}')
    soma+=v
print(f'Valor total: {soma}')

#Outro modo de fazer essa soma
total = sum([float(y) for x,y in carrinho])
print(f'Valor total: {total}')