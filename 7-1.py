def LCM(lst):
    from math import gcd
    lcm = 1
    for i in lst:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


print(LCM([10, 15, 30, 64]))
print(LCM([72, 80, 96]))
print(LCM([75, 120]))
