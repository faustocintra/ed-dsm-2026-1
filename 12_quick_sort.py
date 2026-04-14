# Variáveis globais de estatística
comps = trocas = passd = None

def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô (na
    nossa implementação, será o último) e, na primeira
    passada, divide a lista a partir da posição final do
    pivô em uma sublista à sua esquerda, contendo apenas
    valores menores do que ele, e outra sublista à sua
    direita, compreendendo apenas valores maiores do que
    ele. Em seguida, recursivamente, repete o processo para
    cada uma das sublistas, até que toda a lista esteja
    ordenada.
    """
    global comps, trocas, passd

    # Cada chamada à função (inclusive as recursivas) é
    # considerada uma passada
    passd += 1

    # Quando o valor do parâmetro "fim" não tiver sido
    # informado (ou seja, seu valor é igual a None),
    # atribuímos a ele o valor da última posição da lista
    if fim is None: fim = len(lista) - 1

    # Para que seja possível proceder à ordenação, é
    # necessário que a região da lista delimitada pelos
    # parâmetros "ini" e "fim" contenha, pelo menos, DOIS
    # elementos. Caso não seja essa a situação, saímos da
    # função sem fazer nada ("early return")
    if fim <= ini: return

    # Inicialização das variáveis
    pivot = fim     # O pivô será o último elemento da (sub)lista
    div = ini - 1   # O divisor inicia uma posição antes de "ini"

    # Percorre a lista da posição "ini" até a posição "fim" - 1
    for pos in range(ini, fim):
        # Se o elemento da posição "pos" for MENOR do que o
        # elemento da posição "pivot", avança "div" em uma
        # posição e promove a troca entre os elementos das
        # posições "div" e "pos"
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1
            # Efetua a troca apenas se os valores de "pos" e
            # "div" forem distintos, indicando elementos diferentes
            if pos != div:
                trocas += 1
                lista[pos], lista[div] = lista[div], lista[pos]

    # <~ CUIDADO COM A INDENTAÇÃO AQUI!
    # Após o laço "for" terminar, "div" deve ainda avançar
    # mais uma posição
    div += 1

    # Comparamos os elementos das posições "pivot" e "div"
    # entre si e, caso o primeiro seja MENOR do que o
    # segundo, efetuamos a troca entre eles
    comps += 1
    if lista[pivot] < lista[div]:
        trocas += 1
        lista[pivot], lista[div] = lista[div], lista[pivot]

    # Chamamos recursivamente a função para repetir o processo
    # para as sublistas à esquerda e à direita do pivô
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

##################################################################

comps = trocas = passd = 0

nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]

print("ANTES: ", nums)
quick_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
