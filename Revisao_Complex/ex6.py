import cmath

def calcular_modulo(c):
    return abs(c)

def verificar_propriedades(c1, c2):
    lado_esquerdo_a = calcular_modulo(c1) ** 2
    lado_direito_a = c1.real ** 2 + c1.imag ** 2
    print(f"|c1|² = {lado_esquerdo_a}, a² + b² = {lado_direito_a}")

    lado_esquerdo_b = calcular_modulo(c1 * c2)
    lado_direito_b = calcular_modulo(c1) * calcular_modulo(c2)
    print(f"|c1 * c2| = {lado_esquerdo_b}, |c1| * |c2| = {lado_direito_b}")

    lado_esquerdo_c = calcular_modulo(c1 + c2)
    lado_direito_c = calcular_modulo(c1) + calcular_modulo(c2)
    print(f"|c1 + c2| ≤ |c1| + |c2|: {lado_esquerdo_c} ≤ {lado_direito_c}")

c1 = complex(input("Insira o numero complexo c1 (na forma a+bj): "))
c2 = complex(input("Insira o numero complexo c2 (na forma a+bj): "))

verificar_propriedades(c1, c2)
