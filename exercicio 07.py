num1 = int(input('Digite o numero desejado: '))
num2 = 0
"""
for que percorrerá de 1 até o numero desejado usando uma variavel que
somará no final
"""
for i in range(1 , num1 + 1, 1):
    num2 += i
print('soma: ', num2)