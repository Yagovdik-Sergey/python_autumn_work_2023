def find_values(dct, X):
    values = []
    if X in dct:
        values.append(dct[X])
    for key, value in dct.items():
        if isinstance(value, dict):
            values.extend(find_values(value, X))
    return values

sample_dict = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}

key_to_find = 1
result = find_values(sample_dict, key_to_find)

if result:
    print(result)
else:
    print(f"Ключ '{key_to_find}' не найден.")
