class A:
    class_field = 4

    def __init__(self):
        self.value = 1
        self.two = None
        print("in class A")

    def inc(self):
        print(self.class_field)


class B(A):
    def __init__(self):
        super().__init__()
        print("In class B")


print(B.class_field)