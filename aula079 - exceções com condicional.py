def converte_valor(valor):
    try:
        valor = int(valor)
        print('Variável convertido para INTEIRO')
        return valor
    except ValueError:
        try:
            valor = float(valor)
            print('Variável convertido para FLOAT')
            return valor
        except ValueError:
            pass




numero = str(input('Digite um valor: ')).strip()
converte_valor(numero)
print(numero)
