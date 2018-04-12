plik=open("lorem.txt","r+")
n=plik.readlines()
i=n[0]
i.replace(",","")
i.replace(".","")
tablica = i.split(" ")
print(len(tablica))
