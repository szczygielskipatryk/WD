start=[0,1]
def fibonacci(lista,n):
    nowe=0
    for i in range(n):
        nowe=int(lista[-1])+int(lista[-2])
        lista.append(nowe)
        print (nowe)
n=input("Podaj ile wartości ciągu fibonacciego chcesz uzyskac: ")
fibonacci(start,int(n))
