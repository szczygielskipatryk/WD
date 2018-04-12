def srednia(lista):
    srednia=0.0
    srednia=sum(lista)/len(lista)
    return srednia
def liczenie():
    lista=[]
    while(True):
        x=input("Podaj liczbe lub q: ")
        if z =="q":
            print(lista)
            print(sum(lista))
            print(srednia(lista))
            break
        else:
            lista.append(int(z))
liczenie()
