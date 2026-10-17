def scphh(n):
    if n<0:
        return False
    return (n**0.5) % 1 == 0
n=(int(input()))
print(scphh(n))