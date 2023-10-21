#OPERADORES LÓGICOS
# AND E OR
saldo = 1000
saque = 200
limite = 100

ex_1 = saldo >= saque and saque <= limite
ex_2 = saldo >= saque or saque <= limite

print(ex_1)
print(ex_2)

#UTILIZANDO NOT
contatos_emergencia = []
ex_3 = not 1000 > 1500 
print(ex_3)
ex_4 = not contatos_emergencia
print(ex_4)
ex_5 = not "saque 1500;"
print(ex_5)
ex_6 = not ""
print(ex_6)

# PARENTESES

saldo = 1000
saque = 250
limite = 200
conta_especial = True

ex_7 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(ex_7)
ex_8 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(ex_8)
#tabela de operadores lógicos
# na condição AND para True todos precisam ser True, na condição OR apenas 1 condição precisa ser True
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)