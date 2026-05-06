class Queue:
    """
    ESTRUTURA DE DADOS FILA
    Trata-se de uma estrutura de dados linear com acesso restrito,
    na qual a operação de inserção ("enqueue") ocorre no final (ou
    cauda), enquanto a operação de remoção ("dequeue") é feita no
    início (ou cabeça). Em decorrência, o funcionamento da fila
    pode ser descrito pelo princípio FIFO (First In, First Out): o
    o primeiro elemento a entrar é também o primeiro elemento a sair.

    Métodos:
        __init__(self)
            Inicializa uma lista privada e vazia

        enqueue(self, val)
            INSERE val no FINAL da estrutura

        is_empty(self)
            Retorna True se a lista estiver vazia, ou False, caso contrário

        dequeue(self)
            REMOVE o elemento que está no INÍCIO da estrutura. Emite erro
            caso a fila esteja vazia

        peek(self)
            Retorna o elemento que está no início da estutura (o próximo a
            ser removido), sem removê-lo. Emite erro caso a fila esteja vazia

        __str__(self)
            Retorna uma representação da fila como string

        Usando como base o código do arquovo stack.py, implemente os métodos
        descritos acima, fazendo as modificações necessárias para garantir o
        comportamento FIFO. Codifique também o arquivo 20_fila.py, com exemplos
        de utilização de filas (use 16_pilha1.py) como modelo.

        Entrega: até 12/05 às 19h, via Teams

        Esta atividade será considerada no cálculo da nota de participação.
    """