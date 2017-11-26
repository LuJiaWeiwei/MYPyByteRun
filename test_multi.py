class A():
    def __init__(self, k):
        self.k = k

    def  __mod__(self, other):
        return  self.k * other.k



a = A(1)
b = A(2)
x = 1
y = 2
print(a.__mod__(b))
print(x % y)
print(a.__mod__(b))
