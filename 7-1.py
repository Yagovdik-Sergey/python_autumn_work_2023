def factors(n):
    k = 2
    lst = []
    while k <= n:
        if n % k == 0:
            lst.append(k)
            n /= k
        else:
            k += 1
    return lst


first = factors(int(input()))
second = factors(int(input()))
for x in second:
    if x in first:
        first.remove(x)
j = 1
for i in first + second:
    j *= i
print(j)
