def orderSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [1,2,5,7,9,11,31,34]
print(orderSequentialSearch(testlist, 31))
print(orderSequentialSearch(testlist, 32))