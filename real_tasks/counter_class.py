"""
Написать тест который проверит что value = 1 
"""


class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1


def test_inc_value():
    counter = Counter()
    counter.inc()
    return counter.value == 1


print(test_inc_value())