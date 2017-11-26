def f():
    b = 0
    a = 1
    while b < a:
        yield a
        a, b = a + b, a


for i in range(5):
    print(f())
