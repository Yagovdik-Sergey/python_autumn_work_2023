def from_roman_to_numb(rom):
    basic_romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    last_digit_value = 0
    for i in rom[::-1]:
        digit_value = basic_romans[i]
        if digit_value >= last_digit_value:
            value += digit_value
            last_digit_value = digit_value
        else:
            value -= digit_value
    return value