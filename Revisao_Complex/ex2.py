def calcular_potencia_complexa(n):
    resto_modulo_4 = n % 4
    
    if resto_modulo_4 == 0:
        return 1
    elif resto_modulo_4 == 1:
        return complex(0, 1) 
    elif resto_modulo_4 == 2:
        return -1
    elif resto_modulo_4 == 3:
        return complex(0, -1) 

n = int(input("Insira a potencia desejada: "))

resultado = calcular_potencia_complexa(n)

print("Resultado:", resultado)
