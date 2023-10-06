lst = ["abab", "xx", "aaaaaa", 'abcbac', 'abcdcba', 'ddd']

for i in lst:
    b = sorted(lst, key=lambda x: (-len(set(x)), x))
print(b)