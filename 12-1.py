def find_min_max_indices(lst):
    if not lst:
        return [], []
    min_val = min(lst)
    max_val = max(lst)
    min_indices = [index for index, value in enumerate(lst) if value == min_val]
    max_indices = [index for index, value in enumerate(lst) if value == max_val]
    return min_indices, max_indices

my_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
min_indices, max_indices = find_min_max_indices(my_list)

print("Индексы минимальных элементов:", min_indices)
print("Индексы максимальных элементов:", max_indices)
