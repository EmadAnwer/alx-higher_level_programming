#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rez = a / b
    except (ZeroDivisionError):
        rez = None
    finally:
        print("Inside result: {}".format(rez))
        return rez
