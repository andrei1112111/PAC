import numpy as np
from numpy.ma.core import count

print("""Task 1""")

a = np.array([[1, 2, 1], [4, 2, 2], [7, 8, 9]])

unique_elements, frequency = np.unique(a, return_counts=True)
sorted_indexes = np.argsort(frequency)[::-1]
b = unique_elements[sorted_indexes]

print(b)

print("""Task 2""")

h = 3
w = 2

img = np.random.randint(256, size=(h, w))

print(count(np.unique(img)))

print("""Task 3""")

data = np.random.randint(256, size=10)

print(data)

window_size = 3
window = np.ones(window_size) / window_size
print(window)
moving_average = np.convolve(data, window, 'valid')

print(moving_average)

print("""Task 4""")

n = 10

ar = np.random.randint(256, size=(n, 3))

for i in ar:
    si = sorted(i)
    if si[2] >= si[1] + si[0]:
        print(i)

print("""Task 5""")

"""
3x + 4y + 2z = 17
5x + 2y + 3z = 23
4x + 3y + 2z = 19
"""
arr = np.matrix("3 4 2 17; 5 2 3 23; 4 3 2 19", dtype=float)
print(arr)
# second
c = arr[1, 0] / arr[0, 0]
arr[0] *= c
arr[1] -= arr[0]
# third
c = arr[2, 0] / arr[0, 0]
arr[0] *= c
arr[2] -= arr[0]

c = arr[2, 1] / arr[1, 1]
arr[1] *= c
arr[2] -= arr[1]

print(arr)

z = arr[2, 3] / arr[2, 2]
y = arr[1, 3] / (arr[1, 2] * z + arr[1, 1])
x = arr[0, 3] / (arr[0, 2] * z + arr[0, 1] * y + arr[0, 0])

print(x, y, z)

print("""Task 6""")

"""
A = U * Sigma * V^(-1)
"""

A = np.matrix("1 0 1; 0 1 0; 1 0 1")

U, Sigma, V = np.linalg.svd(A)
