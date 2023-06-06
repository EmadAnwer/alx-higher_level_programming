#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format((65 + (i - 97))
                        if (((123 - i) % 2) == 0) else i), end="")
