from packageExample import *
from independent_module import add
from abc import ABC, abstractmethod


# Abstract Base Class example
class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


# Property example
class Point(Drawable):

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y


    @property
    def x(self) -> float:
        return self._x


    @x.setter
    def x(self, x: float) -> None:
        self._x = x


    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float) -> None:
        self._y = y


    def draw(self):
        print("X:", self._x, "Y:", self._y)


if __name__ == "__main__":
    # Importing from independent module example
    print(add(1, 2))

    # Importing from package with __all__ variable set example
    print(module1.function_a())
    print(module2.function_b())

    try:
        print(module3.function_c())
    except NameError:
        print("You need to explicitly import module3!")

    # Relative importing is inside module3
    from packageExample import module3
    print(module3.relative_import())

    # Property and ABC demon
    point = Point(2.0, 2.0)
    point.draw()
