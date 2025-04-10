# import random
# import sys
#
# """
# TASK 1
# """
# st = input()
# if all(
#         [st[i] == st[-(i + 1)] for i in range(len(st))]
#     ):
#     print("Yes")
# else:
#     print("No")
#
#
# """
# TASK 2
# """
# print(
#     max(
#         input().split(),
#         key=lambda x: len(x)
#     )
# )
#
#
# """
# TASK 3
# """
# random.seed(1)
#
# data = [random.randint(-1 * sys.maxsize, sys.maxsize) for _ in range(1000)]
#
# even = sum([
#     i % 2 == 0 for i in data
# ])
#
# print("Четных:", even)
# print("Нечетных:", len(data) - even)
#
#
# """
# TASK 4
# """
# data = {
#     "1": "11",
#     "2": "22"
# }
#
# def repl(word):
#     if word in data.keys():
#         return data[word]
#
#     return word
#
# print(
#     " ".join([
#         repl(w) for w in input().split()
#     ])
# )
#
#
# """
# TASK 5
# """
# def fib(n):
#     if n == 1:
#         return 0
#     if n <= 3:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
#
# """
# TASK 6
# """
# with open("some_text_file.txt") as file:
#     data = file.read()
#     print("Строк:", len(data.split('\n')))
#     print("Слов", len(data.split()))
#     print("Букв:", sum([
#         1 for i in data if 'a' <= i <= 'z' or 'A' <= i <= 'Z'
#     ]))
#

"""
TASK 7
"""
def generate_geometric_progression(a: int, r: int):
    """geometric progression starts from {a}, and each next element is {previous * {r}}"""
    while True:
        yield a
        a *= r

# progression = generate_geometric_progression(2, 2)
# print(next(progression))
# print(next(progression))
# print(next(progression))
#
