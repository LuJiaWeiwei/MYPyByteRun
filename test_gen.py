def f(max):
    b = 0
    a = 1
    n = 0
    while n < max:
        yield a
        a, b = a + b, a
        n = n + 1

for i in f(4):
    print(i)
