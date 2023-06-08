#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    from sys import argv
    count = len(argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operators = ['+', '-', '*', '/']
    functions = [add, sub, mul, div]
    for i in range(4):
        if argv[2] == operators[i]:
            print("{:d} {:s} {:d} = {:d}"
                  .format(a, argv[2], b, functions[i](a, b)))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
