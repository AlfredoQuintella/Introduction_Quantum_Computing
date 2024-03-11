import numpy

def calcular_conjugado(c):
    return numpy.conj(c)

def verificar_propriedades(c1, c2):
    prop_a_esquerda = calcular_conjugado(c1) + calcular_conjugado(c2)
    prop_a_direita = calcular_conjugado(c1+c2)
    print(f"Propriedade a) {prop_a_esquerda} = {prop_a_direita}")

    prop_b_esquerda = calcular_conjugado(c1) * calcular_conjugado(c2)
    prop_b_direita = calcular_conjugado(c1 * c2)
    print(f"Propriedade b) {prop_b_esquerda} = {prop_b_direita}")

c1 = complex(input("Insira o numero complexo c1 (na forma a+bj): "))
c2 = complex(input("Insira o numero complexo c2 (na forma a+bj): "))

verificar_propriedades(c1, c2)
