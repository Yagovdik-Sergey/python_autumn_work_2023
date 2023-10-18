def func(def_lst):
    for n in def_lst:
        for i in range(1):
            if n % 2 == 1:
                yield n
        n += 1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
g = func(lst)
for i in range(len(lst)):
    try:
        print(next(g), end=' ')
    except StopIteration:
        break
