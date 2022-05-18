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
