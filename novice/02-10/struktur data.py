#contoh list
contoh = ['satu', 'dua', 'tiga']
print (contoh)

#contoh list campuran
contohlg = ["air", 2, "ADA"]
print (contohlg)

#cara mengambil list
makan = ["satu", "air", "lauk", "nasi", "sayur"]
print (makan[2]) #outputnya lauk

#cara mengganti data
ganti = ["satu", "air", "lauk", "nasi", "sayur"]
ganti[1] = "cemilan"
print (ganti) #outputnya ['satu, 'cemilan', 'lauk', 'nasi', 'sayur']

#contoh append
minum = ["kopi","susu", "es"]
minum.append("jus")
print (minum) #outputnya ['kopi', 'susu', 'es', 'jus']
#untuk cara prepend sama dengan append
#untuk insert kita tambahkan angka untuk memasukkan data dimana yang akan kita pilih

#cara menghapus data atau variabel
ngapus = ["apa", "yang", "perlu", "di", "hapus"]
del ngapus [3]
print (ngapus) #outputnya ['apa', 'yang', 'perlu', 'hapus']

#cara memotong data atau variabel
motong = ["ketoprak", "mie ayam", "bakso", "gado-gado", "sate", "angkringan"]
print (motong[1:5]) #outputnya ['mie ayam', 'bakso', 'gado-gado', 'sate']

#cara menambah 
makanan = ["nasi", "ikan", "gorengan", "seblak"]
minuman = ["es teh", "kopi", "jus", "air putih"]
pesenan = makanan + minuman 
print (pesenan) #outputnya ['nasi', 'ikan', 'gorengan', 'seblak', 'es teh', 'kopi', 'jus', 'air putih']

#cara perkalian
daily = ["makan", "tidur"]
ulangi = 3
daily = daily * ulangi
print (daily) #outputnya ['makan', 'tidur', 'makan', 'tidur', 'makan', 'tidur']

#contoh cara list multidimensi
gabung = [
    ["makan", "tidur"], 
    ["seblak", "capcin"],
    ["nonton", "drakor"] 
] #misalkan ingin nonton maka 
print (gabung[2][0]) 

#contoh cara menampilkan list
ulang_lezat = [
    ["Nasi Padang", "Bakso", "Soto"],
    ["Jasuke", "Seblak", "Cilor"],
    ["Es teh", "Kopi", "Jus"]
]
for menu in ulang_lezat:
    for milih in menu:
        print (milih)

#contoh cara menghapus
ngehapus = ["pagi", "siang", "sore", "malem"]
del ngehapus [2]
print (ngehapus) #output yang dihasilkan ['pagi', 'siang', 'malem']

#contoh mneghapus menggunakan remove 
angka = ["satu", "dua", "tiga", "empat", "lima"]
angka.remove("tiga")
print (angka) #output yang dihasilkan ['satu', 'dua', 'empat', 'lima']

#contoh menggunakan pop
ilang = ["abs", "def", "ghi", "jkl"]

print ("A List : ", ilang.pop())
print ("B List : ", ilang.pop(2))
#output yang dihasilkan yaitu A List: jkl || B List :ghi

#contoh clear
A = set("jogja")
print (A) #outputnya {'j', 'a', 'o', 'g'}
A.clear
print (A)
