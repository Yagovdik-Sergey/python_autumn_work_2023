def func(n):
    odd_numbers = [x for x in n if x % 2 != 0]
    return odd_numbers


lst = [5, 6, 7, 8, 9, 11, 12, 13]
g = func(lst)
print(g)