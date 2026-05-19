from dataclasses import dataclass

class DblLinkedList:
    """
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, sem restrição de acesso, em que
    seus elementos (chamados nodos ou nós) não estão fisicamente
    adjacentes uns aos outros, mas encadeados de forma lógica por
    meio de ponteiros que indicam a localização de memória do nodo
    anterior e do nodo seguinte da sequência. Inserções, exclusões
    e consultas podem ser realizadas em qualquer posição da lista.
    """

    @dataclass
    class Node:
        """
        Classe interna que apenas armazena dados (por isso, o
        decorator @dataclass), cujas instâncias representam as
        unidades de informação que integram a lista duplamente
        encadeada
        """
        prev: int | None    = None      # Ponteiro para o nodo anterior
        data: any           = None      # Qualquer dado, de qualquer tipo
        next: int | None    = None      # Ponteiro para o nodo seguinte
    #---------------------------------------------------------------------

    def __init__(self):
        """ Construtor da classe principal DblLinkedList """
        self.__head = None              # Ponteiro para o início da lista
        self.__tail = None              # Ponteiro para o fim da lista
        self.__count = 0                # Número de elementos na lista

    def insert(self, pos, val):
        """ Método que insere na posição 'pos' o valor 'val' """
        # Se a posição passada for negativa, emitimos um erro
        if pos < 0:
            raise Exception("ERRO: posição não pode ser negativa.")
        
        # Criamos um novo nodo para armazenar 'val' e também os ponteiros
        # 'prev' e 'next', ambos apontando inicialmente para None (ponteiros
        # aterrados)
        new = self.Node(data = val)

        # 1º caso: a lista está vazia, e 'new' é o primeiro nodo a ser
        # inserido. Portanto, ele se tornará, ao mesmo tempo, o primeiro e
        # o último nodo da lista
        if self.__count == 0:
            self.__head = new
            self.__tail = new

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new

        # 3º caso: inserção no final da lista
        # OBS.: sempre que a posição passada para inserção for
        # >= count, interpretaremos como inserção no final
        elif pos >= self.__count:
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4º caso: inserção em posição intermediária
        # Esse caso depende de encontrarmos o elemento que atualmente 
        # está na posição desejada. Isso é feito por um outro método,
        # __find_node(). 

        # Incrementa o número de nodos da lista
        self.__count += 1

    def __find_node(self, pos):
        """ Método PRIVADO para encontrar um nodo na posição dada """
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.__count - 1), retorna self.__tail
        elif pos == self.__count - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se 'pos' estiver na primeira metade da lista (< self.__count // 2),
        # faz o percurso de busca a partir de self.__head
        if pos < self.__count // 2:
            node = self.__head
            for _ in range(1, pos + 1): node = node.next

        # Senão, estando a posição na segunda metade da lista, faz o
        # percurso reverso a partir de self.__tail
        else:
            node = self.__tail
            for _ in range(self.__count - 1, pos, -1): node = node.prev

        return node
    