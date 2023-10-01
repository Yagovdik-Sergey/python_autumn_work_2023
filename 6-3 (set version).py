n = input()
all_letters = list('abcdefghijklmnopqrstuvwxyz')
all_digits = list('0123456789')
letters = []
digits = []
symbols = []
for i in n:
    if i in all_letters:
        letters.append(i)
    elif i in all_digits:
        digits.append(i)
    elif i not in symbols:
        symbols.append(i)

print(' '.join(set(letters)))
print(' '.join(set(digits)))
print(' '.join(set(symbols)))