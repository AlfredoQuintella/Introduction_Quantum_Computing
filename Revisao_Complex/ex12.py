import matplotlib.pyplot as plt
import numpy as np

def plotar_operacoes_complexas(c):
    resultados = [c**n for n in range(1, 11)]

    plt.figure(figsize=(12, 6))

    for i, resultado in enumerate(resultados, start=1):
        plt.subplot(2, 5, i)
        plt.plot(np.real(resultado), np.imag(resultado), 'o', label=f'$c^{{{i}}}$')
        plt.title(f'$c^{{{i}}}$')
        plt.xlabel('Parte Real')
        plt.ylabel('Parte Imaginaria')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.legend()

    plt.tight_layout()
    plt.show()

c = complex(input("Digite um numero complexo na forma a+bj: "))

plotar_operacoes_complexas(c)
