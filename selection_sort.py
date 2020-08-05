def selection_sort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionofMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionofMax]:
                positionofMax = location
        alist[positionofMax], alist[fillslot]= alist[fillslot], alist[positionofMax]

list = [1,5,23,1,35,34,5,1,4,34,6,72]
selection_sort(list)
print(list)