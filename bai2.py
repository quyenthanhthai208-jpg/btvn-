def snt(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            n % i ==0
            return False
        return True

import sys
du_lieu = sys.stdin.read().split()

n = int(du_lieu[0])
m = int(du_lieu[1])
cac_so = du_lieu[2:]

kq = []
for x in cac_so:
    so = int(x)
    if snt(so):
        kq.append(1)
    else:
        kq.append(0)

print(*kq)
    