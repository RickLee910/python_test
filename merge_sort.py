def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j +1
            k = k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i = i + 1
            k=k+1
        while j < len(righthalf):
            alist[k]= righthalf[j]
            j=j+1
            k=k+1

def mergeSort1(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = mergeSort1(alist[:mid])
    right = mergeSort1(alist[mid:])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    merged = []
    while left and right:
        if left[0] <=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)

    return merged

list = [3,1,5,4,6,4,2,3,23,4]
print(merge_sort(list))