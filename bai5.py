s=input()
while len(s) >1:
    n=len(s)
    d=s[:n//2]
    s=s[n//2:]
    tong= int(d) + int(s)
    print(tong, end=' ')
    s=str(tong)

