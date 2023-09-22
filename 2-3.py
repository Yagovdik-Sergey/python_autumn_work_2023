n = int(input())
fact = n
if n < 0:
    print("Факториала отрицательного числа не существует")
elif n == 0:
    print(1)
else:
    for i in range(1, n):
        fact = fact * i
    print(fact)