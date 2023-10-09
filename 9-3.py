lst = "Мама мыла раму".lower()
rez = {}
for i in lst:
    if rez.get(i, None):
        rez[i] += 1
    else:
        rez[i] = 1
rez_sorted = sorted(rez.items(), key=lambda x: (-x[1], x))
dct = dict(rez_sorted)
for i in dct:
    print(f'{i} - {dct[i]}')
