# class Soda:
#     def __init__(self, berry):
#         if isinstance(berry, str):
#             self.berry = berry
#         else:
#             self.berry = None
#
#     def show_my_drink(self):
#         if self.berry:
#             print(f'Soda mit {self.berry}')
#         else:
#             print('Soda for your mom')
#
#
# x = Soda()
# x.show_my_drink()


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        list_item = [self.a, self.b, self.c]
        for item in list_item:
            if item == str:
                print("Нужно вводить только числа!")
                break
            if item < 0:
                print("С отрицательными числами ничего не выйдет!")
            elif self.a >= self.b + self.c and self.b >= self.a + self.c and self.c >= self.a + self.b:
                print("Жаль, но из этого треугольник не сделать")
            elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                print("Ура, можно построить треугольник!")


# triangle_side = TriangleChecker(1, 99, 415345)
# print(triangle_side.is_triangle())
triangle1 = TriangleChecker(1, 78, 78)
print(triangle1.is_triangle())

# def is_triangle(self):
#     if all(isinstance(side, (int, float)) for side in self.sides):
#         if all(side > 0 for side in self.sides):
#             sorted_sides = sorted(self.sides)
#             if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
#                 return 'Ура, можно построить треугольник!'
#             return 'Жаль, но из этого треугольник не сделать'
#         return 'С отрицательными числами ничего не выйдет!'
#     return 'Нужно вводить только числа!'
#

# x = TriangleChecker()
# x.is_triangle(1, 2, 4)
#
# b = TriangleChecker()
# b.sides(1, 2, 4)

# a = int(input("Введите длину первого отрезка: "))
# b = int(input("Введите длину первого отрезка: "))
# c = int(input("Введите длину первого отрезка: "))
# a.isdigit()
# b.isdigit()
# c.isdigit()
#
# if a >= b + c:
#     print("Жаль, но из этого треугольник не сделать")
# elif b >= a + c:
#     print("Жаль, но из этого треугольник не сделать")
# elif c >= a + b:
#     print("Жаль, но из этого треугольник не сделать")
# else:
#     print("Ура, можно построить треугольник!")
#
# return 'С отрицательными числами ничего не выйдет!'
# return 'Нужно вводить только числа!'
