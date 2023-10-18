def func(n):
    for i in n:
        if i % 2 == 1:
            yield i


lst = [5, 6, 7, 8, 9, 10, 11, 12]
g = func(lst)
for k in g:
    print(k, end=' ')
