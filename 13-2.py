def func():
    n = 1
    while True:
        for _ in range(1):
            if str(n) == str(n)[::-1]:
                yield n
        n += 1


g = func()
for i in range(200):
    print(next(g), end=' ')
