import numpy as np
from scipy import optimize
import math

x0 = 0.72
y0 = 1.41


def f1(y):
    return 1 - math.cos(x-1)


def f2(x):
    return 0.8-(1/4 * math.sin(y))


def iter(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn) >= e) & (abs(yn1-yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print('Simple iteration:')
    print('x=', xn, '\ny=', yn, '\nThe amount of iteration = ', n)


iter(x0, y0, 0.0001)


def f3(x):
    return 0.8 - 4*x[0] - math.sin(x[1]), math.cos(x[0] - 1)-x[1]-1


s = optimize.root(f3, [0., 0.], method='hybr')
print('Chek', s.x)
