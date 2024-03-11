import sympy as sp

x = sp.symbols('x')

polinomio = x**2 + 2*x + 2

solucao_complexa = -1 + sp.I 

verificacao = sp.simplify(polinomio.subs(x, solucao_complexa))

if verificacao == 0:
    print(f"{solucao_complexa} eh uma solucao do polinomio.")
else:
    print(f"{solucao_complexa} nao eh uma solucao do polinomio.")
