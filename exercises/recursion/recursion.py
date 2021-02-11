#!/usr/bin/env python3
"""Recursion exercise code template"""

# Key idea:  each upper level in recursion is suspended
# while the lower level executes.  Once lower level is 
# complete, upper level recursion resumes.  So, symmetry
# is easy around base case.


def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b) # This is key!  Must ask for the answer to be returned or it is lost.
    


def hourglass_ite(levels: int) -> None:
    # Better
    for line_ct in range(levels, 0,-1):
        star_str = "*" * (line_ct * 2 -1)
        print("{:^{width}}".format(star_str, width = (levels * 2 + 1)))
    for line_ct in range(2,levels+1,1):
         star_str = "*" * (line_ct * 2-1)
         print("{:^{width}}".format(star_str, width = (levels * 2 + 1)))
    print()



def diamond_ite(levels: int) -> None:
    for line_ct in range(levels):
        star_str = "*" * (1 + line_ct * 2)
        print("{:^{width}}".format(star_str, width = (levels*2 + 1)))

    for line_ct in range(levels-2, -1, - 1):
         star_str = "*" * ( 1 + line_ct * 2)
         print("{:^{width}}".format(star_str, width = (levels * 2 + 1)))
    print()


def hourglass_rec(levels: int) -> None:
    """ print an hourglass.  Print reduced number of stars until
    reach level 1.  At end of recursion, resume execution with increasing
    number of stars per level.  Key insight:  recursion halts until return from
    lower level of recursion.  So last if statement is not executed until after
    level 1 is achieved """
    star_str = "*" * (levels)
    star_str2 = " ".join(star_str)
    print("{:^9}".format(star_str2))
    if levels != 1:
        hourglass_rec(levels-1)
    if levels != 1:
        print("{:^9}".format(star_str2))






def diamond_rec(levels: int) -> str:
    star_str = "*" * (5 - ((levels -1)))
    star_str2 = " ".join(star_str)
    print("{:^9}".format(star_str2))
    if levels != 1:
        diamond_rec(levels -1)
    if levels != 1:
        print("{:^9}".format(star_str2))
    


def main():
    """Main function"""
    print(gcd(2020, 1860))
    print()
    print("Next, the iterative hourglass")
    print()
    hourglass_ite(5)
    print()
    print("Then the recursive hourglass")
    hourglass_rec(5)
    print()
    print("And the iterative diamond")
    print()
    diamond_ite(5)
    print()
    print("And finally the recursive diamond")
    print()
    diamond_rec(5)


if __name__ == "__main__":
    main()