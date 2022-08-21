salario = float(input('Informe seu salário atual: '))
#condições, ex: se salario menor que 500 aprenas 15% de acrescimo
if salario < 500:
    salario = salario + (salario * 15/100)
elif salario < 1000:
    salario = salario + (salario * 10/100)
else:
    salario = salario + (salario * 5/100)
print('Salário Reajustado: ', salario)#printa o salario ja reajustado

