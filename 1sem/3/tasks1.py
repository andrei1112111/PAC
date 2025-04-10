""""""
from xml.dom import ValidationErr

"""
TASKS 1, 2
"""
class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = max_count

    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    def update_max_count(self, val):
        if val < 0:
            return False
        self._max_count = val
        if val > self._max_count:
            self._count = val
        return True

    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок.
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count

    # Ещё один способ изменить атрибут класса
    @count.setter
    def count(self, val):
        self._count = val
        if val <= self._max_count:
            self._count = val

    @staticmethod
    def static():
        print('I am function')

    @classmethod
    def my_name(cls):
        return cls.__name__

    def __add__(self, num):
        """ Сложение с числом """
        return self.count + num

    def __sub__(self, num):
        return self.count - num

    def __mul__(self, num):
        """ Умножение на число """
        return self.count * num

    def __iadd__(self, num):
        self._count += num

        if self._count > self._max_count:
            self._count = self._max_count
        if self._count < 0:
            self._count = 0

        return self

    def __isub__(self, num):
        self._count -= num

        if self._count > self._max_count:
            self._count = self._max_count
        if self._count < 0:
            self._count = 0

        return self

    def __imul__(self, num):
        self._count *= num

        if self._count > self._max_count:
            self._count = self._max_count
        if self._count < 0:
            self._count = 0

        return self

    def __lt__(self, other):
        """ Сравнение меньше """
        return self.count < other.count

    def __le__(self, other):
        return self.count <= other.count

    def __eq__(self, other):
        return self.count == other.count

    def __ne__(self, other):
        return self.count != other.count

    def __gt__(self, other):
        return self.count > other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __len__(self):
        """ Получение длины объекта """
        return self._count


"""
TASK 3
"""
class Fruit(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Vegetable(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Food(Item):
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self._saturation = saturation

    @property
    def eatable(self):
        return self._saturation > 0


class Apple(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=32, color='green', saturation=10):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def eatable(self):
        return super().eatable and self._ripe


class Banana(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=13, color='yellow', saturation=22):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def eatable(self):
        return super().eatable and self._ripe


class Patato(Vegetable, Food):
    def __init__(self, ripe, count=1, max_count=100, color='yellow', saturation=8):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def eatable(self):
        return super().eatable and self._ripe


class Carrot(Vegetable, Food):
    def __init__(self, ripe, count=1, max_count=90, color='orange', saturation=3):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def eatable(self):
        return super().eatable and self._ripe


"""
TASK 4
"""
class Inventory:
    def __init__(self, length):
        self.__data = [None for _ in range(length)]

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError(f'Index {index} more then {len(self)}')
        return self.__data[index]

    def __len__(self):
        return len(self.__data)

    def add(self, obj, index: int):
        if index < len(self) and self[index] is None:
            if isinstance(obj, Food) and obj.eatable == True:
                self.__data[index] = obj
            else:
                raise ValidationErr(f'Object is not eatable food')
        else:
            raise ValidationErr(f'the inventory cell is already occupied')

    def extract(self, index, count):
        if index < len(self) and self[index] is not None:
            self.__data[index].count -= count

            if self[index].count == 0:
                self.__data[index] = None



i = Inventory(5)
b = Banana(ripe=True, count=2)
c = Carrot(ripe=True)

i.add(b, 1)
# i.add(c, 1)
i.add(c, 2)

i.extract(1, 2)
