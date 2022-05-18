# import random

# s = "abczawefwgwee GF aaawdawFGW aertjbkrt 4325 *(@#!$% efkjerfQWK"
# letters = [0] * 26
# for i in s.lower():
#     if i >= "a" and i <= "z":
#         nomer = ord(i) - 97
#         letters[nomer] += 1
#
# for i in range(26):
#     if letters[i] > 0:
#         print(chr(i + 97) * letters[i], end="")  #подсчёт и определение
#         # букв по алфавиту и сколько их

# a = [2, 1, 2, 3, 4, 2, 3, 3, 4, 0, 2, 3, 3, 4, 5, 4, 2]
# count = [0] * 6
# for i in a:
#     count[i] += 1
# print(count)
# for i in range(6):  # подсчёт сколько раз встретилась та или другая цифра
#     if count[i] > 0:
#         print((str(i) + " ") * count[i], end=" ")

# a = []
#
# for i in range(10):
#     a.append(random.randint(-10, 10))
#
# count = [0] * 21
#
# for i in a:
#     count[i + 10] += 1
# print(a)
#
# for i in range(21):
#     print(i - 10, count[i])
