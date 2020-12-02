def encrypt(m):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) + 13) % 26
        n = n + s[j]
    return n

def decrypt(m, k):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) + 26 - k) % 26
        n = n + s[j]
    return n
a = 'yvfuhnv'
changed = decrypt(a, 13)
print(changed)