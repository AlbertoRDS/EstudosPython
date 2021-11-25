#a = 10
#b = 5

a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor: '))

print(type(a))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#print('soma: {soma}. \nsubtracao:  {subtracao}'.format(soma=soma,subtracao=subtracao))


print('soma: {}'.format(soma))
print('soma: ' + str(soma))
print('subtracao: '+ str(subtracao))
print('multiplicacao: '+ str(multiplicacao))
print('divisao: ' + str(divisao))
print('resto: ' + str(resto))