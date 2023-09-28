n = int(input())
triangle = []
for i in range(n):
    triangle.append([])
    triangle[i].append(1)
    for j in range(1, i):
        triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    if n != 0:
        triangle[i].append(1)
for i in range(n):
    print(" " * (n - i), end=" ", sep=" ")
    for j in range(i + 1):
        print('{:1}'.format(triangle[i][j]), end=" ", sep=" ")
    print()
