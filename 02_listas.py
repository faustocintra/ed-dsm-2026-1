"""
LISTA é uma estrutura de dados nativa da linguagem Python.
Ela permite que uma série de valores seja associada a uma
única variável.
"""

x = 10
y = "batata"
z = True

# Lista de frutas
frutas = ["maçã", "morango", "laranja", "uva", "manga", "goiaba"]

# Lista de números
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Lista com valores de diferentes tipos
mistureba = ["Pafúncio", 37, 1.81, True]

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um de seus elementos,
# do primeiro até o último, e fazer algo com cada elemento.

# Percorrendo a lista de frutas para imprimir uma por vez
for elemento in frutas:
    print(elemento)

print('--------------------------------------')

# Percorrendo a lista de primos e exibindo o quadrado de cada um 
for n in primos:
    print(n ** 2)

# Traço separador (80 vezes o caractere "-")
print(80 * "-")

# 2) INSERÇÃO DE UM NOVO ELEMENTO NA LISTA
print("Lista de frutas, ANTES DA INSERÇÃO:", frutas)
print("Lista de números, ANTES DA INSERÇÃO:", primos)

# Inserindo um novo elemento ao FINAL de uma lista: append()
frutas.append("maracujá")
primos.append(37)

print("Lista de frutas, APÓS A INSERÇÃO:", frutas)
print("Lista de números, APÓS A INSERÇÃO:", primos)

print(80 * "-")

# Inserindo um novo elemento EM UMA POSIÇÃO ESPECÍFICA: insert()
# Parâmetros:
# 1º ~> a posição na qual será feita a inserção (obs.: a CONTAGEM
#       do número das posições COMEÇA EM ZERO)
# 2º ~> o novo elemento a ser inserido

# Inserindo um novo elemento na PRIMEIRA POSIÇÃO
frutas.insert(0, "melancia")
print("Lista de frutas após inserir 'melancia' na primeira posição:")
print(frutas)

print(80 * "-")

# Inserindo um elemento na QUARTA posição (posição 3)
frutas.insert(3, "amora")
print("Lista de frutas após inserir 'amora' na posição 3 (QUARTA posição:)")
print(frutas)

print(80 * "-")

# 3) ACESSANDO OS VALORES DA LISTA POR SUA POSIÇÃO
print("Elemento da QUINTA posição:", frutas[4])
print("Elemento da PRIMEIRA posição:", frutas[0])
print("Elemento da ÚLTIMA posição:", frutas[-1])
print("Elemento da PENÚLTIMA posição:", frutas[-2])


