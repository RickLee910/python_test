def Tostr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return Tostr(n//base, base) + convertString[n % base]

print(Tostr(155,16))