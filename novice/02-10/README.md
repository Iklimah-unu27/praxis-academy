# Struktur Data 

Struktur data adalah struktur yang dapat menyimpan dan mengorganisasaikan kumpulan data. 
Berikut struktur data yang ada dalam bahasa pemrograman ptyhon.

### LIst

List adalah struktur data yang menyimpan koleksi data terurut yang dapat menyimpan atau 
menampung dengan tipe data seperti array, namun dalam bahasa pemrogaman python kita dapat 
mengisi dengan data apa saja sepert float dan string dalam satu tempat.

print ("Contoh List")
contoh = ['satu', 'dua', 'tiga']
print (contoh)

print ("contoh cara mengambil list")
makan = ["satu", "air", "lauk", "nasi", "sayur"]
print (makan[2]) #outputnya lauk


Adapun cara untuk menambahkan isi dari list yaitu dengan menambahkan koma saja.
cara untuk mengambil list yang kita inginkan saja yaitu dengan nencamtumkan nomer pada 
datanya saat proses pemanggilan. Data atau noemr indeks pada list dimulai dari angka 0 .
LIst bersifat muutable yang artinya isinya bisa kita ubah-ubah
 
Tedapat tiga metode yang bisa digunakan untuk menambahkan isi pada list:
 1. prepend (menambahkan item dari depan
 2. append (menambahkan item dari belakang)
 3. insert (menambahkan item dari indeks tertentu)

print("cara menambahkan data mengggunakan append") 
minum = ["kopi","susu", "es"]
minum.append("jus")
print (minum) #outputnya ['kopi', 'susu', 'es', 'jus']

 - Cara untuk menghapus hanya salah satu dari isi/list dapat menggunakan perintah del

print ("cara menghapus data atau variabel")
ngapus = ["apa", "yang", "perlu", "di", "hapus"]
del ngapus [3]
print (ngapus) #outputnya ['apa', 'yang', 'perlu', 'hapus']

 - Untuk memotong atau mengcut data dapat menggunakan indeks dengen dimulai dari angka 0

print("cara memootng/mengcut")
motong = ["ketoprak", "mie ayam", "bakso", "gado-gado", "sate", "angkringan"]
print (motong[1:5]) #outputnya ['mie ayam', 'bakso', 'gado-gado', 'sate']

 - Untuk menambah atau menjadikan list dari dua data yang berbeda menjadi satu yaitu dengan 
 menggunakan perintah + antara data pertama dengan data kedua.
 - Cara untuk mengalikan tidak beda jauh dengan cara menambah data, bedanya jika mneggalikan 
 menggunakan perintah atau tanda bintang (*) diantara kedua variabel tersebut
 - List tidak hanya memiliki satu dimensi, namun juga dapat memiliki lebih dari satu dimensi
  yang disebut List Multidiemensi. List multidimensi biasanya digunakan untuk menyimpan struktur 
  data yang kompleks seperti tabel,matriks, graph, tree dan lain sebagainya
 - Untuk perulangan berserang juga bisa menggunakan perintah for
 - Perintah pop digunakan untuk menghapus elemen dalam daftar (bawaan elemen terakhir) dan 
 mengambalikan nilai dari elemen  

### Tuple

Tuple dalam Python adalah stuktur data yang digunakan untuk menyimpan sekumpulan data. 
TupLe memiliki ciri immutable yang artinya isi tuple tidak bisa kita ubah dan hapus. 
Akan tetapi kita dapat mengisi dengan berbagai macam nilai dan objek. TUple memiliki indeks 
untuk mengakses item di dalamnya. Indeks Tuple sama dengan list yaitu selalu dimulai dari nol 0.
Untuk membuat Tuple yang hanya berisi satu (singleton) kita harus manambahkan tanda koma di 
belakangnnya.

print ("Contoh pembuatan tuple")
a = (99, 'iklima')
b = 88, 'safira'
print (a)
print (b)

##### Cara Kerja Tuple
Proses pembuatan dari tuble disebut packing, untuk mengambil (ekstrak) seluruh isinya disebut 
unpacking. Dengan melakukan upacking, isi tuple akan di-copy ke variabel. Lalu dengan variabel
kita bisa melakukan apapun, seperti mengubah isinya. Karena variabel bersifat mutable.

### Set
Set merupakan tipe data tak berurut karena set tidak menggunakan indeks. karena itulah posisi 
setiap anggota set tidak jelas dan tidak terdeteksi. 
Set memiliki kelebihan yang tidak dimiliki tipe data lain yaitu set memiliki anggota yang unik, yang artinya antar anggota satu dengan yang lain tidak ada yang sama (duplikat).Proses pembembuat set 
kita butuh tanda kurung kurawal dengan setiap anggota di dalamnya dipisahkan dengan tanda koma

sets
coba = set('Iklimah')
lagi = set('Safira')
print(coba)
print(lagi)
print(coba - lagi)

### Input dan Output

siapa = "iklima"
print ("Halo semua nama saya" ,siapa) 
output "halo semua nama saya iklima"

### Modul Python

Modul adalah objek Python dengan atribut yang diberi nama yang bisa dijadikan referensi. 
modul adalah file yang terdiri dari kode Python yang dapat mendefinisikan fungsi, kelas dan variabel. Modul juga bisa menyertakan kode yang bisa dijalankan “runable”

#### Import Statement
Kita dapat menggunakan file sumber Python apapun sebagai modul dengan mengeksekusi pernyataan 
impor di file sumber Python lainnya. Ketika interpreter menemukan sebuah pernyataan import, 
ia mengimpor modul jika modul tersebut ada di jalur pencarian. Jalur pencarian adalah daftar 
direktori yang ditafsirkan juru bahasa sebelum mengimpor modul. Misalnya, untuk mengimpor 
modul hello.py, kita perlu meletakkan perintah berikut di bagian atas script.
 

