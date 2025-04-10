import calendar
import random
import math
import sys
import os

"""
TASK 1
"""
random.seed(1)
print(random.randint(100, 999), end=" sum: ")

random.seed(1)
print(
    sum(
        [int(i) for i in str(random.randint(100, 999))]
    )
)


"""
TASK 2
"""
random.seed(1)
print(random.randint(-1 * sys.maxsize, sys.maxsize), end=" sum: ")

random.seed(1)
print(
    sum(
        [int(i) for i in str(random.randint(-1 * sys.maxsize, sys.maxsize))]
    )
)


"""
TASK 3
"""
r = input("Sphere radius: ")

r = float(r)

print(
    f"Sphere surface: {4 * math.pi * (r ** 2)}"
)

print(
    f"Sphere volume: {4/3 * math.pi * (r ** 3)}"
)


"""
TASK 4
"""
r = int(input("Enter year: "))
print(calendar.isleap(r))


"""
TASK 5
"""
def isPrime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


upper_bound = int(input("Enter range: 1, "))

for i in range(1, upper_bound):
    if isPrime(i):
        print(i, end=" ")
print()


"""
TASK 6
"""
x = int(input("Deposit: "))
y = int(input("Period: "))

for _ in range(y):
    x += x * 0.1

print(f"Deposit amount after {y} years: {x}")


"""
TASK 7
"""
def print_files(tree):
    for i in tree:
        if i[2]:
            print(" ".join(i[2]), end=" ")


# files_tree = os.walk("/Users/andrejalekseevic/study/pytthon")
files_tree = os.walk(input("Enter path: "))
print_files(files_tree)
