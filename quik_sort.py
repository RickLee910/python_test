def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint -1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first ,last):
    pointvalue = first+1
    leftmark = first +1
    rightmark = last
    done = False
    while not done:
        while leftmark<=rightmark and alist[leftmark] <= pointvalue:
            leftmark+=1
        while alist[rightmark] >= pointvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[first], alist[rightmark]
    return rightmark

list=[1,5,2,3,132,4,234,1,235,6,2]
quickSort(list)
print(list)