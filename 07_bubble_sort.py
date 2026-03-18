# Variáveis globais de estatística
comps = trocas = passd = None

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o SEGUNDO for MENOR do que o PRIMEIRO. Efetua tantas
    passadas quanto necessárias, até que, na última passada,
    nenhuma troca tenha sido feita.
    """
    # Avisando à função que iremos usar as variáveis globais
    # dentro dela
    global comps, trocas, passd

    # Resetando o valor das variáveis de estatística
    comps = trocas = passd = 0

    # Loop eterno: não sabemos com antecedência quantas
    # passadas serão necessárias para concluir a ordenação
    while True:
        passd += 1

        # Variável que controla se houve ou não troca durante
        # a passada
        trocou = False

        # Percorre a lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        for pos in range(len(lista) - 1):
            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que o seu antecessor (pos), efetuamos
            # uma troca entre eles
            comps += 1
            if lista[pos + 1] < lista[pos]:
                # Faz a troca (swap) direta
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                # Assinala que houve troca na passada
                trocou = True

        # <~ CUIDADO COM A INDENTAÇÃO AQUI!
        # Se não houve troca na passada (trocou ainda tem o valor False),
        # a lista está ordenada e interrompemos o loop while
        if not trocou: break

############################################################################

# Caso médio
# nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]
# Comparações: 63; trocas: 22; passadas: 7

# Melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Comparações: 9; trocas: 0; passadas: 1

# Pior caso
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Comparações: 90; trocas: 45; passadas: 10

print("ANTES: ", nums)

# Chama a função para fazer a ordenação de nums
bubble_sort(nums)

print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")

######################################################################

# TESTE COM 1M+ NOMES

from time import time

import sys
sys.dont_write_bytecode = True      # Desativa a criação do cache

from data.nomes_desord import nomes

hora_ini = time()
bubble_sort(nomes)
hora_fim = time()

print(nomes)

print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")
