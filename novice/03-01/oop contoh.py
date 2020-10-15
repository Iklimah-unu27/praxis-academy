class Santri():
    #all_santri = []                     
    def __init__(self, nama, pondok):    
        self.nama = nama
        self.pondok = pondok
        #Santri.all_santri.append(self)  

class Pondok():                    
    def __init__(self, mushola):
        self.mushola = mushola
        #return f'santri {self.nama}, sedang mengaji {self.pondok} di dalam {mushola} '

class Kitab(Santri, Pondok):                   
    def __init__(self, nama, pondok, mushola, kitab):
        self.kitab = kitab
        Santri.__init__(self, nama, pondok)
        Pondok.__init__(self, mushola)
        print("santri putri bernama {}, di pondok {}, sedang duduk {}, ngaji{}.".format(self.nama, self.pondok, self.mushola, self.kitab))

Data_Kitab = Kitab ('Nida', 'Darul Quran', 'mushola', 'tajwid')

### coba lagi
class Kucing:
    species = 'mammalia'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return "{} sekarang {} bulan umurnya".format(self.name, self.age )
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
class RussellTerrier(Kucing):
    def run(self, speed):
        return "{} jalannya {}".format(self.name, speed)
class Lucu(Kucing):
    def run(self, speed):
        return "{} jalannya {}".format(self.name, speed)
moew = Lucu("kity", 2)
print(moew.description())
print(moew.run("lambat"))