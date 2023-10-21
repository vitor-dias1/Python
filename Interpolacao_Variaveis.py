nome = "vitor"
idade = 23
profissao = "Anl Plan SR"
linguagem = "Python"

# %s é utilizado para concatenar variaveis do tipo string, %d do tipo inteiro e %f do tipo Float. - old style
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

#método format
pessoa = {"nome:" "vitor", "idade:" "23", "profissao:" "Anl Plan SR","linguagem:" "Python"}
nome = "vitor"
idade = 23
profissao = "Anl Plan SR"
linguagem = "Python"
#format padrão
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))
#format com indice - neste formato não precisa incluir mais de uma vez a menção no format e sim a inclusão do número do indice
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))
#format com nomeando a variavel no indice   
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))
#format com dicionario
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(**pessoa))


#utilizando f-string
nome = "vitor"
idade = 23
profissao = "Anl Plan SR"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

#formatação de float ou valores decimais
PI = 3.14159
print(f"valor de PI:{PI:.2f}")
print(f"valor de PI:{PI:10.2f}")



