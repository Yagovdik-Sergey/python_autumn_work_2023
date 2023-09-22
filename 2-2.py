import random
lst = random.sample(range(1, 50), 10)
print(lst)
min_number = lst[0]
for i in range(len(lst)):
    if lst[i] < min_number:
        min_number = lst[i]
print(f'Наименьший элемент: {min_number}')
