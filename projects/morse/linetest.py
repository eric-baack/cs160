file_in = "data/projects/morse/morse.txt"
file_read = open(file_in, "r")
for line in file_read:
    cstr = line.split()
    letter = cstr[0]
    code = cstr[1]
    print(f"letter {letter}")
    print(f"{code}")