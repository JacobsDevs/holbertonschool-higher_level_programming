#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None
    translation = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    processed = False
    length = len(roman_string)
    for i, v in enumerate(roman_string):
        if processed:
            processed = False
            continue
        if i + 1 < length and translation[v] < translation[roman_string[i + 1]]:
            res += translation[roman_string[i + 1]] - translation[v]
            processed = True
        else:
            res += translation[v]
    return res
