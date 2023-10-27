import re
name = input()
print(re.sub(r"([а-яА-Яa-zA-Z])[а-я,А-Я,a-z,A-Z]+\s*", r"\1", name).upper())
