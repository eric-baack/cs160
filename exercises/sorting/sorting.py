""" Sorting.py
April 4, 2019.  E. Baack
Sort list of integers using selection sort, bubble sort, merge sort, quicksort, or heapsort
"""

import heapq

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

def quick_sort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return alist

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    print(alist)

    return rightmark

def heap_sort(alist):
    blist = []
    heapq.heapify(alist)
    print(alist)
    h_total = len(alist)
    for hct in range(h_total):
        blist.append(heapq.heappop(alist))
        print(f"sorted {blist}")
        print(f"to be sorted: {alist}")
    return blist
    


def main():
    """Main function"""
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    print(f"Carrying out insertion sort on {test_list}")
    new_list = insertion_sort(test_list)
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    print(f"Carrying out bubble sort on {test_list}")
    new_list = bubble_sort(test_list)
    print(f"List after insertion sort: {new_list}")
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
    print()
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    test_list = [44, 94, 55, 90, 58, 37, 30, 82, 29]
    print(f"Carrying out quick sort on {test_list}")
    new_list = quick_sort(test_list)
    print(f"List after quick sort: {new_list}")
    print()
    test_list = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    print(f"Carrying out heap sort on {test_list}")
    new_list = heap_sort(test_list)
    print(f"List after heap sort: {new_list}")


if __name__ == "__main__":
    main()
