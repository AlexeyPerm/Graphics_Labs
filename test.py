import numpy as np
import matplotlib.pyplot as plt


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

    return np.array(x_spline), np.array(y_spline)


# Контрольные точки
x_control = [0, 1, 2, 4, 5]
y_control = [0, 3, -1, 2, 0]

# Генерация сплайна
x_new, y_new = bspline_third_order(x_control, y_control)

# Визуализация
plt.figure(figsize=(10, 5))
plt.plot(x_control, y_control, label='Контрольные точки')
plt.plot(x_new, y_new, label='B-сплайн')
plt.legend()
plt.grid(True)
plt.show()
