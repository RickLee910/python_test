from time import time

def bubble_sort(alist):
    for passnum in range(len(alist)- 1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1]= alist[i+1] ,alist[i]

def bubble_sort_improve(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1]= alist[i+1] ,alist[i]
                exchange = True
        passnum -= 1
list = [1,5,23,1,35,34,5,1,4,34,6,72]
list1 = [1,5,23,1,35,34,5,1,4,34,6,72]
t1 = time()
bubble_sort_improve(list)
t2 = time()
bubble_sort(list1)
t3 = time()
print(list)
print(float(t2 - t1))
print(list1)
print(t3 - t2)
print(t3-2*t2+t1)

