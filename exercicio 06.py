""""
utilizando "i%7" pegara todo resto da divisao feita percorrida pelo for igual a zero sendo assim um multiplo
E "i%5" fará o mesmo porém diferente de zero ou seja não multiplos
o condicional IF faz questão de somente esses numeros serem impressos e o for percorre toda a array de numeros
""""
for i in range(5,101):
    if(i % 7 == 0 and i % 5 != 0):
        print(i)
