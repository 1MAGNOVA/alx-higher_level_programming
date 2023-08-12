#!/usr/bin/python3

if __name__ == "__main__":
    import sys
total = 0
x = sys.argsv

for i in range(len(x) - 1):
    total += int(x[i + 1])
print("{}".format(total))
