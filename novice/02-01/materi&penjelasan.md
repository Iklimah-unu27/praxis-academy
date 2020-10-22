## Functional Programming

Pemrograman Fungsional adalah paradigma pemrograman populer yang terkait erat dengan dasar matematika ilmu komputer atau  bahasa yang menggunakan fungsi untuk mengubah data.

Bahasa fungsional adalah bahasa deklaratif ,kita memberi tahu komputer hasil apa yang kita inginkan
berbeda dengan bahasa imperatif yang memberi tahu komputer langkah apa yang harus diambil untuk memecahkan masalah

Pemrograman fungsional mempunyai karakterisitik yang penting yaitu 'The absence of side effects'. Artinya bahwa pemrograman fungsional tidak bergantung pada data yang diluar fungsi, dan tidak merubah data yang ada di luar fungsi.

Pada contoh lain, pemrograman fungsional tidak melakukan iterasi dalam struktur data seperti list, stack dan lain-lain. Untuk melakukan iterasi terhadap data, teknik yang digunakan biasanya dengan fungsi map() dan reduce().

ciri fungsional yaitu :

1. Pure Functions (Fungsi Murni) yaitu tidak mengubah status program. Dengan masukan yang sama, fungsi murni akan selalu menghasilkan keluaran yang sama.  
2. Immutability (Kekekalan) yaitu data tidak dapat diubah setelah dibuat.
3. Higher Order Functions (Fungsi Urutan Tinggi) yaitu fungsi dapat menerima fungsi lain sebagai parameter dan fungsi dapat mengembalikan fungsi baru sebagai keluaran.

Contoh pemerograman Fungsional
def increment(a):
    return a + 1

contoh pemrograman Tidak fungsional
a = 0
def increment():
    global a
    a += 1

### Lamda

Sintaks "lambda" memungkinkan Anda membuat definisi fungsi dengan cara deklaratif. Istilah lainnya "fungsi anonim" karena fungsi lambda dapat digunakan secara in-line tanpa memerlukan nama.

#contoh lamda
a = lambda x: x**5
print(a(5))
print(f'Tipe variabel {type(a)}')

Sebuah "callable" adalah segala sesuatu yang dapat dipanggil dengan tanda kurung - secara praktis berbicara tentang kelas, fungsi dan metode. Diantaranya, penggunaan yang paling umum adalah mendeklarasikan prioritas relatif melalui kunci argumen saat menyortir struktur data.
Kelemahan dari fungsi lambda sebaris adalah fungsi tersebut muncul tanpa nama di pelacakan tumpukan, yang dapat membuat proses debug menjadi lebih sulit

### Functools

Fungsi tingkat tinggi yang merupakan inti dari pemrograman fungsional tersedia pada Python melalui pustaka functools. 

val = [1, 2, 3, 4, 5, 6]
'Kalikan setiap item dengan angka dua'
list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
'Ambil faktorial dgn mengalikan nilainya dengan item berikutnya'
reduce(lambda: x, y: x * y, val, 1) # 1 * 1 * 2 * 3 * 4 * 5 * 6

### map  function

map menerapkan fungsi ke setiap item secara berurutan, mengembalikan urutan resultan, dan mengurangi menggunakan fungsi untuk mengumpulkan setiap item dalam urutan menjadi satu nilai

contoh map
merek = ['acer', 'asus', 'apple', 'hp', 'lg']
contoh_map = map(lambda x: f'aku pake laptop merek {x}', merek)
print(contoh_map)
for name in contoh_map:
    print(name)

### filter function

Mirip dengan map, filter mengambil objek fungsi dan iterable dan membuat daftar baru.
Seperti namanya, filter membentuk daftar baru yang hanya berisi elemen yang memenuhi kondisi tertentu, yaitu fungsi yang berikan mengembalikan True.

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object)) # outputnya Apple, Apricot

### reduce Function

mengurangi bekerja secara berbeda dari map dan filter. Itu tidak mengembalikan daftar baru berdasarkan fungsi dan iterable yang telah kita lewati. Sebaliknya, ini mengembalikan satu nilai.
Dalam Python 3, reduce bukan fungsi bawaan dan dapat ditemukan di modul functools.

rom functools import reduce
list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("nilai awal: " + str(reduce(lambda x, y: x + y, list, 10)))