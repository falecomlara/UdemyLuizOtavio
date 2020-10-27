# Exception

from CursoEmVideo import verificaerro

try:
    print(a)
except NameError:
    print('Variável não definida')
    a=str(input('Insira um dado para a variavél: '))
except Exception as erro:
    print('Ocorreu um erro inesperado', erro)
except SyntaxError:
    print('Ocorrei um erro de sintaxe')
else:
    print('código executado com sucesso')
finally:
    print(a)

