#!/usr/bin/env python
"""happy_numbers.py

Determine whether a number is happy or not, and find the
first 8 happy numbers. All unhappy numbers eventually reach
the 8-digit cycle of 4, 16, 37, 58, 89, 145, 42, 20, 4,
so any numbers that reach this cycle are false, and any
that find 1 are true."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

def get_sum_of_squares(n):
    # get n as array of digits
    n = list(str(n))
    for i in range(len(n)):
        n[i] = (int)(n[i])

    # get sum of sqaures
    sum = 0
    for digit in n:
        sum += digit**2

    return sum

def is_happy(n):
    # sequence entered by all unhappy numbers
    unhappy = [4, 16, 37, 58, 89, 145, 42, 20]
    while(True):
        if n == 1:
            return True
        elif n in unhappy:
            return False
        else:
            n = get_sum_of_squares(n)
            return is_happy(n)

def main():
    # get and validate input
    try:
        n = (int)(sys.argv[1])
        if(n > 1000):
            raise ValueError
        elif n < 1:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: happy_numbers.py [n]")
        print("[n] is a natural number below 1000")
        sys.exit(1)

    # is this number happy?
    if(is_happy(n)):
        print("{} is a happy number.".format(n))
    else:
        print("{} is not a happy number.".format(n))
    print
    
    # print first 10 happy numbers
    happy = []
    i = 1
    while(len(happy) < 10):
        if is_happy(i):
            happy.append(i)
            i += 1
        else:
            i += 1
    print("The first 10 happy numbers are:")
    print(happy)



if __name__ == "__main__":
    main()
