#%%
#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
#que é uma estrutura versátil e simples de entender. Por exemplo:

#for c in range(0, 4):

#print(c)

#print(‘Acabou’)

#%%

#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para 
#o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print("DESAFIO 046")

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("BUM ! BUM! POOOW!")

#%%

#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("DESAFIO 047")

for n in range(2, 51, 2):
    print(n, end=" ")
print("\nAcabou!")


#%%

#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#e que se encontram no intervalo de 1 até 500.

print("DESAFIO 048")

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c 
        cont += 1
print(f"A soma de todos os {cont} valores solicitados é {soma}")

#%%

#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
#só que agora utilizando um laço for.

print("DESAFIO 049")

num = int(input("Digite um número para ver sua tabuada: "))

for c in range(1, 11):
    print(f"{num} x {c:2} = {num*c}")

#%%

#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print("DESAFIO 050")

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f"Você informou {cont} números PARES e a soma foi {soma}")

#%%

#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
#mostre os 10 primeiros termos dessa progressão.

print("DESAFIO 051")

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end= " -> ")
print("Acabou!")

#%%

#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print("DESAFIO 052")

num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f"{c}", end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')

if tot == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele Não é primo!")

#%%

#Exercício Python 53: Crie um programa que leia uma frase qualquer 
#e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print("DESAFIO 053")

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f"O inverso de {junto} é {inverso}")

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")