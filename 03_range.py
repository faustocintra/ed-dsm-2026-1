"""
range() é uma função da linguagem Python que gera uma
série (faixa) de números. É muito usada em assiciação
com listas e com a instrução "for".
"""

# 1) range() com UM parâmetro
#    Gera uma sequência numérica que SEMPRE começa
#    em 0 (zero) e vai até o valor do parâmetro - 1
for num in range(10):
    # Faixa gerada: 0 1 2 3 4 5 6 7 8 9
    print(num)

print("-" * 80)

# 2) range() com DOIS parâmetros
#    1º parâmetro: valor inicial da sequência (inclusive)
#    2º parâmetro: valor final da sequência (EXCLUSIVE)
for x in range(10, 18):
    # Faixa gerada: 10 11 12 13 14 15 16 17
    print(x)

print("-" * 80)

# 3) range() com TRÊS parâmetros
#    1º parâmetro: valor inicial da sequência (inclusive)
#    2º parâmetro: valor final da sequência (EXCLUSIVE)
#    3º parâmetro: intervalo entre um número gerado e o
#                  seguinte (passo)
for n in range(0, 22, 3):
    # Faixa gerada: 0 3 6 9 12 15 18 21
    print(n)

print("-" * 80)

# 4) range() com passo negativo (CONTAGEM REGRESSIVA)
for k in range(10, -1, -1):
    # Faixa gerada: 10 9 8 7 6 5 4 3 2 1 0
    print(k)