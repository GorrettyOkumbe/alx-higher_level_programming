#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    x = "s" if n == 1 or n > 2 else ""
    q = ":" if n > 1 else "."

    print("{:d} arguement{}{}".format(n - 1, x, q))

    for i in range(1, n):
        print("{:d}: {}".format(i, sys.argv[i]))
