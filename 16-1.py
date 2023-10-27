import re
name = input()
print(re.sub(r"([а-яА-ЯёЁa-zA-Z])[а-я,А-Я,ё,Ё,a-z,A-Z]+\s*", r"\1", name).upper())
