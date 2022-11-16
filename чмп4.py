import numpy as np
import random
a = np.array([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
b = np.array([[1, 2, 1], [0, 1, 2], [3, 1, 1]])
c = a*b
d = b*a
print(c, d)

a = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
a2 = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
A = a*a2
print(A)

a = np.array([[5, 8, -4], [6, 9, -5], [4, 7, -3]])
b = np.array([[3, 2, 5], [4, -1, 3], [9, 6, 5]])
c = a.dot(b)
print(c)

a = np.array([[1, 2, 3], [-1, 2, 1], [1, 3, 2]])
a_det = np.linalg.det(a)
print(format(a_det, '9g'))

a = np.array([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 2, 1], [4, 1, 2, 3]])
a_det = np.linalg.det(a)
print(format(a_det, '9g'))

A = np.array([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 2, 1], [4, 1, 2, 3]])
A_inv = np.linalg.inv(A)
print(A_inv)

A = np.matrix([[1, 2, 3, 4], [3, -1, 2, 5], [1, 2, 3, 4], [1, 3, 4, 5]])
rank = np.linalg.matrix_rank(A)
print(rank)

A = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
B = np.matrix([[-2], [-1], [0]])
print('A= ', A)
print('B= ', B)
A_inv = np.linalg.inv(A)
print(A_inv)
x = A_inv.dot(B)
print('x= ', x)

a = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
print('A= ', a)
b = np.matrix([[-2], [-1], [0]])
print('B= ', b)


def kramer(a, b):
    a_det = np.linalg.det(a)
    print('Детермінант матриці = ', a_det)
    if (a_det != 0):
        print('Розв*язуємо систему')
        x_m = np.matrix(a)
        x_m[:, 0] = b
        print('x_m', x_m)
        y_m = np.matrix(a)
        y_m[:, 1] = b
        print('y_m', y_m)
        z_m = np.matrix(a)
        z_m[:, 2] = b
        print('z_m', z_m)
        x = np.linalg.det(x_m)/a_det
        y = np.linalg.det(y_m)/a_det
        z = np.linalg.det(z_m)/a_det
        print('X= ', round(x, 5))
        print('Y= ', round(y, 5))
        print('Z= ', round(z, 5))
    else:
        print('Розв*язків немає')


kramer(a, b)
X = np.linalg.solve(a, b)
print('Перевірка Х= ', X)

len_mass = int(input('Enter M: '))
len_elem = int(input('Enter N: '))
a, b = -10, 10
mass = [[random.randint(a, b) for _ in range(len_elem)]
        for _ in range(len_mass)]


def print_matrix(mass):
    for arr in mass:
        print(*arr, ser='\t')


print_matrix(mass)
res = []
for line in mass[1::3]:
    res.extend(line[1::3])
print(sum(res)/len(res))
