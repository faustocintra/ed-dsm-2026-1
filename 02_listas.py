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

print(80 * "-")

# 4) SUBSTITUINDO VALORES EXISTENTES
print("Lista de frutas antes das substituições:")
print(frutas)

# Substituindo o valor da posição 3 (QUARTA posição)
frutas[3] = "framboesa"
# Substituindo o valor da posição 0 (PRIMEIRA posição)
frutas[0] = "pitanga"
# Substituindo o valor da posição -1 (ÚLTIMA posição)
frutas[-1] = "melão"

print("Lista de frutas após as substituições:")
print(frutas)

print(80 * "-")

# 5) DETERMINANDO A QUANTIDADE DE ELEMENTOS DE UMA LISTA: len()
print(frutas)
print("Quantidade de elementos da lista de frutas:", len(frutas))
print(primos)
print("Quantidade de elementos da lista de números:", len(primos))

print(80 * "-")

# 6) REMOÇÃO DE ELEMENTOS DA LISTA

print("Lista de frutas, ANTES da remoção do último elemento:")
print(frutas)

# Removendo o ÚLTIMO elemento da lista: pop() (SEM parâmetro)
print("Removendo o elemento da última posição...")
removido = frutas.pop()
print("Elemento removido:", removido)

print("Lista de frutas, DEPOIS da remoção do último elemento:")
print(frutas)

# Removendo o elemento por SUA POSIÇÃO: pop() (COM parâmetro)
print("Removendo o elemento da posição 4...")
removido = frutas.pop(4)
print("Elemento removido:", removido)
print("Lista de frutas, depois da remoção do elemento da pos. 4:")
print(frutas)

# Removendo um elemento por seu valor: remove()
print("Removendo o elemento 'manga'...")
frutas.remove("manga")
print("Lista de frutas, após a remoção do elemento 'manga':")
print(frutas)

print(80 * "-")

# 7) AUMENTANDO A LISTA COM ELEMENTOS DE OUTRA LISTA: extend()
mais_frutas = ["carambola", "pera", "acerola", "jabuticaba", "caqui"]
frutas.extend(mais_frutas)
print("Lista de frutas estendida com elementos vindos de outra lista:")
print(frutas)

print(80 * "-")

# 8) FATIANDO UMA LISTA
#    Fatiar significa marcar um trecho de uma lista existente (sublista)
#    e, a partir dele, criar uma nova lista

# Criando uma nova lista com os elementos da posição 2 à posição 5
# ATENÇÃO: a posição 6 informada NÃO entra no resultado!
sublista2a5 = frutas[2:6]
print("Sublista com as posições de 2 a 5:", sublista2a5)
print("A lista original de frutas permanece intocada:")
print(frutas)

# Criando uma nova lista com todos elementos do início até
# a posição 7
# ATENÇÃO: a posição final 8 NÃO entra no resultado!
sublista_ate7 = frutas[:8]
print("Sublista com elementos do início até a posição 7:")
print(sublista_ate7)

# Criando uma nova lista com todos os elementos da posição 5
# até o final da lista
sublista_desde5 = frutas[5:]
print("Sublista com elementos da posição 5 até o final:")
print(sublista_desde5)