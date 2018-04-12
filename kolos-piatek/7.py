def tablica():
    lista1=[]
    lista2=[]
    lista3=[]
    listaniep=[]
    listaparz=[]
    for i in range(20):
        import random
        random.seed()
        x=random.randint(1,50)
        lista1.append(x)
        z=random.randint(1,50)
        lista2.append(z)
    lista3=lista1+lista2
    for j in range(40):
        if lista3[j]%2==0:
            listaparz.append(lista3[j])
        else:
            listaniep.append(lista3[j])

    print("Losowe liczby nieparzyste to \n"+str(listaniep))
    print("Losowe liczby parzyste to\n"+str(listaparz))

tablica()