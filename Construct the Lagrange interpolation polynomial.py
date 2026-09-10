import matplotlib.pyplot as plt
import numpy as np

def lagrang(xf, xe, ye, ne):
    Pn = 0
    for i in range(0, ne):
        mult = 1
        for k in range(0, ne):
            if(k != i):
                mult = mult * ((xf - xe[k])/(xe[i] - xe[k]))
        
        Pn = Pn + ye[i] * mult
    
    return Pn

# Чтение исходных данных
# -------------------------
import re
file = open("data.txt")
values = file.read().split("\n")
data = []
for key in values:
    value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
    
    if value != []:
        data.append(value)
# -------------------------
x = np.zeros(11)
y = np.zeros(11)
for i in range(0, 11):
    x[i] = data[i][0]
    y[i] = data[i][1]

print("Считанные данные из файла: \n", data)
print("Вектор значений x: \n", x)
print("Вектор значений y(x): \n", y)

x_intp = np.zeros(101)
n_x_intp = np.size(x_intp)
for i in range(0, n_x_intp-1):
    x_intp[i+1] = x_intp[i] + 0.1

y_intp = np.zeros(n_x_intp)
n = np.size(x)
for i in range(0, n_x_intp):
    y_intp[i] = lagrang(x_intp[i], x, y, n)

# Построение графика
plt.title("Зависимость y(x), y_intp(x_intp)") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y, "r*", x_intp, y_intp)  # построение графика
plt.show()
