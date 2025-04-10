def readMatrix(filename):
    matrix = []

    with open(filename, "r") as file1:
        line = file1.readline()
        while line.split():
            matrix.append(
                [int(i) for i in line.split()]
            )
            line = file1.readline()

    return matrix


class DataScientist:
    def __init__(self):
        self.money = 0

    def take_salary(self, i):
        self.money += i

    def do_work(self, filename1, filename2):
        pass


class Pupa(DataScientist):
    def __init__(self):
        super().__init__()

    def do_work(self, filename1, filename2):
        for st1, st2 in zip(readMatrix(filename1), readMatrix(filename2)):
            for i1, i2 in zip(st1, st2):
                print(i1 + i2, end=" ")
            print()


class Lupa(DataScientist):
    def __init__(self):
        super().__init__()

    def do_work(self, filename1, filename2):
        for st1, st2 in zip(readMatrix(filename1), readMatrix(filename2)):
            for i1, i2 in zip(st1, st2):
                print(i1 - i2, end=" ")
            print()


class Accountant:
    def __init__(self, salary=2):
        self.salary = salary

    def give_salary(self, worker):
        if isinstance(worker, Pupa) or isinstance(worker, Lupa):
            worker.take_salary(self.salary)


p1 = Pupa()
l1 = Lupa()
a1 = Accountant()

print(p1.money, l1.money)

a1.give_salary(p1)
a1.give_salary(p1)
a1.give_salary(l1)

print(p1.money, l1.money)

p1.do_work("matrix1.txt", "matrix1.txt")
l1.do_work("matrix1.txt", "matrix1.txt")


