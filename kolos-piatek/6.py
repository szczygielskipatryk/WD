def ustawienie():
    plik=open("liczby.txt","r+")
    s=plik.readlines()
    i=s[0].split(" ")
    l="\n"
    k=l.join(i)
    plik.write(k)


ustawienie()