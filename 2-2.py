import random
lst = random.sample(range(1, 50), 10)
print(lst)
min = lst[0]
for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
print(f'Наименьший элемент: {min}')
