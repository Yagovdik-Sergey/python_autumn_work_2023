def func(n):
    for x in range(1, n + 1):
        if x % 2 == 0:
            yield -x
        else:
            yield x


g = func(23)
for i in g:
    print(i, end=' ')
