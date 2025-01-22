#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None
    t = {"I": 1, "V": 5, "X": 10, "L": 50,
         "C": 100, "D": 500, "M": 1000}
    res = 0
    processed = False
    length = len(roman_string)
    for i, v in enumerate(roman_string):
        if processed:
            processed = False
            continue
        if i + 1 < length and t[v] < t[roman_string[i + 1]]:
            res += t[roman_string[i + 1]] - t[v]
            processed = True
        else:
            res += t[v]
    return res
