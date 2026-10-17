n= int(input())
b=int(input())
s=""
while n>0:
    du=n%b
    if du <10:
        s=str(du) + s
    else:
        s=chr(du-10+ord('A'))+s
    n=n//b
    print(s)