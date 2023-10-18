def func(n):
    for x in range(n + 1):
        if x % 2 == 0:
            yield -x
        else:
            yield x


g = func(24)
for i in g:
    for j in range(24):
        print(next(g), end=' ')
