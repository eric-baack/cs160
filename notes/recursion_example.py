# recursion example from class on March 20, 2019
# Hadiqa Afzal
# goal:  obtain sum by shrinking problem

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

def factorial(x):
    ans = 1
    for i in range(x):
        ans = ans * (i + 1)
    return ans

def factorial_rec(x):
    if x == 0:
        return 1
    else:
        return x * factorial_rec(x-1)

print(factorial_rec(900))
    
    

print(listsum([1,4,5,7,8,9]))
