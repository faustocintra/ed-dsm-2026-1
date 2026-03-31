def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT
    Durante o processo de ordenação, este algoritmo "desmonta"
    a lista original, contendo N elementos, até obter N listas
    com apenas um elemento cada uma. Em seguida, utilizando a
    técnica de mesclagem ("merging"), "monta" uma nova lista,
    contendo os elementos já ordenados.
    """
    # PARTE 1: DIVISÃO DA LISTA ORIGINAL EM LISTAS MENORES

    # Para que possa haver a divisão da lista, esta deve ter
    # mais de um elemento. Se essa condição não for satisfeita,
    # sai prematuramente da função retornando a própria lista
    if len(lista) <= 1: return lista

    # Calcula a posição do meio da lista, para fazer a divisão
    # em duas partes (aproximadamente) do mesmo tamanho
    meio = len(lista) // 2

    # Faz uma cópia da primeira metade da lista, usando fatiamento
    sublista_esq = lista[:meio]
    # Faz o mesmo para a segunda metade
    sublista_dir = lista[meio:]

    print(f"ESQ: {sublista_esq}, DIR: {sublista_dir}")

    # Chamamos recursivamente (duas vezes!) a própria função para
    # que ela continue repartindo cada sublista em outras duas, menores
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # PARTE 2: REMONTAGEM DA LISTA, DE FORMA ORDENADA

    # Ponteiros para percorrer as sublistas esquerda e direita
    pos_esq = pos_dir = 0

    # Inicializando duas listas vazias
    ordenada, sobra = [], []

    # Percorremos as sublistas esquerda e direita, comparando os elementos
    # e os inserindo na ordem correta na lista ordenada
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        # O menor elemento está na sublista da esquerda
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1    # Avança o ponteiro da esquerda
        # O menor elemento está na sublista da direita
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1    # Avança o ponteiro da direita

    # <~ CUIDADO COM A INDENTAÇÃO AQUI!
    # Verifica se há sobra na sublista da esquerda
    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
    # A sobra pode estar também na sublista da direita
    else: sobra = sublista_dir[pos_dir:]

    # A lista final ordenada é o resultado da junção (concatenação)
    # da lista ordenada com a sobra
    return ordenada + sobra

#############################################################################

nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]

print("ANTES: ", nums)

nums_ord = merge_sort(nums)

print("DEPOIS:", nums_ord)