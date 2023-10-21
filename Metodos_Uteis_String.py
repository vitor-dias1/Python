curso = "PyThon"

#Texto em maisculo
print(curso.upper())

#Texto em minusculo
print(curso.lower())

#Texto em minusculo com a primeira letra maiscula
print(curso.title())

curso = "   Python   "

#Retira os espaços da esquerda e da direita
print(curso.strip())

#Retira os espaços da esquerda
print(curso.lstrip())

#Retira os espaços da direita
print(curso.rstrip())

curso = "Python"

#centraliza e inclui caracteres a esquerda e a direita de acordo com a quantidade de caracteres determinadas na função, segundo parametro caso não seja incluso, preencherá com caracteres em branco
print(curso.center(10, "#"))

#inclui o caractere determinado entre os itens do objeto
print(".".join(curso))