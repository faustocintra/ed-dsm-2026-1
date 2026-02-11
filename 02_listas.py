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