def func():
    n = 1
    while True:
        for _ in range(1):
            if n % 2 == 0:
                yield -n
            else:
                yield n
        n += 1


g = func()
for i in range(20):
    print(next(g), end=' ')
