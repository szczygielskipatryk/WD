def sprawdz(r,n):
    if r.count(n)==0:
        return 0
    else:
        return 1

r: str=input("Podaj ciąg tekstowy ")

n: str=input("Podaj jaki znak chcesz zliczyc ")

k=sprawdz(r,n)
wyniki=[]
if k==0:
    print("Twój ciąg nie zawiera tej litery")
else:
    i=0
    while i < len(r):
        if r[i]==n:
            wyniki.append ((i+1))
        i=i+1
    print(wyniki)