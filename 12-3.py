def parse_ranges(str):
    result = []
    ranges = str.split(',')

    for r in ranges:
        bounds = r.split('-')
        if len(bounds) == 1:
            result.append(int(bounds[0]))
        elif len(bounds) == 2:
            start, end = map(int, bounds)
            result.extend(range(start, end + 1))
        else:
            raise ValueError("Invalid range format")
    return result

str = "1-2,4-4,3-6"
result_list = parse_ranges(str)
print(result_list)
