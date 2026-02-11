"""
Função que calcula o Índice de Massa Corporal (IMC) de uma
pessoa, dados o seu peso e sua altura
"""
# Declaração da função
def imc(peso, altura):
    calculo = peso / altura ** 2
    return calculo

imc_pessoa1 = imc(78, 1.65) # Chamada da função
print('IMC da pessoa 1:', imc_pessoa1, '(normal)')
print(f'IMC da pessoa 1: {imc_pessoa1} (normal)')

print('IMC da pessoa 2:', imc(104, 1.82))
print(f'IMC da pessoa 2: {imc(104, 1.82)}')

#----------------------------------------
# Retângulo: base * altura
# Triângulo: base * altura / 2
# Elipse/circulo: (base / 2) * (altura / 2) * pi (3.1416...)

from math import pi

def calc_area(base, altura, tipo):
    """
    Função que calcula a área de uma forma geométrica plana,
    dadas as medias da base e da altura e o tipo da forma
    """
    match tipo:
        case "R":   # Retângulo
            return base * altura
        case "T":   # Triângulo
            return base * altura / 2
        case "E":   # Elipse
            return (base / 2) * (altura / 2) * pi
        case _:     # Nenhuma das anteriores
            return None
        
    # if(tipo == "R"):
    #     return base * altura
    # elif(tipo == "T"):
    #     return base * altura / 2
    # elif(tipo == "E"):
    #     return (base / 2) * (altura / 2) * pi
    # else:
    #     return None
    
area_forma1 = calc_area(12, 17, "T")
print(f"Área de um triângulo 12x17: {area_forma1}")

area_forma2 = calc_area(10, 10, "E")
print(f"Área de um círculo 10x10: {area_forma2}")

area_forma3 = calc_area(16, 23, "X")
print(f"Área forma desconhecida 16x23: {area_forma3}")

area_forma4 = calc_area(15.5, 45.25, "R")
print(f"Área de um retângulo 15,5x45,25: {area_forma4}")
        