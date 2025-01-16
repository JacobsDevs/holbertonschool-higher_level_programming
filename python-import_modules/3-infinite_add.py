#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    result = 0
    counter = 1
    for i in range(length):
        result += int(argv[counter])
        counter += 1
    print("{}".format(result))
