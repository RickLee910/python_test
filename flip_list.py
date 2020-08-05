'''

#循环翻转列表
def flip_list(L):
    for i in range(0,len(L) // 2):
        temp = L[i]
        L[i] = L[len(L) - i-1]
        L[len(L) - i-1] = temp

'''
def flip_list1(L):


    return L[0] + flip_list1(L[1:])





L = [1,2,3,4,5]


print(flip_list1(L))