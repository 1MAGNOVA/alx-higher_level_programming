#!/usr/bin/python3
"""imports the def add(a, b): from 0-add.py abd prints result of addition"""
if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add
    a = 1
    b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
