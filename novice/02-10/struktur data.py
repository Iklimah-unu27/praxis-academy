print("Struktur data dalam bahasa python: 1.List 2.TUpel 3.Set")

print ("Contoh List")
contoh = ['satu', 'dua', 'tiga']
print (contoh)

print ("contoh list campuran")
contohlg = ["air", 2, "ADA"]
print (contohlg)

print ("contoh cara mengambil list")
makan = ["satu", "air", "lauk", "nasi", "sayur"]
print (makan[2]) #outputnya lauk

print ("contoh cara mengganti data")
ganti = ["satu", "air", "lauk", "nasi", "sayur"]
ganti[1] = "cemilan"
print (ganti) #outputnya ['satu, 'cemilan', 'lauk', 'nasi', 'sayur']

print ("contoh cara list multidimensi")
gabung = [
    ["makan", "tidur"], 
    ["seblak", "capcin"],
    ["nonton", "drakor"] 
] #misalkan ingin nonton maka 
print (gabung[2][0]) 

print ("contoh cara menampilkan list")
ulang_lezat = [
    ["Nasi Padang", "Bakso", "Soto"],
    ["Jasuke", "Seblak", "Cilor"],
    ["Es teh", "Kopi", "Jus"]
]
for menu in ulang_lezat:
    for milih in menu:
        print (milih)

print("cara memootng/mengcut")
motong = ["ketoprak", "mie ayam", "bakso", "gado-gado", "sate", "angkringan"]
print (motong[1:5]) #outputnya ['mie ayam', 'bakso', 'gado-gado', 'sate']

print ("Oprasi pada list 1. penggabungan,2. perkalian,3. pembagian,4. pengurangan,5. sisa_bagi,6. pemangkatan")

print ("contoh cara menambahkan/penggabungan")
makanan = ["nasi", "ikan", "gorengan", "seblak"]
minuman = ["es teh", "kopi", "jus", "air putih"]
pesenan = makanan + minuman 
print (pesenan) #outputnya ['nasi', 'ikan', 'gorengan', 'seblak', 'es teh', 'kopi', 'jus', 'air putih']

print("cara menambahkan data mengggunakan append") 
minum = ["kopi","susu", "es"]
minum.append("jus")
print (minum) #outputnya ['kopi', 'susu', 'es', 'jus']

print("contoh cara perkalian")
daily = ["makan", "tidur"]
ulangi = 3
daily = daily * ulangi
print (daily) #outputnya ['makan', 'tidur', 'makan', 'tidur', 'makan', 'tidur']

print ("Perintah POP digunakan untuk menghapus elemen dalam daftar (bawaan elemen terakhir) dan mengambalikan nilai dr elemen")
print ("contoh menggunakan pop")
ilang = ["abs", "def", "ghi", "jkl"]
print ("A List : ", ilang.pop())
print ("B List : ", ilang.pop(2))
#output yang dihasilkan yaitu A List: jkl || B List :ghi
#contoh clear
A = set("jogja")
print (A) #outputnya {'j', 'a', 'o', 'g'}
A.clear
print (A)

print ("cara menghapus data atau variabel")
ngapus = ["apa", "yang", "perlu", "di", "hapus"]
del ngapus [3]
print (ngapus) #outputnya ['apa', 'yang', 'perlu', 'hapus']
#contoh cara menghapus
ngehapus = ["pagi", "siang", "sore", "malem"]
del ngehapus [2]
print (ngehapus) #output yang dihasilkan ['pagi', 'siang', 'malem']
print ("Contoh mneghapus menggunakan remove") 
angka = ["satu", "dua", "tiga", "empat", "lima"]
angka.remove("tiga")
print (angka) #output yang dihasilkan ['satu', 'dua', 'empat', 'lima']

print ("TUPLE") #stuktur data yang digunakan untuk menyimpan sekumpulan data
print ("Contoh pembuatan tuple")
a = (99, 'iklima')
b = 88, 'safira'
print (a)
print (b)

print ("contoh tupel satu data")
a = 'motor',      
b = 'mobil'       
print (a)
print (b)

print ("contoh tupel cut")
transport = ('mobil', 'motor', 'becak', 'angkot', 'TJ', 'kereta')
print(transport[1:4])

print ("Contoh tupel jumlah data")
transport = ('mobil', 'motor', 'becak', 'angkot', 'TJ', 'kereta')
print("Kendaraan darat: %d" % len(transport))

print ('contoh tuple nested')#tuple bisa diisi dengan tuple
tuple1 = 'roti', 'gandum', 'jagung'
tuple2 = 'mie', 'beras'
tuple3 = (tuple1, tuple2)
print (tuple3)

print ("SET")
print ("contoh penggunaan set")
cobaset = [9,8,7,8,9, "huruf", 5]
print (cobaset)

print("Dictionaries")#tipe kumpulan data yang mempunyai pasangan key-value.
dict = {
    "bantal":"kasur",
    "langit":"bumi",
    "aku":"kamu"
}
dict
keluarga = {'bapak': 'ibu', 'anak': 3}
print (keluarga['anak'])

print ("Perulangan")
print ("contoh perulangan list")
list = [x*5 for x in range(20)]
for u in list:
    print(u)

print ("contoh perulangan dictionary")
kebalikan = {
    "jauh":"dekat",
    "kasar": "lembut",
    "kuat":"lemah",
    "terang":"gelap",
    "mahal":"murah"
}
for sifat, dasar in kebalikan.items():     
    print(sifat,kebalikan)

for dasar in kebalikan.values():
    print(dasar)

for sifat in kebalikan.keys():
    print(sifat)

print ("contoh input dan  output")
siapa = "iklima"
print ("Halo semua nama saya" ,siapa)