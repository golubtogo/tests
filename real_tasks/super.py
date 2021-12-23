class A:
    def __init__(self):
        print("In class A")


class B(A):
    def __init__(self):
        super().__init__()
        print("In class B")

b = B()
