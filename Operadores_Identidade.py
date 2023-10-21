#OPERADORES DE IDENTIDADE
curso = "Curso de python"
nome_curso = curso
saldo, limite = 200, 300

ex_1 = curso is nome_curso
print(ex_1)
ex_2 = curso is not nome_curso
print(ex_2)
ex_3 = saldo is limite
print(ex_3)

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)
