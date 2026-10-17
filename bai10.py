def ktdb(n):
    for kt in n:
        if not kt.isalnum():
            raise ValueError('co kt dac biet')
    return True
n=input()
print(ktdb(n))
        
