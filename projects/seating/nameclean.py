# nameclean.py
# Takes initial name csv file and leaves only name strings

myinfile = open("names.csv")
myoutfile = open("names2.txt", "w")
ctr = 0
for line in myinfile:
    print(line)
    l2 = line.strip()
    nlist = l2.split(",")
    outstr = nlist[0] + " " +nlist[1] + ";" + ";" + "\n"
    myoutfile.write(outstr)
myinfile.close()
myoutfile.close()