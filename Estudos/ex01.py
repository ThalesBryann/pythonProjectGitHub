'''
horas = int(input('Informe as horas: '))
if horas <= 11:
    print('Bom dia')
elif horas <= 17:
    print('Boa tarde')
else:
    print('Boa noite')
'''  # Saudação Bom dia - Boa Tarde - Boa Noite

'''# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')''' #Número par ou ímpar

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

'''
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# #casa, o programa vai perguntar o valor da casa, o sário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do #salário ou então o empréstimo será negado.

valorDoImovel = float(input("Qual o valor do Imóvel? "))
salario = float(input("Digite seu salário: "))
anos = int(input("Quantos anos de financiamento? "))

salariodividido = salario * 0.3
prestação = valorDoImovel / (anos * 12)

if prestação <= salariodividido:
    print(f'Seu financiamento foi aprovado e suas parcelas serão de R${prestação:.2f} em {prestação} parcelas.')

else:
    print(f'empréstimo negado. O valor das parcelas é de R${prestação:.2f}, o que excede', end=' ')
    print(f'o limite de 30% do salário, que é R${salariodividido:.2f}.')
''' # ex036 Aprovando empréstimo

'''
num = int(input('Digite um número inteiro: '))
print(Escolha uma das bases para conversão: 
[ 1 ] converter para BINÀRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL)
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÀRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
''' # ex037 conversor de bases numéricas

'''Desafio 38 
Escreva um programa que leia dois números inteiros e compare-os, mostrando 
na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('\033[7;40m O primeiro valor é maior\033[m')
elif n2 > n1:
    print('\033[7;40mO O segundo valor é maior\033[m')
else:
    print('\033[7;40m Os dois valores são iguais!\033[m')
''' # ex038 qual número é maior

'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo 
com a idade: 
-Se ele ainda vai se alistar ao serviço militar
-se é a hora de se alistar
-Se já passou do tempo do alistamento.
O programa também deverá mostrar o tempo que falta ou que passou do prazo. 


from datetime import date

print(f'\033[7;40m{"-"*4} Alistamento para Forças Armadas {"-"*4}\033[m')

try:
    ano_nascimento = int(input('Informe seu ano de nascimento: '))
    ano_atual = date.today().year

    if ano_nascimento > ano_atual:
        print('Ano de nascimento inválido. Por favor, insira um ano antes do ano atual.')
    else:
        idade_alistamento = ano_atual - ano_nascimento

        if idade_alistamento == 18:
            print(f'Você tem {idade_alistamento} anos. Procure um SAC para fazer seu alistamento!')
        elif idade_alistamento < 18:
            anos_que_faltam = 18 - idade_alistamento
            print(f'Você tem {idade_alistamento} anos. Ainda faltam {anos_que_faltam} anos para poder se alistar.')
            ano = ano_atual + anos_que_faltam
            print(f'Seu alistamento será em {ano}')
        elif idade_alistamento > 18:
            saldo = idade_alistamento - 18
            print(f'Você já deveria ter se alistado há {saldo} anos!')
            print(f'Seu alistamento foi em {ano_atual - saldo}')
except ValueError:
    print("Entrada inválida. Por favor, insira um ano de nascimento válido (por exemplo, 2000).")''' # ex039 alistamento militar

'''Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
-Média abaixo de 5.0 REPROVADO
-Média entre 5.0 e 6.9 recuperação
-Média 7.0 ou superior APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

if média < 5:
    print(f'Sua nota foi {média} e você foi Reprovado')
elif média <= 6.9:
    print(f'Sua nota foi {média} e você está na Recuperação')
else:
    print(f'Sua nota foi {média} e você foi APROVADO')
'''  # ex040 Aquele

'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria 
de acordo com a idade: 
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: Sênio
- Acima: Master


try:
    idade = int(input('Informe sua idade: '))

    if idade <= 0:
        print('Informe uma idade válida!')
    elif idade <= 9:
        print('Sua categoria é Mirim')
    elif idade <= 14:
        print('Sua categoria é Infantil')
    elif idade <= 19:
        print('Sua categoria é JUNIOR')
    elif idade <= 20:
        print('Sua categoria é SÊNIO')
    elif idade > 20:
        print('Sua categoria é MASTER')
except ValueError:
    print("Informe uma idade válida!")
''' # ex41 Classificando atletas

#ex042

'''
print(f'\033[7;40m{"-"*4}Vamos calcular seu IMC{"-"*4}\033[m ')

try:
    peso = int(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc = peso / (altura ** 2)
    print(f'Seu IMC é {imc:.1f} ')

    if imc < 18.5:
        print('Seu IMC está abaixo do peso')
    elif imc <= 25:
        print('Peso ideal')
    elif imc <= 30:
        print('Sobrepeso')
    elif imc <= 40:
        print('Obesidade')
    else:
        print('Obesidade mórbida,cuidado')
except ValueError:
    print('Informe seu peso e altura corretos.')

''' # ex042 Indice de Massa corporal

'''

print('\033[7;40m---Caixa---\033[m')

try:
    valorProduto = float(input('Preço das compras: '))
    print(FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão)
    opção = int(input('Qual é a opção? '))
    if opção == 1:
        print(f'Sua compra de {valorProduto}  vai custar {valorProduto - (valorProduto * 0.10)} no final.')
    elif opção == 2:
        print(f'Sua compra de {valorProduto} vai custar {valorProduto - (valorProduto * 0.05)} no final.')
    elif opção == 3:
        print(f'Sua compra será parcelada em 2x de {valorProduto / 2} sem juros')
    elif opção == 4:
        parcelas = int(input('Quantas parcelas? '))
        print(f'Sua compra será parcelada em {parcelas}x de {(valorProduto + (valorProduto * 0.20)) / parcelas:.2f} com juros')
        print(f'Sua compra de {valorProduto} vai custar {valorProduto + (valorProduto * 0.20):.2f} no final.')
    else:
        print(f'Opção de pagamento inválida, tente novamente!')
        print(f'Sua compra de R${valorProduto:.2f} vai custar R${valorProduto} no final.')

except ValueError:
    print('Insira um valor e forma de pagamento válido')

''' # ex044 Gerenciador de pagamentos

'''
import random

print(Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura)

itens = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)
aleatorio = itens[computador]
opcao = int(input('Escolha uma opção: '))

if opcao >= 1 and opcao <= 3:
    escolha_usuario = itens[opcao - 1]
    print(f'Você escolheu: {escolha_usuario}')
    print(f'O computador escolheu: {aleatorio}')

    if escolha_usuario == aleatorio:
        print('Empate!')
    elif (escolha_usuario == 'Pedra' and aleatorio == 'Tesoura') or \
         (escolha_usuario == 'Papel' and aleatorio == 'Pedra') or \
         (escolha_usuario == 'Tesoura' and aleatorio == 'Papel'):
        print('Você venceu!')
    else:
        print('O computador venceu!')
else:
    print('Opção inválida. Por favor, escolha entre 1, 2 ou 3.')

''' #ex045 Jogo Pedra, papel e tesoura

# REPETIÇÕES (for) <------------------------

'''
import time
print('Contagem regressiva')
for c in range(10, 0 ,-1):
    print(c)
    time.sleep(1)
print('\U0001F386 \U0001F386')

''' # ex046 Contagem regressiva

'''
for c in range(0, 50+1):
    if c % 2 == 0:
        print(c)
''' # ex047 Contagem de pares

'''
soma = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        soma = soma + c
print(soma)
''' # ex048 soma impares múltiplos de três

'''
n = int(input('Digite um número para ver sua tabuada:  '))
for c in range(0, 11):
    print(f'{n} x {c} = {n * c}')

''' # tabuada v2.0