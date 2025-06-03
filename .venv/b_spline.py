import matplotlib.pyplot as plt

x_points = [1, 2, 4, 7]
y_points = [2, 3, 5, 6]


# a0 = (xi-1 + 4xi+ xi+1)/6
def a0(arr):
    for a in range(len(arr)):
        q = arr[a - 1] + 4 * arr[a] + arr[a + 1]


# Построение графика
plt.plot(x_points, y_points)
plt.xlim(0, max(y_points))
# Добавление меток для осей
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)

plt.show()
