import sympy as sp

x = sp.symbols('x')

equation = x**4 + 2*x**2 + 1

solutions = sp.solve(equation, x)

real_solutions = [sol.evalf() for sol in solutions if sol.is_real]

if not real_solutions:
    print("A equacao nao possui solucoes reais.")
else:
    print("A equacao possui solucoes reais:", real_solutions)
