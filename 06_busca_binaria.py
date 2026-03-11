# Variável global para contar o número de comparações
comps = None

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dada uma lista, que DEVE ESTAR PREVIAMENTE ORDENADA, e um
    valor de busca, divide a lista em duas partes iguais tanto
    quanto possível, procurando pelo valor de busca apenas no
    lado onde poderia estar. Novas subdivisões são feitas até
    que se encontre o valor de busca ou que reste apenas uma
    sublista vazia, quando então se conclui que o valor de
    busca não consta da lista buscada.
    """

    global comps    # Usa a variável global dentro da função
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        comps += 1

        # Calculando a posição do meio da lista
        # O operador // em Python significa divisão inteira
        # (descarta a parte fracionária, se houver)
        meio = (ini + fim) // 2

        # Verifica se o valor que está no meio da lista é
        # igual ao valor de busca. Em caso afirmativo, 
        # retornamos a posição do meio, pois o valor de busca
        # foi encontrado
        if val == lista[meio]:
            return meio
        
        # Senão, se o valor de busca é MENOR do que aquele que
        # está no meio da lista, move o ponteiro do fim para
        # a posição anterior à do meio e reinicia a busca na
        # metade ESQUERDA da lista
        elif val < lista[meio]:
            fim = meio - 1

        # Por fim, caso o valor de busca seja MAIOR do que aquele
        # que está no meio da lista, move o ponteiro de início para
        # a posição seguinte à do meio e reinicia a busca na metade
        # DIREITA DA LISTA
        else:
            ini = meio + 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI
    # Se chegamos até aqui, é porque o valor de busca não existe
    # na lista
    return -1

#############################################################################

# TESTE COM 1M+ DE NOMES

import sys
sys.dont_write_bytecode = True  # Impede a criação do cache

from time import time

from data.nomes_completos import nomes

buscas = [
    "EDSON PEREIRA",
    "MARIA FERREIRA",
    "VALDIR SILVA",
    "GILCINEIA GARCIA"
]

for n in buscas:
    hora_ini = time()
    pos = busca_binaria(nomes, n)
    hora_fim = time()
    if pos >= 0:
        print(f"Nome {n} encontrado na posição {pos}.")
    else:
        print(f"Nome {n} não encontrado, busca retornou {pos}.")
    print(f"Número de comparações: {comps}")
    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")