

class Pracownik:
    imie=[]
    nazwisko=[]
    wiek=[]
    plec=[]
    def __init__ (self, imie, nazwisko, wiek , plec):
        self.imie=imie
        self.nazwisko=nazwisko
        self.plec=plec
        self.wiek=wiek
    def __str__(self):
        print("Pracownik " +self.imie+" "+self.nazwisko+" to "+self.plec+ " w wieku " + str(self.wiek) +" lat." )
plik=open("pracownik.txt","r")
n=plik.readlines()
k=n[0]
i=n[1]
l=n[2]
prac1=k.split(",")
prac2=i.split(",")
prac3=l.split(",")
plik.close()
jan=Pracownik(prac1[0],prac1[1],prac1[2],prac1[3])
jan.__str__()
jan2=Pracownik(prac2[0],prac2[1],prac2[2],prac2[3])
jan2.__str__()
jan3=Pracownik(prac3[0],prac3[1],prac3[2],prac3[3])
jan3.__str__()


