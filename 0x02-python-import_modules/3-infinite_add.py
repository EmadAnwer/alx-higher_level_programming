#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    count = len(argv) - 1
    # add all arguments in sum variable
    for i in range(count):
        sum += int(argv[i + 1])
    # print sum
    print("{:d}".format(sum))
