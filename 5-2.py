k = int(input())
n = 1
lst = []
while n <= k:
    if k % n == 0:
        lst.append(n)
    n = n + 1
print(f'Делители числа {k}: {", ".join(str(i) for i in lst)}')
