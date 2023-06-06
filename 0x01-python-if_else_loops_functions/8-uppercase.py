#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:c}".format(65 + (ord(c) - 97)
                            if ord(c) >= 97 and ord(c) <= 122
                            else ord(c)), end="")
    print("")
