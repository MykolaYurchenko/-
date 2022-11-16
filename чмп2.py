import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative


def f(x):
    return x**4 - 4*x - 1


a = float(-1.73)
b = float(1.73)
eps = 0.001


def hord(a, b, eps):
    if (f(a)*derivative(f, a, n=2) > 0):
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    print(f'Метод хорд.Корінь знаходиться в точці x =', round(xi_1, 5))


hord(a, b, eps)


def dihotom(a, b, eps):
    while (abs(a-b) > eps):
        if f(a)*f((a+b)/2) < 0:
            b = (a+b)/2
        else:
            a = (a+b)/2

    print('Корінь рівняння x = ', round((a+b)/2, 5))


dihotom(a, b, eps)

x = np.arange(a, b, 0.01)
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод ділення навпіл')
plt.grid()
plt.show()
