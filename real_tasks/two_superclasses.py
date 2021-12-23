"""
Создать два суперкласса
"""


class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1


class SecondCounter():
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 2


class LastCounter(Counter, SecondCounter):
    pass


def inc_value():
    counter = LastCounter()
    counter.inc()
    return counter.value


print(inc_value())