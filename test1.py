'''
def solve(N):
    pool = # A
    def queen(cur=0):
        if cur == len(pool):
            return # X
        res = # Y

        for col in range(len(pool)):
            pool[cur], flag = col
            for row in range(cur):
                if pool[row] == col or abs(col - pool[row]) == cur - row:
                    flag = False
                    break
                if flag:
                    res +=queen(cur + 1)
            return res
        return queen(0)

print(solve(8))
'''