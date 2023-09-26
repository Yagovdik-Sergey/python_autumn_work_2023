x = input()
y = input()
dct_x = {}
dct_y = {}
a = ['.', ',', ' ', '!', '?', ';', ':', '-', '\'', '\"',  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(len(x)):
    if x[i] not in a:
        dct_x[x[i].lower()] = dct_x.get(x[i].lower(), 0) + 1
    else:
        continue
for i in range(len(y)):
    if y[i] not in a:
        dct_y[y[i].lower()] = dct_y.get(y[i].lower(), 0) + 1
    else:
        continue
print(dct_y == dct_x)