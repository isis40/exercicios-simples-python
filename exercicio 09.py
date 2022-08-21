digitos = int(input('número: '))
contador = 0
"""
while que reduzira o numero até zero e adicionará ao contador cada vez que uma redução decimal for feita.
"""
while digitos != 0:
    digitos //= 10 #aproxima o numero da divisão para o inteiro mais prox
    contador += 1
print('Total de digitos: ', contador)#printa a contagem feita