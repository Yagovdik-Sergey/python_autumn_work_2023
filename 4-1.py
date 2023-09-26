s = input().split()
input_first, operator, input_second = s
first, second = int(input_first), int(input_second)
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
else:
    if second != 0:
        print(first / second)
    else:
        print('На ноль делить нельзя!')
