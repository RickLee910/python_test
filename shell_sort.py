def shell_sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is ", alist)
        sublistcount = sublistcount // 2 


def gapInsertSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

list = [1,5,23,1,35,34,5,1,4,34,6,72]
shell_sort(list)
