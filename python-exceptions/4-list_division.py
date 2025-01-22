#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = [0] * list_length
    for i in range(list_length):
        res = 0.0
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            results[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            results[i] = 0
            print("division by 0")
        except IndexError:
            results[i] = 0
            print("out of range")
        else:
            results[i] = res
    return results
