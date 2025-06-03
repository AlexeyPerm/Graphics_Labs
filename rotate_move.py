import math
import numpy as np
import matplotlib.pyplot as plt

angle = 23
rad_angle = math.radians(angle)
cos_theta = math.cos(rad_angle)
sin_theta = math.sin(rad_angle)

# базовые координаты точек
x = [1, 2, 6, 7, 7, 6, 7, 7, 6, 2, 1, 1, 3, 3, 5, 5, 4, 5, 5, 3, 3, 1, 1]
y = [2, 1, 1, 2, 6, 7, 8, 11, 12, 12, 11, 9, 9, 10, 10, 8, 7, 6, 3, 3, 4, 4, 2]

# Преобразование координат точек:
x_rotate = []
y_rotate = []

for i in range(len(x)):
    x_rotate.append(x[i] * cos_theta - y[i] * sin_theta)
    y_rotate.append(x[i] * sin_theta + y[i] * cos_theta)
# Построение графика
plt.plot(x_rotate, y_rotate)
#
#Для соблюдения размера x и y
if angle == 0:
    plt.xlim(0, max(y))
# Добавление меток для осей
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)

plt.savefig('rotate.png')
plt.close('all')
print("####### Вращение #######")
for i in range(len(x)):
    print(f"{x_rotate[i]}\t{y_rotate[i]}")
####### Перемещение #######
m = -3
n = 4

x_move = []
y_move = []

for i in range(len(x)):
    x_move.append(x_rotate[i] + m)
    y_move.append(y_rotate[i] + n)

plt.plot(x_move, y_move)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)

plt.savefig('move.png')
plt.close('all')
print("####### Перемещение #######")
for i in range(len(x)):
    print(f"{x_move[i]}\t{y_move[i]}")

####### Масштабирование #######

a = 0.2
d = 1.2
x_scale = []
y_scale = []

for i in range(len(x)):
    x_scale.append(x_move[i] * a)
    y_scale.append(y_move[i] * d)

plt.plot(x_scale, y_scale)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)

plt.savefig('scale.png')
plt.close('all')

print("####### Масштабирование #######")
for i in range(len(x)):
    print(f"{x_scale[i]}\t{y_scale[i]}")

#Полная матрица преобразования
x_full = []
y_full = []

# | a*(x*cos(alpha)-y*sin(alpha)+m d*(x*sin(alpha)+y*(cos(alpha)+n)|

# angle = 23
# rad_angle = math.radians(angle)
# cos_theta = math.cos(rad_angle)
# sin_theta = math.sin(rad_angle)
