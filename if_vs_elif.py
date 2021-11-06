#!/usr/bin/env python3
"""
Demonstrating elif vs if
"""

import sys, datetime

var = 0
time_stamp = datetime.datetime.now()

# hello world


hello = "hello " + "world"

if var == 0:
    if True:
        print("zero" + "to" + "hero")
        print(time_stamp)

# -------------------
# if these two are elif's, only "one" prints
# if these two are if's, "one" and "two" will print
elif var == 1:
    print("one")
elif var == 1:
    print("two")
# -------------------

if var == 3:
    print("three")
else:
    print("Enter 0-3")
