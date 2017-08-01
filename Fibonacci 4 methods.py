def fib1(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)


def fib3(n):
    c = 0
    a, b = 0, 1
    while True:
        if c > n: return
        yield a
        a, b = b, a + b
        c += 1


def fib4(n):
    a, b = 0, 1
    for i in range(n):
        nex = a + b
        if i <= 1:
            print(i)
        else:
            print(nex)
            a, b = b, nex


print('Method 1:')
fib1(5)
print('Method 2:')
for i in range(5):
    print(fib2(i))
print('Method 3:')
n = fib3(5)
for i in n:
    print(i)
print('Method 4:')
fib4(5)
