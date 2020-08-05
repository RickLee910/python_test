#normal binary search
def bin_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <=last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item > alist[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint - 1

    return found

#recursion binary search
def fac_bin_search(alist, item):
    if len(alist )== 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item > alist[midpoint]:
                return fac_bin_search(alist[midpoint+1:],item)
            else:
                return fac_bin_search(alist[:midpoint],item)

testlist = [1,2,3,4,5,11,12]
print(bin_search(testlist, 7))
print(fac_bin_search(testlist, 5))