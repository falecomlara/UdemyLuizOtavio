# Módulos padrão do Python
# Módulos são arquivos .py (que contém código Python)
# docs.python.org/3/py-modindex.html


# Exemplo de várias maneiras diferentes, importando o módulo
import sys
print(sys.platform)

from sys import platform
print(platform)

from sys import platform as qualquernome
print(qualquernome)

