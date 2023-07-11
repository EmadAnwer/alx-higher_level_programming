#!/usr/bin/python3

def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data)
