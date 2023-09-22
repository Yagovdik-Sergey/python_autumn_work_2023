import random
first = int(input("Введите число начала отрезка генерации случайного списка: "))
last = int(input('Введите число конца отрезка генерации случайного списка: '))
if first >= last:
    print('Первое число должно быть больше второго')
else:
    if last - first < 10:
        lst = random.sample(range(first, last + 1), (last + 1) - first)
        print(lst)
        min_number = lst[0]
        for i in range(len(lst)):
            if lst[i] < min_number:
                min_number = lst[i]
        print(f'Наименьший элемент: {min_number}')
    else:
        lst = random.sample(range(first, last + 1), 10)
        print(lst)
        min_number = lst[0]
        for i in range(len(lst)):
            if lst[i] < min_number:
                min_number = lst[i]
        print(f'Наименьший элемент: {min_number}')
