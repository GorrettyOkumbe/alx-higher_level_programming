#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    number = 0
    total = 0

    roman_digit = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    for x in roman_string[::-1]:
        number = roman_digit[x]
        total += number if total < number * 5 else number
    return number
