def insert_sort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position- 1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position]= currentvalue

list = [1,5,23,1,35,34,5,1,4,34,6,72]
insert_sort(list)
print(list)