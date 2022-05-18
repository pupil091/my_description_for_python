# def while_train():
#     cre = int(input())
#     key = 1
#     while key <= cre // 2:
#         if cre % key == 0:
#             print(key, end=" ")
#     key += 1  # как найти делитель, не понимаю почему не работает
#
#
# # 23235
# # 235235235235
# # 235235
# #
# #
#
#
# a = 1
#
# while a < 10:
#     print('Цикл выполнился', a, 'раз(а)')
#     a += 1
# print('Цикл окончен')
#
# a = 1
#
# while a == 1:
#     b = input('Как тебя зовут?')
#     print('Привет', b, ', Добро пожаловать')
#     break
# print("STOP IT!")
#
# # 34335
# # ddrgd
# # 34635tergdfth
#
#
# ac = 1
# while ac < 5:
#     print('условие верно')
#     ac += 1
# else:
#     print('условие неверно')
# # DOESNOT WORK!
#
#
# adf = 1
# while adf < 5:
#     adf += 1
#     if adf == 3:
#         break
#     print(adf)  # 2
#
# adb = 1
# while adb < 5:
#     adb += 1
#     if adb == 3:
#         continue
#     print(adb)  # 2, 4, 5
#
# xe = 20
#
#
# def run_commands(xe):
#     print(xe)
#
#
# run_commands(xe)
# xe += 1
# while xe <= 10:
#     run_commands(xe)
#     xe += 1
#
# x = 1
#
# while x <= 10:
#     print(x)
#     x += + 1
# else:
#     print("Готово")
#
# # x = 1
# # while x: print(x) - infinite cicle
# #
# # x = 1
# # while x >= 1:
# #     print(x)
#
# xa = 1
# while xa <= 10:
#     if xa == 5:
#         break
#     print(xa)
#     xa += 1
#
# xw = 1
# while xw <= 10:
#     if xw == 5:
#         xw += 1
#         continue
#     print(xw)
#     xw += 1
#
# i = 1
# while i > 0:
#     print("Iteration NUMBER", i)
#     if i == 10:
#         break
#     i += 1
#
# while True:
#     awe = input()
#     if awe == "exit":
#         break
#     if len(awe) < 5:
#         continue
#     print(awe, len(awe))
#
# ultor = 1
# while ultor <= 15:
#     print(ultor)
#     ultor += 1
# else:
#     print("aaaaaa")
#     print("hell yeah")
# print("end")

asd = [12, 14, 114, 1412, 12412]
# if asd % 2 == 0:
#     print("yes")
# else:
#     print("no")
while len(asd) > 0:
    last = asd.pop()
    if last % 2 != 0:
        print('WOOW', last)
        break
else:
    print("YEAH")
