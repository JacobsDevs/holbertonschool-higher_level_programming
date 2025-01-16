#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = "arguments"
    arg_terminator = ":"
    length = len(argv) - 1
    if length == 1:
        arg = "argument"
    if length == 0:
        arg_terminator = "."
    print("{} {}{}".format(length, arg, arg_terminator))
    counter = 1
    for i in range(length):
        print("{}: {}".format(counter, argv[counter]))
        counter += 1
