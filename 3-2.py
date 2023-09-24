n = abs(int(input()))
ind = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count = [0] * 10
for i in str(n):
    count[int(i)] += 1
for i in range(10):
    print(f'{ind[i]} - {count[i]}')
