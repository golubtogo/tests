class A:
    def rk(self):
        print(f"In class {__class__}")


class B:
    def rk(self):
        print(f"In class {__class__}")


class C(A, B):
    pass


c = C()
c.rk()

