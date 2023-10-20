def tri_2(n):
    if n < 1:
        return
    for i in range(0, n):
        print("*", end=" ")
    print("\n", end="")

    tri_2(n - 1)
    if n < 2:
        return
    for i in range(0, n):
        print("*", end=" ")
    print("\n", end="")


tri_2(5)
