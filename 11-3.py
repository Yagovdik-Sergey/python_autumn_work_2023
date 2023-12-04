def arabic_to_roman(num):
    if not 0 < num < 4000:
        raise ValueError("Число должно быть в пределах от 1 до 3999")

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value

    return result

arabic_number = int(input())
roman_number = arabic_to_roman(arabic_number)
print(f"{arabic_number} -> {roman_number}")
