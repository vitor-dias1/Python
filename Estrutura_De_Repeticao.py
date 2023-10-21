#Estrutura FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

#Função RANGE
# Range (stop) -> range object
# Range (start, stop [, step]) -> range object

list(range(4))

#RANGE com o FOR
# apresentará um range de 0 à 10
for numero in range (0, 11):
print(numero, end =" ")

#exemplo com a função built-in range
#apresentará de 0 à 50 de 5 em 5
for numero in range (0, 51, 5):
print(numero, end =" ")

#Estrutura WHILE    
opcao = -1

while opcao != 0:
    opcao = int(input(("[1] Sacar \n [2] Extrato \n [0] Sair \n:))
    if opcao == 1: 
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else: 
    print("Obrigado por usar nosso sistema bancário, até logo!")
    
#Estrutura BREAK com WHILE

while True:
    numero = int(input("informe um numero: "))
    
    if numero == 10:
        break
    
    print(numero)
#Estrutura CONTINUE com WHILE

while True:
    numero = int(input("informe um numero: "))
    
    if numero == 10:
        break
    if numero % 2 == 0:
        continue
    
    print(numero)

#Estrutura BREAK com FOR

for numero in range (100)
    if numero == 12
        break
    
    print(numero, end=" ")
    
#Estrutura CONTINUE com FOR

for numero in range (100)
    if numero % 2 ==0:
        continue
    
    print(numero, end=" ")    