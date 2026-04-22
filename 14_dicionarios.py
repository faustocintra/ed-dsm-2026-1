"""
DICIONÁRIO é uma estrutura de dados nativa da linguagem Python
capaz de armazenar múltiplos valores em uma única variável,
por meio de pares chave-valor (key-value).
Um dicionário é delimitado entre chaves {}. Diferentemente da
lista, que tem posições numeradas, o dicionário possui posições
NOMEADAS. Cada uma das posições nomeadas de um dicionário
(ou seja, cada par de chave-valor) é chamada de PROPRIEDADE.
"""
# Um dicionário com dados que representam uma pessoa.
# As chaves são sempre strings.
# Os valores podem ser de qualquer tipo válido no Python
pessoa = {
    # "chave": valor
    "nome": "Orozimbo Oliveira Osório",
    "sexo": "M",
    "idade": 72,
    "peso": 76,
    "altura": 1.77,
    "aposentado": True,
    "filhos": ["Zeferina", "Adamastor", "Gercina"]
}

# Acessando o valor das propriedades
print("Nome: ", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("É aposentado?", pessoa["aposentado"])

# Usando o valor das propriedades para efetuar um cálculo
# (no caso, o IMC - Índice de Massa Corporal)
imc = pessoa["peso"] / pessoa["altura"] ** 2

print(f"O IMC de {pessoa["nome"]} é {imc:.4f}")

print("-" * 80)

####################################################################

# Usando dicionários para representar formas geométricas

forma1 = {
    "base": 7.5,
    "altura": 3,
    "tipo": "T"             # Triângulo
}

forma2 = {
    "base": 5,
    "altura": 3.75,
    "tipo": "E"             # Elipse/círculo
}

forma3 = {
    "base": 6,
    "altura": 3,
    "tipo": "R"             # Retângulo
}

# Valor da propriedade "base" não é do tipo esperado pela função calc_area()
# forma4 = {
#     "base": "batata",
#     "altura": 14,
#     "tipo": "T"
# }

forma4 = {
    "base": 20,
    "legume": 12,
    "tipo": "E"
}

formas = [forma1, forma2, forma3, forma4]

# Reimplementação da função calc_area() do arquivo 01. Agora, no entanto,
# as informações necessárias para efetuar o cálculo são recebidas como
# um dicionário
from math import pi

def calc_area(forma):
    match forma["tipo"]:
        case "R":       # Retângulo
            return forma["base"] * forma["altura"]
        case "T":       # Triângulo
            return forma["base"] * forma["altura"] / 2
        case "E":       # Elipse/círculo
            return (forma["base"] / 2) * (forma["altura"] / 2) * pi
        case _:         # Forma inválida / não reconhecida
            return None

# <~ CUIDADO COM A INDENTAÇÃO AQUI!

# Testes com a função calc_area()

for forma in formas:
    print(f"Base: {forma["base"]}")
    print(f"Altura: {forma["altura"]}")
    print(f"Tipo: {forma["tipo"]}")
    print(f"Área: {calc_area(forma)}")
    print("-" * 30)