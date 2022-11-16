from scipy import integrate
import math
eps = 0.001


def f1(x):
    return (x/2)*math.log10(x**2/2)


def simpson(a, b, n):
    h = (b - a) / n
    integr = f1(a) + f1(b)
    for i in range(1, n):
        k = a + i*h
        if i % 2 == 0:
            integr += 2 * f1(k)
        else:
            integr += 4 * f1(k)
    integr *= h/3
    return integr


if abs(simpson(1.6, 3.2, 3*8) - simpson(1.6, 3.2, 8)) / 15. <= eps:
    print("Simpsone method:", round(simpson(1.6, 3.2, 8), 5))
v, err = integrate.quad(f1, 1.6, 3.2)  # Перевірка
print("Check for the simpsone method= ", round(v, 5))
