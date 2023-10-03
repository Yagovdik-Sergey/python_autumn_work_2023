def max_3(x):
    result = []
    for i in x:
        for k in list(i):
            result.append(k)
    lst_max_3 = sorted(result, reverse=True)[:3]
    return sorted(lst_max_3)
