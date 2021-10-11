# July 2021, Eric Baack
# Given list of students, prior seats, and prior teammates, create a new set of seats / teams

import random

def readnames(namefile):
# names2.txt    Contains name (last, first - must be unique);  seats; teammates - separated by ';'
#               Seats (list, comma separated.  May be empty)
#               Teammates (list, comma separated, of strings of names.  May be empty)
    tdict = {}
    sdict ={}
    for line in namefile:
        #print(line)
        l1 = line.strip()
        l2 = l1.replace('"', '')
        l3  = l2.split(";")
        name = l3[0]
        seats = l3[1]
        teammates = l3[2]
        tdict[name] = [teammates]
        sdict[name] = [seats]
    namefile.close()
    return tdict, sdict

def readseats(seatfile, student_ct):
#v206seats.csv    Contains seat, group, day, priority, separated by commmas
# Priority determines which seats are not used depending on class size
# When make this a function, pass dictionary, # of students.  Use this to drop priority.

# Will adjust last group depending on student count
# If student_ct % 3 == 0 or 2  no adjustment
# if student_ct % 3 == 1; 

    ndict = {}
    group_adjust = (student_ct % 3 == 1)
    for line in seatfile:
        l2 = line.strip()
        l3  = l2.split(",")
        seat = l3[0]
        group= int(l3[1])
        day = l3[2]
        priority = int(l3[3])
        if priority <= student_ct:
            ndict[seat] = group
            if group_adjust and priority == (student_ct - 1):
                ndict[seat] = group + 1
    seatfile.close()
    return ndict

def randseats(nseatsdict, teamdict):
# Next:  randomly assign seats / groups
    gdict = {}
    seatlist = list(nseatsdict.keys())
    studentlist = list(teamdict.keys())
    seatdict = {}
    for s in studentlist:
        if len(seatlist) > 1:
            m = random.randrange(0,len(seatlist))
        else:
            m = 0
        nseat = seatlist.pop(m)
        seatdict[s] = nseat
        group = nseatsdict[nseat]
        if group not in gdict:
            gdict[group] = [s]
        else:
            gdict[group].append(s)
    return seatdict, gdict

def checkseats(new_seats, new_groups, nseatsdict, teamdict, seatsdict):
    pseats = {}
    for s in new_seats:
        # check for same seat previously
        nseat = new_seats[s]
        nrow = nseat[0]
        #print("sl: ", seatsdict[s])
        if len(seatsdict[s])> 0:
            sl = len(seatsdict[s])
            lseat = seatsdict[s]  # Won't work if multiple seats.  
            lrow = lseat[0]
            #print("n, l: ", nrow, lrow)
            if nrow == lrow:
                pseats[s] = new_seats[s]
        # check for same teammates previously
        ngroup = nseatsdict[nseat]
        for t in new_groups[ngroup]:
            if t != s:
                if t in teamdict[s]:
                    pseats[s] = new_seats[s]
    return pseats

def save_seats(teamdict, seatsdict, nseatsdict, new_seats, new_groups):
    for s in new_seats:
        nseat = new_seats[s]
        ngroup = nseatsdict[nseat]
        seatsdict[s].append(nseat)
        for t in new_groups[ngroup]:
            if t != s:
                teamdict[s].append(t)
    outfile = open("names2.txt", "w")
    for s in new_seats:
        seat_str = ""
        for seat in seatsdict[s]:
            if len(seat_str) > 0:
                seat_str = seat_str + ", " + seat
            else:
                seat_str = seat_str + seat
        team_str = ""
        for mate in teamdict[s]:
            if len(team_str) > 0:
                team_str = team_str + ", " + mate
            else:
                team_str = team_str + mate
        out_str = s + ";" + seat_str + ";" + team_str + "\n"
        outfile.write(out_str)
    outfile.close()
    outfile = open("newseats.txt", "w")
    for s in new_seats:
        out_str = s + "\t" + new_seats[s] + "\n"
        outfile.write(out_str)
    outfile.close()
    outfile = open("newgroups.txt", "w")
    glist = list(new_groups.keys())
    glist.sort()
    for g in glist:
        t_str = ""
        for t in new_groups[g]:
            if len(t_str) > 0:
                t_str = t_str + "," + t
            else:
                t_str = t_str + t
        out_str = str(g) + "\t" + t_str + "\n"
        outfile.write(out_str)
    outfile.close()

    return

        
def changeseats(prob_seats, new_seats, nseatsdict):
    mseats = list(prob_seats.values())
    for s in prob_seats:
        if len(mseats) > 1:
            m = random.randrange(0,len(mseats))
        else:
            m = 0
        nseat = mseats.pop(m)
        new_seats[s] = nseat
    gdict = {}
    for s in new_seats:
        nseat = new_seats[s]
        group = nseatsdict[nseat]
        if group not in gdict:
            gdict[group] = [s]
        else:
            gdict[group].append(s)
    return new_seats, gdict


    





# After assignment, check if repeat seat / teammates
# If just one repeat, redo randomization
# If two, try swap, check.  If fail, redo randomization
# If three or more, try random swaps 10x.  If fail, redo randomization

def main():
    namefile = open("names2.txt", "r")
    seatfile= open("olin102seats.csv", "r")

    teamdict, seatsdict = readnames(namefile)
    
    student_ct = len(teamdict)
    nseatsdict = readseats(seatfile, student_ct)
    new_seats, new_groups = randseats(nseatsdict, teamdict)
    
    prob_seats = checkseats(new_seats, new_groups, nseatsdict, teamdict, seatsdict)
    
    first = True
    while len(prob_seats) > 0:
        print("oh boy, # problems: ", len(prob_seats))
        first = True
        # first attempt - try again if conflicts
        # this doesn't work if testing for row flips - need better
        if len(prob_seats) > 3:
            if first == True:
                ctr = 0
                first = False
            while ctr < 5:
                new_seats, new_groups = changeseats(prob_seats, new_seats, nseatsdict)
                ctr += 1
        else:
            new_seats, new_groups = randseats(nseatsdict, teamdict)
        prob_seats = checkseats(new_seats, new_groups, nseatsdict,teamdict, seatsdict)
    save_seats(teamdict, seatsdict, nseatsdict, new_seats, new_groups)
    print("New seats and groups assigned")

main()