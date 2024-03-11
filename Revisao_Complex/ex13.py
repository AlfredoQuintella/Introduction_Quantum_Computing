import matplotlib.pyplot as plt
import numpy as np

def plotar_operacao_complexa_i0(c, i0_values):
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))

    for i, i0 in enumerate(i0_values):
        resultado = c + 1j * i0

        ax = axes[i // 5, i % 5]
        ax.plot(np.real(resultado), np.imag(resultado), 'o', label=f'$c + i \cdot {i0}$')
        ax.set_title(f'$c + i \cdot {i0}$')
        ax.set_xlabel('Parte Real')
        ax.set_ylabel('Parte Imaginaria')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()

    plt.tight_layout()
    plt.show()

c = complex(input("Digite um numero complexo na forma a+bj: "))

i0_values = np.arange(-5, 5)

plotar_operacao_complexa_i0(c, i0_values)
