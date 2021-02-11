#!/usr/bin/env python3
"""
Touchscreen Keyboard
"""

# create a map of the keyboard in order
# to find distances
# How?  Dictionary?  Letter - followed by XY coordinate
# eg A = 1,2.  B = 5,1.  C = 3,1.  D = 3,2.
# And D = abs(diff(x)) + abs(diff(Y))
# OK, how to do this in a dict?  Probably not:  two dimensions, need three
# Need letter, x, y.  Create a class?
# Or use two dicts:  letterx, lettery

import sys

LETTERX = dict()
LETTERY = dict()

## Had this broken into several functions, but combined for sake of testing formatpy

# Status Sunday Feb 24.
# Program seems to be working.  Not able to run test code as yet.
# output files must exist, must have a final line after output


def spell_check(filename):
    """  Rank words by their proximity to the target  """

    string1 = "qwertyuiop"
    string2 = "asdfghjkl"
    string3 = "zxcvbnm"
    letter = []
    for i in range(len(string1)):
        letter = string1[i : i + 1]
        LETTERX[letter] = i
        LETTERY[letter] = 1
    for i in range(len(string2)):
        letter = string2[i : i + 1]
        LETTERX[letter] = i
        LETTERY[letter] = 2
    for i in range(len(string3)):
        letter = string3[i : i + 1]
        LETTERX[letter] = i
        LETTERY[letter] = 3
    file_read = open(filename, "r")

    ctr = 0
    for line in file_read:
        if ctr == 0:
            # print("A", ctr)
            examples = int(line)
            examp_ct = 0
            new_example = True  # Controls how to deal with next line from file
            wtot = 0  # need to define variables before next part of loop
            max_ct = ctr + wtot
            original = ""  # holder for original word
            word_dist = dict()
        if new_example:
            if ctr > 0:
                # print("C", ctr)
                olist = line.split()
                original = olist[0]
                # print(original, "\n")
                wtot = int(olist[1])
                max_ct = (
                    ctr + wtot + 1
                )  # sets end of lines looking at alt words for this word
                min_ct = ctr
                if examp_ct < examples:
                    word_dist = dict()
                    new_example = False
                    examp_ct += 1
        if not new_example:
            # print("B", ctr)
            if min_ct < ctr < max_ct:  # checks if still in lines for this word
                dword = line.rstrip()  # remove end of line characters, etc.
                # print(dword)
                tot_dist = 0  # set total distance from word and dictionary entry
                for i in range(len(dword)):
                    ltr1 = original[i : i + 1]
                    ltr2 = dword[i : i + 1]
                    ydist = abs(LETTERY[ltr1] - LETTERY[ltr2])
                    xdist = abs(LETTERX[ltr1] - LETTERX[ltr2])
                    dist = ydist + xdist
                    tot_dist = tot_dist + dist
                word_dist[dword] = tot_dist  # store alt word, distance
            if ctr == max_ct - 1:  # will sort alt words by distance, then word, print
                swdist = sorted(word_dist, key=lambda x: (word_dist[x], x))
                for yword in swdist:
                    print(yword, word_dist[yword])
                    new_example = True
        ctr += 1


def main(argv):
    """Entry point"""
    # spell_check("data/projects/keyboard/sample.in")
    filearg = argv[1]
    arglen = len(filearg)
    filelen = arglen
    filearg2 = filearg[0:filelen] + ".txt"
    file_string = "data/projects/keyboard/" + filearg2
    # file_string =  filearg2
    spell_check(file_string)


if __name__ == "__main__":
    main(sys.argv)
