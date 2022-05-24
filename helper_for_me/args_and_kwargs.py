def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("Значение для {} является {}".format(key, value))


print_values(my_name="Sammy", your_name="Casey")


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("Значение для {} является {}".format(key, value))


print_values(
    name_1="Alex",
    name_2="Gray",
    name_3="Harper",
    name_4="Phoenix",
    name_5="Remy",
    name_6="Val"
)
