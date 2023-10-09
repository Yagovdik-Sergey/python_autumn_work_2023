lst = "Мама мыла раму".lower()
rez = {}
for i in lst:
    if rez.get(i, None):
        rez[i] += 1
    else:
        rez[i] = 1
rez_sorted = sorted(rez.items(), key=lambda x: (-x[1], x))
dct = dict(rez_sorted)
first_10 = {k: dct[k] for k in list(dct)[:10]}
print(first_10)
