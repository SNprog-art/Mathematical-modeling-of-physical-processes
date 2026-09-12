import sympy as sym

# Определение символьных переменных
x = sym.Symbol('x')
y = sym.Symbol('y')

# 1. Раскрытие скобок
f1 = (x + 2)*(x + 3) + (y + 5)
f1e = sym.expand(f1)
print("Раскрытие скобок для f1 = f1e = ", f1e)

# 2. Упрощение выражения
f2 = (x * y**3 + 2*y + x**4 * y) / y
f2s = sym.simplify(f2)
print("Упрощение выражения f2 = f2s = ", f2s)

# 3. Факторизация многочлена
f3 = (x+4)**4 + x**2 + (x-2)**3
f3f = sym.factor(f3)
print("Факторизация многочлена f3 = f3f = ", f3f)
