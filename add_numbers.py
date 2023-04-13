#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("Usage: {} num1 num2".format(sys.argv[0]))
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
result = num1 + num2
print(result)
