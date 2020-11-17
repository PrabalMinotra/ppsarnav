
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    # pass
    def met(self):
        print("This is a method from class C")


class D(C, B):
    def met(self):
        print("This is a method from class D")
    # pass

a = A()
b = B()
c = C()
d = D()

d.met()

