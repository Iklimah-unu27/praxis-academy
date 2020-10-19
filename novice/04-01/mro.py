class Sayuran: 
    def jenis(self): 
        print(" kangkung, bayam, cesim, kacang panjang") 

class Buah(Sayuran): 
    def jenis(self): 
        print(" jeruk, mangga, melon, semangka, anggur") 

class Sembako(Sayuran): 
    def jenis(self): 
        print(" beras, gula, minyak, telor, daging") 
      
h = Buah() 
h.jenis()   
