import cmath

a = complex(input("Insira o primeiro numero complexo na forma a+bj: "))
b = complex(input("Insira o segundo numero complexo na forma a+bj: "))

print("z1 + z2 =", a + b)
print("z2 + z1 =", b + a)
print("Sao iguais :)")

print("z1 * z2 =", a * b)
print("z2 * z1 =", b * a)
print("Sao iguais :)")

c = complex(input("Insira o terceiro numero complexo na forma a+bj: "))

print("(z1 + z2) + z3 =", (a + b) + c)
print("z1 + (z2 + z3) =", a + (b + c))
print("Sao iguais :)")

print("(z1 * z2) * z3 =", (a * b) * c)
print("z1 * (z2 * z3) =", a * (b * c))
print("Sao iguais :)")

print("z1 * (z2 + z3) =", a * (b + c))
print("(z1 * z2) + (z1 * z3) =", (a * b) + (a * c))
print("Sao iguais :)")
