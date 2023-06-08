#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    print("{:d} arguments{:s}".format(count, '.' if count == 0 else ':'))
    for i in range(count):
        print("{:d}: {:s}".format(i + 1, argv[i + 1]))
