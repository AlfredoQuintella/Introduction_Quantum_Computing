import math

def cartesianas_para_polares(x, y):
    r = math.sqrt(x**2 + y**2)
    
    theta = math.atan2(y, x)
    
    return r, theta

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

r, theta = cartesianas_para_polares(x, y)

print(f"Coordenadas polares: (r = {r}, θ = {theta} radianos)")
