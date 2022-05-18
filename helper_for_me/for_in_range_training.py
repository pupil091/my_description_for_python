#
#
#
# abe = list(range(1, 102, 10))
# print(abe)
#
# abr = sum(range(1, 101))
# print(abr)
#
# abt = len(range(5, 15, 5))  # сколько чисел в
# # последовательности невключительно
# print(abt)
#
# a, b, c = range(5, 8)
# print(a, b, c)
#
# ter = range(1, 7)
# len(ter)
#
# yeah = iter(range(5))
# print(yeah)
#
# # next(yeah)
#
# qwe = iter([11, True, "Alloha"])
# qwe.__next__()
#
# qwe.__next__()
#
# qwe.__next__()  # почему не даёт поочерёдно все элементы пролистать?


# for a in range(100, 1000):
#     if a % 2 == 0 and a % 7 == 0:
#         print(a) - в цикле поиск чётных и нечётных

# s = 0
# for a in range(1, 6):
#     s += a
#     print(s) - сложение с
#
# pr = 1
# for i in range(1, 5):
#     pr *= i
# print(pr)  - произведение на


# n = int(input())
# pr = 1
# for i in range(1, n + 1):
#     pr *= i
# print(pr) - факториал ЭННого числа

# n = int(input())
# for i in range(n):
#     print("HABUBARA")
#

# s = 0
# n = int(input())
# for i in range(n):
#     a = randint(1, 10)
#     s += a
#     print(a, end=" ")
# print()
# # print(s)    - рандомная сумма решение


# for i in range(1, 11):
#     print("*" * i)
#     print(2 ** i)
#

# n = int(input())
# s = 0
# for i in range(n):
#    a = int(input())
#    s += a
#    print("current s:", s) - сумма
# print("total", s) - максимальная сумма
# print("middle ariph=", s / n) - среднее арифметическое


# a = [123, 124, 1553, 5234, 234]
# count = 0
# for i in a:
#     print(i)  # - присваивание значение списка а - нное значение
#     count += 1
#     print(count, "Obhod")
#     input() - #прокрутка списка по нумерации, делается столько раз
#     # сколько элементов в списке
#


# a = [1231, 1231, 123453, 352345, 234234, 23423]
# count = 0
# for i in a:
#     i += 5
#     print(i) - #делаем операцию в i над копией значения из а
# print(a)


# a = [1231, 424, 23, 12, 24]
# count = 0
# for i in a:
#     print(i, a.index(i)) - #нумерация (способ) / обход по значению
#     #нельзя изменить, не точно, если есть одинаковые значения
#

# a = [13, 14, 113, 13, 12, 14]
# n = len(a)
# for i in range(n):
#     print(i, a[i])  # достоверный способ проверить список циклом
#     a[i] += 5
# print(a)      #обход по индексу лучше чем по значению


# a = [1, 4, 1, 2, 4, 5, 2, 43, 5, 3, 2, 45, 1, 3, 2, 4, 5]
# b = []
# for i in a:
#     if not i in b:
#         b.append(i)
# print(b)# как сделать список без повторений, мнимое удаление повторений


# a = [1, 3, 4, 2, 54, 1, 2, 34, 54, 21, 3, 1, 245]
# even = []
# uneven = []
# n = len(a)
# for i in range(n):
#     if a[i] % 2 == 0:
#         even.append(i + 1)
#     else:
#         uneven.append(i + 1)
# print(even)
# print(uneven)  # определение чётных и нечётных чисел по индексам


# s = "Check You Knowledge"
# for i in s:
#     if i >= "a" and i < "z":
#         print(i, "small")
#     elif "A" <= i <= "Z":
#         print(i, "big")
#     else:
#         print(i) # проверка строки на большие и маленькие буквы


# vowels = "aeiou"
# s = "aertiooikjoaikl"
# n = len(s)
# # (((s[1]-->s[2]
# # s[3]-->s[4]
# #
# # s[i]-->s[i+1])))
#
# for i in range(n - 1):
#     if s[i] in vowels and s[i + 1] in vowels:
#         print(s[i], s[i + 1])  # проверка на гласные
