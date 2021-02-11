# CS 190 exercise 1.  Feb 6, 2019.  E. Baack
# Find the first character that is not repeated in a string
# Logic:  create dictionary containing all characters in a string, and the number of occurrences.
# Move through dictionary to find first value == 1; print the associated key.

teststring = "AXT6M89T7GXMA98"
len_tstring = len(teststring)
ctr = 0
ltrs = dict()
while (ctr < (len_tstring)):
    testchar = teststring[ctr]
    if testchar in ltrs:
        ltrs[testchar] += 1
    else:
        ltrs[testchar]=1
    ctr+=1
first = 1
for k in ltrs:
    if ltrs[k]==1:
        if first == 1:
            print("The first character without repeat is %s" % k)
            first = 0