"""String search"""

# CS 190 exercise 1.  Feb 6, 2019.  E. Baack
# Find the first character that is not repeated in a string
# Logic:  create dictionary containing all characters in a string, and the number of occurrences.
# Move through dictionary to find first value == 1; print the associated key.

#!/usr/bin/env python3

A_STRING = "A"+"A"*1000000+"C" + "B" * 100000

def find_non_repeat(A_STRING):
    LEN_A_STRING = len(A_STRING)
    Ctr = 0
    Ltrs = dict()
    while Ctr < (LEN_A_STRING):
        Testchar = A_STRING[Ctr]
        if Testchar in Ltrs:
            Ltrs[Testchar] += 1
        else:
            Ltrs[Testchar] = 1
        Ctr += 1
    First = 1
    for k in Ltrs:
        if Ltrs[k] == 1:
            if First == 1:
                print("The first character without repeat is %s" % k)
                First = 0
    if First == 1:
        #raise ValueError("No character was found without repeats")
        print(f"no repeat character in {A_STRING}")
        
find_non_repeat(A_STRING)