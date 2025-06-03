import matplotlib.pyplot as plt
import math

# Координаты точек
x = [1, 2, 6, 7, 7, 6, 7, 7, 6, 2, 1, 1, 3, 3, 5, 5, 4, 5, 5, 3, 3, 1, 1]
y = [2, 1, 1, 2, 6, 7, 8, 11, 12, 12, 11, 9, 9, 10, 10, 8, 7, 6, 3, 3, 4, 4, 2]
a = 0.2
d = 1.2
m = -3
n = 4

angle = 23
rad_angle = math.radians(angle)
cos_theta = math.cos(rad_angle)
sin_theta = math.sin(rad_angle)

# Полная матрица преобразования
x_full = []
y_full = []
# | a*(x*cos(alpha)-y*sin(alpha)+m d*(x*sin(alpha)+y*(cos(alpha)+n)|

for i in range(len(x)):
    x_full.append(a * (x[i] * cos_theta - y[i] * sin_theta + m))
    y_full.append(d * (x[i] * sin_theta + y[i] * cos_theta + n))

for i in range(len(x)):
    print(f"{x_full[i]}\t{y_full[i]}")

# plt.plot(x_full, y_full, '')
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")
# plt.grid(True)
#
# plt.show()
