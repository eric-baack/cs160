""" Sorting.py
April 4, 2019.  E. Baack
Sort list of integers using selection sort, bubble sort, merge sort, quicksort, or heapsort
"""

def bubble_sort(alist):
    """ implementation of bubble sort"""
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        print(alist)
    return alist

def selection_sort(alist):
    """ implementation of selection_sort"""
    for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       print(alist)
    return alist

def insertion_sort(alist):
    """ implementation of insertion_sort"""
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
        print(alist)
    return alist

def merge_sort(alist):
    """ implementation of merge sort """
    print(f"Splitting {alist}")
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        print(f"Merging {alist}")
    return alist

def quick_sort(list):
    pass

def main():
    """Main function"""
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    print(f"Carrying out bubble sort on {test_list}")
    new_list = bubble_sort(test_list)
    print(f"List after bubble sort: {new_list}")
    print()
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    print(f"Carrying out selection sort on {test_list}")
    new_list = selection_sort(test_list)
    print(f"List after selection sort: {new_list}")
    print()
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    print(f"Carrying out merge sort on {test_list}")
    new_list = merge_sort(test_list)
    print(f"List after merge sort: {new_list}")


if __name__ == "__main__":
    main()
