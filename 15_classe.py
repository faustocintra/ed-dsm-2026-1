"""
CLASSE é uma estrutura de dados que representa simultaneamente
dados e algoritmos que operam sobre esses dados. Uma classe pode
ser comparada a uma "assadeira" com a qual se pode produzir
diferentes tipos de iguarias assadas (ou não), variando os
"ingredientes" (dados) da receita e o "modo de fazer" (algoritmos).
Apesar dessas variações, todos os objetos ("assados") criados a
partir de uma mesma classe terão sempre algumas características
comuns, impostas por ela.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classe em Python seguem o formato
    PascalCase (primeira letra de cada palavra em maiúscula).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, implementando os algoritmos). Uma função especial,
    chamada __init___, é invocada sempre que se tenta criar um
    novo objeto a partir da classe. Essa função especial é
    conhecida como MÉTODO CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas de MÉTODOS. Em Python, o
       primeiro parâmetro de todo método é sempre "self", o qual
       representa o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        """ Método construtor """
        self.base = base
        self.altura = altura
        self.tipo = tipo

#####################################################################

# Criando um objeto a partir da classe FormaGeometrica
forma1 = FormaGeometrica("batata", 14, "R")

print(f"Base: {forma1.base}")
print(f"Altura: {forma1.altura}")
print(f"Tipo: {forma1.tipo}")