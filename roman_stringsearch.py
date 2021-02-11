#/usr/bin/python3  - specify interpreter
# add line for purpose for code
# put imports here

s = 'abcxxab'  # start with smaller test

def find_non_repeat_count(astr):
    for i in range(len(astr)):
        if astr[i] not in astr[i+1:]:
            return(astr[i])

def main():   ## only called if explicitly run code.  not if imported
    result = find_non_repeat_count(s)
    print(result)

if _name_ == '_main_':
    main()
# this code fails - the last a it gets to it returns

# fstring - new way to format strings in py 3.6+
# allows inclusion of values inside a string without using %, as previous


# new format for dictionary
for idex, char in enumerate(a_string):
    position_count_list=str_dict.get(char, [0,0])  # build dictionary with default values
    str_dict[char] = [idx, position_count_lst[1] + 1]
for char in a_string:
    if str_dict[char][1] == 1:
        return char
raise ValueError("No repeating characters")