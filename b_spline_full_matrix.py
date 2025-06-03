import numpy as np
import matplotlib.pyplot as plt


# Функция для добавления крайних сегментов для замыкания сплайна
def add_closing_segments(x, y, t, x_spline, y_spline):
    closing_indices = [
        ([-3, -2, -1, 0], [-3, -2, -1, 0]),
        ([-2, -1, 0, 1], [-2, -1, 0, 1]),
        ([-1, 0, 1, 2], [-1, 0, 1, 2])
    ]
    for xi, yi in closing_indices:
        x_last = [x[i] for i in xi]
        y_last = [y[i] for i in yi]
        a3, a2, a1, a0 = coeffs(x_last)
        b3, b2, b1, b0 = coeffs(y_last)
        x_t = ((a3 * t + a2) * t + a1) * t + a0
        y_t = ((b3 * t + b2) * t + b1) * t + b0
        x_spline.extend(x_t)
        y_spline.extend(y_t)


# Коэффициенты для x(t) и y(t)
def coeffs(p):
    """
    Вычисляет коэффициенты для B-сплайна третьего порядка по четырём контрольным точкам.
    :param p: Список или массив из четырёх контрольных точек (координат по одной оси)
    :return: Кортеж из четырёх коэффициентов (c3, c2, c1, c0) для полинома сплайна
    """
    c3 = (-p[0] + 3 * p[1] - 3 * p[2] + p[3]) / 6
    c2 = (p[0] - 2 * p[1] + p[2]) / 2
    c1 = (-p[0] + p[2]) / 2
    c0 = (p[0] + 4 * p[1] + p[2]) / 6
    return c3, c2, c1, c0


def bspline_third_order(x, y, num_points_per_segment=10):
    """
    Генерация B-сплайна третьего порядка по контрольным точкам.
    :param x: Координаты X контрольных точек
    :param y: Координаты Y контрольных точек
    :param num_points_per_segment: Генерация параметра t от 0 до 1 с шагом 0.1
    :return: Координаты B-сплайна
    """
    x = np.asarray(x)
    y = np.asarray(y)

    if len(x) != len(y):
        raise ValueError("x и y должны иметь одинаковую длину")
    if len(x) < 4:
        raise ValueError("Необходимо минимум 4 контрольные точки")

    n_segments = len(x) - 3
    # Генерация параметра t от 0 до 1 с шагом 0.1
    t = np.linspace(0, 1, num_points_per_segment).round(1)

    x_spline, y_spline = [], []

    for i in range(n_segments):
        # Текущие контрольные точки
        xi = x[i:i + 4]
        yi = y[i:i + 4]

        a3, a2, a1, a0 = coeffs(xi)
        b3, b2, b1, b0 = coeffs(yi)

        # Вычисление координат сплайна
        x_t = ((a3 * t + a2) * t + a1) * t + a0
        y_t = ((b3 * t + b2) * t + b1) * t + b0

        x_spline.extend(x_t)
        y_spline.extend(y_t)

    # Добавление крайних сегментов для замыкания сплайна

    add_closing_segments(x, y, t, x_spline, y_spline)

    # Преобразование в массивы NumPy
    return np.array(x_spline), np.array(y_spline)


# Контрольные точки
x_control = [-0.57, -0.31, 0.43, 0.53, 0.22, -0.04, 0.06, -0.17, -0.43, -1.17, -1.28, -1.12, -0.75, -0.83, -0.46, -0.30,
             -0.41, -0.15, 0.09, -0.28, -0.36, -0.73, -0.57]
y_control = [7.48, 6.84, 8.72, 10.29, 14.71, 15.35, 16.92, 20.23, 20.87, 18.99, 17.42, 15.21, 16.15, 17.25, 18.19,
             15.98, 14.41, 13.77, 10.46, 9.52, 10.63, 9.69, 7.48]

# Генерация сплайна
x_new, y_new = bspline_third_order(x_control, y_control)

# Визуализация
plt.figure(figsize=(10, 10))
plt.plot(x_control, y_control, label='Контрольные точки')
plt.plot(x_new, y_new, label='B-сплайн')
plt.legend()
plt.grid(True)

plt.show()
