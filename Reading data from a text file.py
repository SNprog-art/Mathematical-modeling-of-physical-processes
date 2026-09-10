import matplotlib.pyplot as plt
import numpy as np
x = np.zeros(11)
y = np.zeros(11)

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

for i in range(0,11):
    x[i] = data[i][0]
    y[i] = data[i][1]

print("Считанные данные из файла: \n", data)
print("Вектор значений x: \n",x)
print("Вектор значений y(x): \n",y)


'''
OUTPUT:

Считанные данные из файла:
		тут дохуя написано, если интересно см. ЛК4 или Ctrl+C, +V в CMD
'''
