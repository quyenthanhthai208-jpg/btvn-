def ip(s):
    tach=s.split('.')
    if tach !=4:
        return False
    for p in tach:
        if not p.isdigit():
            return False
        if int(p)>255:
            return False
        if len(p)>1 and p[0] =='0' :
            return False
    return True
T=int(input())
for _ in range(T):
    s=input()
    if ip(s):
        print('YES')
    else:
        print('NO')

    