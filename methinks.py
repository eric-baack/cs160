# challenge 1.12 M&R:  generate 'methinks it is like a weasel'
import random
import string
oldwlist = ['x']*28
keeplets = []
keepchars = []
def randlet():
    m = " " + string.ascii_lowercase
    n = str(random.choice(m))
    return n

def check_str(x, y):
    cs = "methinks it is like a weasel"
    success = 0
    if x == cs:
        print("success after %d attempts" % y)
        success = 1
    return success

def keep_str(x,y):
    cs = "methinks it is like a weasel"
    for i in range(0, 28):
        if cs[i] == x[i]:
            if i not in keeplets:
                keeplets.append(i)
                oldwlist[i] = x[i]
    return


def rand_word():
    randstr = []
    for ictr in range(0,28):
        if ictr not in keeplets:
            randstr.append(randlet())
        else:
            randstr.append(oldwlist[ictr])
    rs2 = ''.join(x for x in randstr)
    return rs2

success = 0
ctr = 0
while success < 1:
    new_string = rand_word()
    success = check_str(new_string, ctr)
    keep_str(new_string, ctr)
    ctr +=1
    if ctr % 100 == 0:
        print(ctr)



