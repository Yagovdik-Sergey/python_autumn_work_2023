x = int(input())
y = int(input())
sum = x + y
sub = x - y
multi = x * y
div = x / y
floor_div = x // y
list = [sum, sub, multi, div, floor_div]
max_number = max(list)
list.remove(max_number)
max_number_2 = max(list)
print(max_number_2)