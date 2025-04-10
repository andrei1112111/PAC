class Queue(list):
    def __init__(self):
        super().__init__()
        self.__queue = []

    def get(self):
        if len(self.__queue) == 0:
            return None

        elem = self.__queue[0]
        self.__queue = self.__queue[1:]

        return elem

    def put(self, elem):
        self.__queue.append(elem)

    def get_all(self):
        return self.__queue.copy()


class Stack(list):
    def __init__(self):
        super().__init__()
        self.__stack = []

    def get(self):
        if len(self.__stack) == 0:
            return None

        elem = self.__stack[-1]
        self.__stack = self.__stack[:-1]

        return elem

    def put(self, elem):
        self.__stack.append(elem)

    def get_all(self):
        return self.__stack.copy()


a = Queue()
# a.__queue.append(123)
a.get()
print(a.get_all())
a.put(1)
a.put(2)
print(a.get_all())
a.get()
print(a.get_all())

s = a.get_all()
print(a.get_all())

s.append(999)

print(s)
print(a.get_all())
