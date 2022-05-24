from helper_for_me.if_elif_else_description import Training


class TrainingNext(Training):
    def _ono(self, p, o):
        name = [1, 2, 3, 4, 5, 6]
        for i in name:
            if i == p:
                print(i + 1)
            if i == o:
                print('ok')

    def owner_4(self):
        self._ono(1, 2)


box = TrainingNext()
box.owner_4()
*names, = 1, 2, 3, 4, 5, 2, 35, 213
print(names)


class Explosion(object):
    """docstring"""

    def __init__(self, dead, alive, blows):
        """Constructor"""
        self.dead = dead
        self.alive = alive
        self.blows = blows

    def blow(self):
        """
        Blow!!!
        """
        return "Blowing"

    def help(self):
        """
        Helping!
        """
        return "People need some help right now!"


# Прямоугольник.
class Rectangle:
    'Это класс Rectangle'

    # Способ создания объекта (конструктор)
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    # Метод расчета площади.
    def getArea(self):
        return self.width * self.height


r1 = Rectangle(40, 10)
r2 = Rectangle(30, 17)

print("r1.width = ", r1.width)
print("r1.height = ", r1.height)
print("r1.getWidth() = ", r1.getWidth())
print("r1.getArea() = ", r1.getArea())

print("-----------------")

print("r2.width = ", r2.width)
print("r2.height = ", r2.height)
print("r2.getWidth() = ", r2.getWidth())
print("r2.getArea() = ", r2.getArea())
