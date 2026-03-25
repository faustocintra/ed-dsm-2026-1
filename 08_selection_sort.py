# Variáveis globais de estatística
comps = trocas = passd = None

def selection_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e, em
    seguida, encontra o menor valor entre os elementos
    restantes na lista. Se o valor encontrado for MENOR
    do que o valor previamente selecionado, efetua a troca
    entre eles. Continuando, seleciona o segundo elemento
    da lista, buscando pelo menor valor nas posições
    subsequentes. O processo se repete até que o penúltimo
    elemento da lista seja comparado com o último e feita
    a troca entre eles, caso preciso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop que vai da primeira até a PENÚLTIMA posição
    # para selecionar o elemento que será comparado com os
    # demais. Este laço também determina a quantidade de
    # passadas que serão executadas (número constante: n-1)
    for pos_sel in range(len(lista) - 1):
        passd += 1

        # Inicia supondo que a posição do menor valor do resto
        # da lista é aquela imediatemente seguinte à do valor
        # selecionado
        pos_menor = pos_sel + 1

        # Percorre o restante da lista, da posição seguinte a
        # pos_menor até a púltima posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor que estiver na posição atual (pos) for
            # MENOR do que aquele apontado por pos_menor, ajusta
            # pos_menor para o mesmo valor que pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # <~ CUIDADO COM A INDENTAÇÃO AQUI!
        # Neste ponto, já terminamos de percorrer o restante da
        # lista e sabemos a posição do menor valor que há ali.
        # Comparamos os valores das posições pos_menor e pos_sel.
        # Se o PRIMEIRO for MENOR do que o SEGUNDO, efetuamos a
        # troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_sel], lista[pos_menor] = lista[pos_menor], lista[pos_sel]
            trocas += 1

################################################################################

# Caso médio
# nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]
# Comparações: 45; trocas: 8; passadas: 9

# Melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Comparações: 45; trocas: 0; passadas: 9

# Pior caso
nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# Comparações: 45; trocas: 9; passadas: 9

print("ANTES: ", nums)

# Chama a função para fazer a ordenação de nums
selection_sort(nums)

print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")

######################################################################

# TESTE COM 1M+ NOMES

from time import time

import sys
sys.dont_write_bytecode = True      # Desativa a criação do cache

from data.nomes_desord import nomes

hora_ini = time()
selection_sort(nomes)
hora_fim = time()

print(nomes)

print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")