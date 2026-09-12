import numpy as np
import sympy as sym

# --- Точное значение интеграла (символьно) ---
xs = sym.Symbol('xs')
ys = 0.5 * sym.sin(xs)
Is = sym.integrate(ys, (xs, 0, 10))
Is = float(Is)
print("Истинное значение определенного интеграла: ", Is)

# --- Численное интегрирование методом трапеций ---
def f(x):
    return 0.5 * np.sin(x)

# Создаем исходную таблицу для численного интегрирования
hx = 1
x = np.zeros(11)
n = np.size(x)
y = np.zeros(n)
y[0] = f(x[0])
for i in range(1, n):
    x[i] = x[i-1] + hx
    y[i] = f(x[i])

# Рассчитываем определенный интеграл методом трапеций
Itr = 0
for i in range(1, n):
    Itr = Itr + (hx / 2) * (y[i-1] + y[i])
print("Значение интеграла, рассчитанное методом трапеций: ", Itr)

# Относительная ошибка
Etr = 100 * np.abs(Is - Itr) / Is
print("Относительная ошибка интегрирования", Etr, " %")
