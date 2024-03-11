import numpy as np

def produto_tensorial(matriz1, matriz2):
    m, n = matriz1.shape
    p, q = matriz2.shape

    resultado = np.zeros((m * p, n * q), dtype=complex)

    for i in range(m):
        for j in range(n):
            resultado[i*p:(i+1)*p, j*q:(j+1)*q] = matriz1[i, j] * matriz2

    return resultado

rows1 = int(input("Digite o numero de linhas da primeira matriz: "))
cols1 = int(input("Digite o numero de colunas da primeira matriz: "))

matriz1 = np.zeros((rows1, cols1), dtype=complex)
for i in range(rows1):
    for j in range(cols1):
        parte_real = float(input(f"Digite a parte real do elemento [{i}][{j}] da primeira matriz: "))
        parte_imaginaria = float(input(f"Digite a parte imaginaria do elemento [{i}][{j}] da primeira matriz: "))
        matriz1[i][j] = parte_real + parte_imaginaria * 1j

rows2 = int(input("Digite o numero de linhas da segunda matriz: "))
cols2 = int(input("Digite o numero de colunas da segunda matriz: "))

matriz2 = np.zeros((rows2, cols2), dtype=complex)
for i in range(rows2):
    for j in range(cols2):
        parte_real = float(input(f"Digite a parte real do elemento [{i}][{j}] da segunda matriz: "))
        parte_imaginaria = float(input(f"Digite a parte imaginaria do elemento [{i}][{j}] da segunda matriz: "))
        matriz2[i][j] = parte_real + parte_imaginaria * 1j

resultado_tensorial = produto_tensorial(matriz1, matriz2)

print("\nProduto Tensorial das Matrizes:")
print(resultado_tensorial)
