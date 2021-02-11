#!/usr/bin/env python3
"""Hashing functions"""

import math

# import functions here will be implicit when functions below are imported


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key % size


# def hash_mid_sqr(key: int, size: int) -> int:
#     """Find hash using mid-square method"""
#     # Method will work for x such that x**2 is less than 10000
#     if key**2 < 100:
#         mid_square = key **2
#     else:
#         mid_square = ((key **2) // 10) % 100
#     return (mid_square % size)


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    # This method will work for all integers up until max out int methods
    # Better:  think of how to do this with mathematical formulas, in general
    # Logic:  obtain length of integer:  k.  Use floor(math.log10(k))+1
    # Remove k-2 / 2 digits at each end.
    # to do this, use // and %, with the denominator set by k-2 /2
    # Example 123456.  Seek 34.  Len = 6.  Remove 2 from left, 2 from right.
    # To remove 2 from left, do 123456 % 10000.  So, denom = 10**(k-2)
    # To remove 2 from right, do 3456 // 100.  So, denom = 10 ** (k-2)
    # What if odd number of digits?  1234567?  Target is still 34.
    # To obtain, denom = 10 ** (k-2)
    diglen = math.floor(math.log10(key ** 2)) + 1
    if diglen < 3:
        mid_square = key ** 2
    elif diglen % 2 == 0:
        ldigits = (key ** 2) // (10 ** (diglen // 2 - 1))
        mid_square = ldigits % (10 ** (diglen // 2))
    else:
        ldigits = (key ** 2) // (10 ** (diglen // 2))
        if round(math.log10(ldigits) - 0.5, 0) > 1:
            mid_square = ldigits % (10 ** (diglen // 2 - 1))
        else:
            mid_square = ldigits
    return mid_square % size


def hash_folding(key: str, size: int) -> int:
    """Find hash using folding method"""
    # Assumes numbers are separated by "-" within string.
    # new_key = key.replace("-", "")
    # Note:  import functions can be placed in functions - will be automatic in test.
    # new_key = re.sub('[^0-9]', '', key) # attempt to use regular expression to strip strings

    ctr = 0
    hashtot = 0
    new_key = ""
    while ctr < len(key):
        if key[ctr : ctr + 1].isdigit():
            new_key = new_key + key[ctr : ctr + 1]
        ctr += 1
    print(new_key)
    ctr = 0
    while ctr < len(new_key):
        intc1 = new_key[ctr : ctr + 1]
        if ctr + 1 < len(new_key):
            intc2 = new_key[ctr + 1 : ctr + 2]
        else:
            intc2 = ""
        intstr = f"{intc1}{intc2}"
        hashtot = int(intstr) + hashtot
        ctr += 2
    return hashtot % size


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    charsum = 0
    for ctr in range(len(key)):
        char = key[ctr : ctr + 1]
        charsum = charsum + ord(char)
    return charsum % size


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    # Note test file starts weights at 0 rather than at 1, unlike text.
    charsum = 0
    for ctr in range(len(key)):
        char = key[ctr : ctr + 1]
        charsum = charsum + (ord(char) * (ctr))
    return charsum % size
