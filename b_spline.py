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
x_control = [1, 2, 6, 7, 7, 6, 7, 7, 6, 2, 1, 1, 3, 3, 5, 5, 4, 5, 5, 3, 3, 1, 1]
y_control = [2, 1, 1, 2, 6, 7, 8, 11, 12, 12, 11, 9, 9, 10, 10, 8, 7, 6, 3, 3, 4, 4, 2]

# Генерация сплайна
x_new, y_new = bspline_third_order(x_control, y_control)

# Визуализация
plt.figure(figsize=(5, 5))
plt.plot(x_control, y_control, label='Контрольные точки')
plt.plot(x_new, y_new, label='B-сплайн')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Сохраняет масштаб осей
plt.show()
