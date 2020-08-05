def fac(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 'error'
    else:
        return n * fac(n - 1)

print(fac(5))
print(fac(0))
print(fac(15))
print(fac(-1))