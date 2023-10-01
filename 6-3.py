n = input()
all_letters = list('abcdefghijklmnopqrstuvwxyz')
all_digits = list('0123456789')
letters = []
digits = []
symbols = []
for i in n:
    if i in all_letters and i not in letters:
        letters.append(i)
    elif i in all_digits and i not in digits:
        digits.append(i)
    elif i not in symbols and i not in letters and i not in digits:
        symbols.append(i)

print(' '.join(letters))
print(' '.join(digits))
print(' '.join(symbols))

