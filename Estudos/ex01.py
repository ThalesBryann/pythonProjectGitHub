'''
horas = int(input('Informe as horas: '))
if horas <= 11:
    print('Bom dia')
elif horas <= 17:
    print('Boa tarde')
else:
    print('Boa noite')
'''  # Saudação Bom dia - Boa Tarde - Boa Noite


'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos  escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = str(input('Digite seu nome: '))
if len(nome) <= 4:
    print(f'Seu nome é curto, contém {len(nome)} letras ')
elif len(nome) <= 6:
    print(f'Seu nome é normal, contém {len(nome)} letras ')
else:
    print(f'Seu nome é muito grande, contém {len(nome)} letras ')
''' # Qtd de letras no nome


# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')

