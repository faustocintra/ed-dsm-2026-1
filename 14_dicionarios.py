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