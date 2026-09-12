import numpy as np
import sympy as sym

# --- Точное значение интеграла (символьно) ---
xs = sym.Symbol('xs')
ys = 0.5 * sym.sin(xs)
Is = sym.integrate(ys, (xs, 0, 10))
Is = float(Is)
print("Истинное значение определенного интеграла: ", Is)

# --- Численное интегрирование методом прямоугольников ---
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

# Рассчитываем определенный интеграл методом прямоугольников
Ipr = 0
for i in range(0, n):
    Ipr = Ipr + hx * y[i]
print("Значение интеграла, рассчитанное методом прямоугольников: ", Ipr)

# Относительная ошибка
Epr = 100 * np.abs(Is - Ipr) / Is
print("Относительная ошибка интегрирования", Epr, " %")
