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

    @staticmethod
    def _static():
        print("static")


counter = Counter()
# counter == self
counter.inc()
counter._static()
print(counter.value)


Counter.inc(counter)
Counter._static()

print(counter.value)
