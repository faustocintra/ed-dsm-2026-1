frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer (iterar) uma lista e exibir apenas seus
# elementos, usamos a estrutura for..in, como já visto no
# arquivo 02
for f in frutas:
    print(f)

print("-" * 80)

# Percorrendo a lista em ordem inversa: reversed()
for el in reversed(frutas):
    print(el)

print("-" * 80)

# No entanto, é comum precisar exibir, além do elemento, também
# sua posição na lista. Nesse caso, devemos usar a estrutura
# for..in combinada com as funções range() e len()
for pos in range(len(frutas)):
    print(f"Posição {pos} => {frutas[pos]}")

print("-" * 80)

# Às vezes, será necessário percorrer a lista em ordem reversa,
# tendo acesso às posições dos elementos. Para isso, usamos for..in
# combinado com as funções range() (com passo negativo) e len()
for p in range(len(frutas) - 1, -1, -1):
    print(f"Posição {p} => {frutas[p]}")