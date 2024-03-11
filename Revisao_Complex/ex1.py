import sympy as sp

x = sp.symbols('x')

equation = x**4 + 2*x**2 + 1

solutions = sp.solve(equation, x)

real_solutions = [sol.evalf() for sol in solutions if sol.is_real]

if not real_solutions:
    print("A equação não possui soluções reais.")
else:
    print("A equação possui soluções reais:", real_solutions)
