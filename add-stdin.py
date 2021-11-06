#!/usr/bin/env python3

import sys

# Get input from stdin
numbers = [int(n.strip()) for n in sys.stdin]

total = 0

for number in numbers:
    total += number

print(total)
