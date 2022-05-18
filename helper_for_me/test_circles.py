number_range1 = list(range(1, 200, 10))
number_range2 = list(range(1, 200, 20))
PPP = number_range1, number_range2


def get_foo(a):
    iii = PPP[a]
    for number2 in iii:
        data = 1 + number2
        if data == 2:
            print('fuck you')
        else:
            print('ok')


get_foo(0)

get_foo(1)

data_list = list(range(0, 150, 15))

data_tuple = tuple(range(1, 100, 5))


def data_change(hubl_list, bubl_list):
    for hubl in hubl_list:
        for bubl in bubl_list:
            key = 10 - hubl + bubl
            key_ok = key <= 0
            print(key)
            if key_ok:
                print('worse')
            else:
                print('right')
            if key == 201:
                print('almost right')
            if key == 216:
                print('definitely worst')


data_change(data_list, data_tuple)

x = lambda t: 2 ** t
print(x(5))

print(list(filter(lambda a: a * 2 == 8, [1, 3, 5, 4, 645, 2 + 2])))

intelligence = 10

while intelligence >= 3:
    print(intelligence)
    intelligence -= 1
