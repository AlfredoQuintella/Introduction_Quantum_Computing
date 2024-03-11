import matplotlib.pyplot as plt

def soma_vetores(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]

def subtrai_vetores(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1]]

vetor_a = [2, -1]
vetor_b = [1, 1]

resultado_soma = soma_vetores(vetor_a, vetor_b)

resultado_subtracao = subtrai_vetores(vetor_a, vetor_b)

plt.figure(figsize=(8, 8))

plt.quiver(0, 0, vetor_a[0], vetor_a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='a')

plt.quiver(0, 0, vetor_b[0], vetor_b[1], angles='xy', scale_units='xy', scale=1, color='red', label='b')

plt.quiver(0, 0, resultado_soma[0], resultado_soma[1], angles='xy', scale_units='xy', scale=1, color='green', label='a + b')

plt.quiver(0, 0, resultado_subtracao[0], resultado_subtracao[1], angles='xy', scale_units='xy', scale=1, color='purple', label='a - b')

plt.xlim(-1, 4)
plt.ylim(-2, 2)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
