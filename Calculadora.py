# calculadora simples

numero1 = 0
numero2 = 0
resultado = 0
operacao= ''

numero1 = int(input('Digite o numerop 1:'))
operacao = input('Digite a operacao:')
numero2 = int(input('digite o numero2:'))

if operacao =='+':
    resultado = numero1 + numero2
elif operacao =='-':
    resultado = numero1 - numero2
elif operacao =='/':
    resultado = numero1 - numero2
elif operacao =='*':
    resultado = numero1 - numero2
else:
    resultado = 'Operação inválida'

print (numero1,operacao,numero2,'=',resultado )