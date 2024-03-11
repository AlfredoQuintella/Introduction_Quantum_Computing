import numpy as np

def transposta_conjugada_dagger(matriz):
    transposta = np.transpose(matriz)

    conjugada = np.conj(matriz)

    dagger = np.transpose(conjugada)

    return transposta, conjugada, dagger

rows = int(input("Digite o numero de linhas da matriz: "))
cols = int(input("Digite o numero de colunas da matriz: "))

matriz_complexa = np.zeros((rows, cols), dtype=complex)
for i in range(rows):
    for j in range(cols):
        parte_real = float(input(f"Digite a parte real do elemento [{i}][{j}]: "))
        parte_imaginaria = float(input(f"Digite a parte imaginaria do elemento [{i}][{j}]: "))
        matriz_complexa[i][j] = parte_real + parte_imaginaria * 1j

transposta, conjugada, dagger = transposta_conjugada_dagger(matriz_complexa)

print("\nMatriz Original:")
print(matriz_complexa)

print("\nTransposta:")
print(transposta)

print("\nConjugada:")
print(conjugada)

print("\nDagger:")
print(dagger)
