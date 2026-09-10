import matplotlib.pyplot as plt
import numpy as np

# --- Часть 1: Получение исходной таблицы данных ---

x = np.zeros(11)
y = np.zeros(11)
float_rn = np.zeros(11)

# Заполнение вектора x от 0 до 10 с шагом 1
for i in range(0, 10):
    x[i+1] = x[i] + 1

# Заполнение вектора случайных чисел и вычисление y
for i in range(0, 11):
    float_rn[i] = np.random.rand()
    y[i] = 0.5 * np.sin(x[i]) + 2 * float_rn[i]

print("Вектор значений x: \n", x)
print("Вектор сл.значений от 0 до 1: \n", float_rn)
print("Вектор значений y(x): \n", y)

# Сохранение исходных данных
f = open("data.txt", "w")
for i in range(0,11):
    f.write("%f" % x[i])
    f.write(" ")
    f.write("%f \n" % y[i])

f.close()

# --- Часть 2: Построение графика ---

# Построение графика
plt.title("Зависимость y(x) = 0.5*sin(x)+2*rand") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y, "r*")  # построение графика (красные звездочки)
plt.show()
