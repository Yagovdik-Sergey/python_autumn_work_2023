n = float(input())
lst = []
s = 0
while n != 0:
    s += n
    lst.append(n)
    n = float(input())
print(s / len(lst))
