if 5 > 5:
    print(1)
    # чтобы выполнилось следующее условие - н
    # нужно чтобы предыдущее условие было ложное False
    print(2)
elif 3 > 2:
    print(3)
    print(4)
elif 6 > 4:
    print(5)
    print(6)


class Training:
    @staticmethod
    def _outer_1(number):
        black_hole = int(number)
        if black_hole == 1:
            print("collapse")
        elif black_hole == 2:
            print("nuclear blow")
        else:
            print("worse atoms")

    @staticmethod
    def _outer_2(number):
        day = int(number)
        if day == 1:
            print("Monday")
        elif day == 2:
            print("Tuesday")
        elif day == 3:
            print("Wednesday")
        elif day == 4:
            print("Thursday")
        elif day == 5:
            print("Friday")
        elif day == 6:
            print("Saturday")
        elif day == 7:
            print("Sunday")
        else:
            print("Something wrong is incoming")

    def outer_3(self, o):
        one_digit = int(o)  # input num in "box"
        if one_digit < 0 or one_digit >= 1000:
            print("Alert, RETARD ALERT!")
        elif one_digit < 10:
            if one_digit % 2 == 0:
                self._outer_1(11)
            else:
                self._outer_2(6)
        elif one_digit < 100:
            print("2 digit")
        elif one_digit < 1000:
            print("3 digit")


box = Training()
box.outer_3(23242)  # call the func from class

Training().outer_3(22)  # call the func from class shorter
