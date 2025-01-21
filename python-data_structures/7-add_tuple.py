#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nums = [0, 0]
    for i, v in enumerate(tuple_a):
        if i >= 2:
            pass
        else:
            nums[i] += v
    for i, v in enumerate(tuple_b):
        if i >= 2:
            pass
        else:
            nums[i] += v 
    tup = tuple(nums)
    return tup
