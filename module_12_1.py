

import numpy as np
print("***NumPy***")
"""Numpy  is a Python library that provides a multidimensional array object,
various derived objects (such as masked arrays and matrices),
and an assortment of routines for fast operations on arrays,
including mathematical, logical, shape manipulation, sorting, selecting,
I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations,
random simulation and much more."""

#print(help(numpy))
#3D массив
a3D = np.array([[1, 2, 5 ], [3, 4, 7], [5, 6, 9]])
print("3D массив: \n", a3D)
print("Число осей: ", a3D.ndim, ", форма:", a3D.shape)
print("Максимальный элемент в массиве:", np.amax(a3D))
print("Первый элемент", a3D[(0, 0)], "Посдедний ", a3D[(2, 2)])

poly = np.polynomial.polynomial.Polynomial((1, 2, 3), symbol = "x")
print("Полином:", poly, "После интегрирования ", poly.integ(1))

i = np.intc(-1)
print(i, type(i), np.intc.__mro__)


"""Requests allows you to send HTTP/1.1 requests extremely easily"""
print("\n***Requests***\n")

import requests as rq

r_put = rq.put('https://httpbin.org/put', data ={"Requests" : "Test put"})
print(r_put.text)
r_get = rq.get('https://httpbin.org/get')
print(r_get.json())

print("\n***Matplotlib***\n")

import matplotlib.pyplot as plt

"""Matplotlib library for creating static, animated, and interactive visualizations"""

x = np.linspace(0, 4, 9)
z = np.random.randint(0, 4, 9)
print(x)
fig, ax = plt.subplots()
ax.set_xlabel('test x')  # Add an x-label to the Axes.
ax.set_ylabel('test y')  # Add a y-label to the Axes.
ax.set_title("Simple plot")  # Add a title to the Axes.
ax.plot(x, z, label='random')
ax.plot(x, x, label='linear')
ax.legend()
plt.show()