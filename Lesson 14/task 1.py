import matplotlib.pyplot as plt
import numpy as np

# Задаємо функцію, яку будемо вивчати
# Задання функції
def func(x):
    return np.sqrt(x)*np.sin(5*x)

# Значення x в інтервалі від 0 до 10 з кроком 0.1
x_values = np.arange(0, 5, 0.1)
# Знаходимо відповідні значення y за допомогою функції
y_values = func(x_values)

# Побудова графіка
plt.plot(x_values, y_values, label='np.sqrt(x)*np.sin(5*x)', color='blue', linestyle='-', linewidth=2)

# Додаємо підписи осей
plt.xlabel('x')
plt.ylabel('y')

# Додаємо заголовок графіка
plt.title('Графік функції np.sqrt(x)*np.sin(5*x)')

# Встановлюємо позначення на графіку
plt.legend()

# Виведення графіка на екран
plt.grid(True)
plt.show()
