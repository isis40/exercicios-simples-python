num1 = int(input('Qual o valor desejado?: '))
"""
for que irá de 1 até 10 (tabuada de 10) fazendo com que o codigo seja realizado varias vezes
com multiplos diferente. primeira vez: 1 x (num escrito) // segunda vez: 2 x (num escrito) 
fazendo assim a multiplicação
"""
for i in range(1, 11):
    print(num1, 'X', i, '=', (num1 * i))