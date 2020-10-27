
def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError as erro:
        print('Log: ', erro)
        raise

try:
    print(dividir(2,0))
except ZeroDivisionError as erro:
    print('Não é possível dividir por zero')