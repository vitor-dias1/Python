# IF | ELIF | ELSE
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")
        
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")
        
#IF ALINHADO
conta_normal = True
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else: 
        print("Saldo insuficiente!")
elif conta_especial:
    print("Conta especial selecionada!")
else: 
    print("Sistema não reconheceu o seu tipo de conta, entre em contato com seu gerente!")
    
#if ternário

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
