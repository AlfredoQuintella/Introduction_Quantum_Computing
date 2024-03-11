import matplotlib.pyplot as plt
import numpy as np

def retangular_para_polar(vetor):
    x, y = vetor
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

def polar_para_retangular(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

vetor_a = [2, -1]
vetor_b = [1, 1]

r_a, theta_a = retangular_para_polar(vetor_a)
r_b, theta_b = retangular_para_polar(vetor_b)

r_soma = r_a + r_b
theta_soma = theta_a + theta_b

r_subtracao = r_a - r_b
theta_subtracao = theta_a - theta_b

resultado_soma = polar_para_retangular(r_soma, theta_soma)
resultado_subtracao = polar_para_retangular(r_subtracao, theta_subtracao)

plt.figure(figsize=(8, 8))

plt.quiver(0, 0, vetor_a[0], vetor_a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='a')

plt.quiver(0, 0, vetor_b[0], vetor_b[1], angles='xy', scale_units='xy', scale=1, color='red', label='b')

plt.quiver(0, 0, resultado_soma[0], resultado_soma[1], angles='xy', scale_units='xy', scale=1, color='green', label='a + b')

plt.quiver(0, 0, resultado_subtracao[0], resultado_subtracao[1], angles='xy', scale_units='xy', scale=1, color='purple', label='a - b')

plt.xlim(-1, 4)
plt.ylim(-2, 2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
