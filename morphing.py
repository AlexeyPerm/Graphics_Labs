import matplotlib.pyplot as plt

# Координаты точек базовой фигуры. t = 0
x_t0 = [1, 2, 6, 7, 7, 6, 7, 7, 6, 2, 1, 1, 3, 3, 5, 5, 4, 5, 5, 3, 3, 1, 1]
y_t0 = [2, 1, 1, 2, 6, 7, 8, 11, 12, 12, 11, 9, 9, 10, 10, 8, 7, 6, 3, 3, 4, 4, 2]

# Координаты точек преобразованной фигуры. t = 1
x_t1 = [-0.57, -0.31, 0.43, 0.53, 0.22, -0.04, 0.06, -0.17, -0.43, -1.17, -1.28, -1.12, -0.75, -0.83, -0.46, -0.3,
        -0.41, -0.15, 0.09, -0.28, -0.36, -0.73, -0.57]
y_t1 = [7.48, 6.84, 8.72, 10.29, 14.71, 15.35, 16.92, 20.23, 20.87, 18.99, 17.42, 15.21, 16.15, 17.25, 18.19, 15.98,
        14.41, 13.77, 10.46, 9.52, 10.63, 9.69, 7.48]

t_025 = 0.25
t_05 = 0.5
t_075 = 0.75

def interpolate_shape(x0, y0, x1, y1, t):
    x = []
    y = []
    for i in range(len(x0)):
        x.append(x0[i] * (1 - t) + x1[i] * t)
        y.append(y0[i] * (1 - t) + y1[i] * t)
    return x, y


x_t025, y_t025 = interpolate_shape(x_t0, y_t0, x_t1, y_t1, t_025)
x_t05, y_t05 = interpolate_shape(x_t0, y_t0, x_t1, y_t1, t_05)
x_t075, y_t075 = interpolate_shape(x_t0, y_t0, x_t1, y_t1, t_075)

plt.plot(x_t0, y_t0, color='black', label='Базовая фигура в t=0', linewidth=1)
plt.plot(x_t025, y_t025, '--', color='green', label='Фигура в t=0.25')
plt.plot(x_t05, y_t05, '-.', color='red', label='Фигура в t=0.5')
plt.plot(x_t075, y_t075, '-', color='c', label='Фигура в t=0.75')
plt.plot(x_t1, y_t1, color='#0313FF', label='Фигура в t=1', linewidth=1)

plt.title("Преобразование фигуры Morphing")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)
plt.legend()
plt.show()

# plt.savefig('morphling_figure.png')
# plt.close('all')
