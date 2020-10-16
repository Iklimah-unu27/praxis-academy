### Pengertian OOP 

OOP (Pemrograman berorientasi objek) adalah paradigma pemrograman yang didasarkan pada konsep objek 
yang dapat memuat data dan kode data dalam bentuk field dan kode dalam bentuk prosedur/metode. 
Lebih mudahnya OOP adalah teknik pemrograman di mana semua hal dalam program dimodelkan seperti objek dalam dunia nyata. Objek di dunia nyata memiliki ciri atau attribut juga aksi atau kelakuan.Fitur objek 
adalah prosedur objek itu sendiri dapat mengakses dan sering kali memodifikasi bidang datanya sendiri. 

OOP menyediakan lapisan abstraksi yang dapat digunakan untuk memisahkan internal dari kode eksternal. Kode eksternal dapat menggunakan objek dengan memanggil metode instance tertentu dengan sekumpulan parameter input tertentu, membaca variabel instance, atau menulis ke variabel instance.
Objek dibuat dengan memanggil metode tipe khusus di kelas yang dikenal sebagai konstruktor .Suatu program dapat membuat banyak instance dari kelas yang sama saat dijalankan, yang beroperasi secara independen. Ini adalah cara mudah untuk menggunakan prosedur yang sama pada kumpulan data yang berbeda. 

##### Polimorfisme
adalah saat kode pemanggil dapat bersifat agnostik terhadap kelas mana dalam hierarki yang didukung tempat ia beroperasi - kelas induk atau salah satu turunannya.

##### Rekursi terbuka
Dalam bahasa yang mendukung rekursi terbuka, metode objek dapat memanggil metode lain pada objek yang sama (termasuk metode itu sendiri), biasanya menggunakan variabel khusus atau kata kunci yang disebut this atau self. 

OOP dikenal sebagai bahasa 
- Bahasa disebut bahasa OO "murni", karena semua yang ada di dalamnya diperlakukan secara konsisten sebagai objek, dari primitif seperti karakter dan tanda baca, hingga seluruh kelas, prototipe, blok, modul, dll. Mereka dirancang khusus untuk memfasilitasi, bahkan menegakkan, metode OO. Contoh: Ruby , Scala, Smalltalk, Eiffel, Emerald, JADE, Self, Raku .
- Bahasa yang dirancang terutama untuk pemrograman OO, tetapi dengan beberapa elemen prosedural. Contoh: Java , Python , C ++ , C # , Delphi / Object Pascal , VB.NET .
- Bahasa yang secara historis merupakan bahasa prosedural , tetapi telah diperluas dengan beberapa fitur OO. Contoh: PHP , Perl , Visual Basic (berasal dari BASIC), MATLAB , COBOL 2002 , Fortran 2003 , ABAP , Ada 95 , Pascal .
- Bahasa dengan sebagian besar fitur objek (kelas, metode, warisan), tetapi dalam bentuk asli yang jelas. Contoh: Oberon (Oberon-1 atau Oberon-2).
- Bahasa dengan dukungan tipe data abstrak yang dapat digunakan untuk menyerupai pemrograman OO, tetapi tanpa semua fitur orientasi objek. Ini termasuk object berdasarkan dan berbasis prototipe bahasa. Contoh: JavaScript , Lua , Modula-2 , CLU .
- Bahasa bunglon yang mendukung banyak paradigma, termasuk OO. Tcl menonjol di antara ini untuk TclOO, sistem objek hybrid yang mendukung pemrograman berbasis prototipe dan OO berbasis kelas.
- Variabel yang dapat menyimpan informasi yang diformat dalam sejumlah kecil tipe data bawaan seperti bilangan bulat dan karakter alfanumerik termasuk struktur data (string , daftar , dan tabel hash) yang merupakan bawaan atau hasil dari menggabungkan variabel menggunakan pointer memori .
- Prosedur - juga dikenal sebagai fungsi, metode, rutinitas, atau subrutin - yang mengambil masukan, menghasilkan keluaran, dan memanipulasi data.

##### OOP dan aliran kontrol
OOP dikembangkan untuk meningkatkan penggunaan kembali dan pemeliharaan kode sumber. Representasi transparan dari aliran kontrol tidak memiliki prioritas dan dimaksudkan untuk ditangani oleh kompilator. Dengan meningkatnya relevansi perangkat keras paralel dan pengkodean multithread , mengembangkan aliran kontrol transparan menjadi lebih penting, sesuatu yang sulit dicapai dengan OOP.

Objek adalah entitas run-time dalam sistem berorientasi objek. Mereka mungkin mewakili seseorang, tempat, rekening bank, tabel data, atau item apa pun yang harus ditangani oleh program.

Ada beberapa upaya untuk memformalkan konsep yang digunakan dalam pemrograman berorientasi objek. Konsep dan konstruksi berikut telah digunakan sebagai interpretasi konsep OOP:
- tipe data aljabar gabungan 
- tipe data abstrak (yang memiliki tipe eksistensial ) memungkinkan definisi modul tetapi ini tidak mendukung pengiriman dinamis
- tipe rekursif
- keadaan dikemas
- warisan
    
Record adalah dasar untuk memahami objek jika literal fungsi dapat disimpan dalam bidang (seperti dalam bahasa pemrograman fungsional), tetapi kalkulus yang sebenarnya perlu jauh lebih kompleks untuk memasukkan fitur-fitur penting OOP.

#### Class dengan Python
Berfokus pertama pada data, masing-masing benda atau benda merupakan turunan dari beberapa class. Struktur data primitif yang tersedia dengan Python, seperti angka, string, dan daftar dirancang untuk mewakili hal-hal sederhana

class adalah mekanisme yang digunakan untuk membuat struktur data pengguna baru yang ditentukan. Ini berisi data serta metode yang digunakan untuk memproses data tersebut.

class merupakan sebuah objek yang di dalam nya biasanya terdapat beberapa metode yang memang merupakan isi dari sebuah class ini. Class dan metode ini biasa di sebut sebagai OOP atau object oriented programing. Dan OOP ini memang fungsinya untuk memudahkan proses atau kegiatan programing. 

##### Cara Menentukan class dengan Python
Mendefinisikan sebuah class sederhana dengan Python:

class Fish: 
        pass

Bagian (object) dalam tanda kurung menentukan class induk yang diwarisi. Dengan Python 3, ini tidak lagi diperlukan karena ini adalah default implisit. 

##### Atribut Instance
Semua class membuat objek, dan semua objek mengandung karakteristik yang disebut atribut (disebut sebagai properti pada paragraf pembuka). Gunakan __init__()metode untuk menginisialisasi (misalnya, tentukan) atribut awal objek dengan memberi mereka nilai default (atau side state). Metode ini harus memiliki setidaknya satu argumen dan juga selfvariabel, yang mengacu pada objek itu sendiri. 

class Fish:
    def __init__(self, name, age):
        self.name = name
        self.age = age

     class hanya untuk mendefinisikan Kucing
     self variabel juga merupakan instance dari class

##### Atribut class
Sementara atribut instance spesifik untuk setiap objek, atribut class sama untuk semua contoh

class Kucing:
# class Attribute
    species = 'mamalia'
# Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
Jadi sementara setiap Kucing memiliki nama dan umur yang unik. 

##### Instantiating Objek
Instansiasi adalah untuk menciptakan instance class baru yang unik

>>> class Kucing:
...     pass
...
>>> Kucing()
<__main__.Kucing object at 0x1004ccc50>
>>> Kucing()
<__main__.Kucing object at 0x1004ccc90>
>>> a = Kucing()
>>> b = Kucing()
>>> a == b
False

##### Instance Methods
Metode Instance didefinisikan di dalam class dan digunakan untuk mendapatkan isi sebuah instance. Mereka juga bisa digunakan untuk melakukan operasi dengan atribut objek kita. Seperti __init__metodenya, argumen pertama selalu self:

##### Warisan Python
Warisan adalah proses dimana satu class mengambil atribut dan metode yang lain. class yang baru terbentuk disebut class anak , dan class class anak diturunkan dari class orang tua disebut .
Penting untuk dicatat bahwa class anak menimpa atau memperluas fungsionalitas (misalnya, atribut dan perilaku) class orang tua. Dengan kata lain, class anak mewarisi semua atribut dan perilaku orang tua namun juga dapat menentukan perilaku yang berbeda untuk diikuti. Jenis class yang paling dasar adalah class objectyang umumnya mewarisi class lainnya sebagai orang tua mereka.


### CRD Card (responsibility)
CRC Card adalah satu cara untuk pengaambaran diagram UML sederhana dimana crd card dapat 
digunakan untuk mengetahui reponsibility dan kolaborasi yang ada dr sebuah kelas.
Kelas mewakili sekumpulan objek serupa. 
Tanggung jawab adalah sesuatu yang diketahui atau dilakukan kelas, dan 
kolaborator adalah kelas lain yang berinteraksi dengan kelas untuk memenuhi tanggung jawabnya

Software system terdiri dari modul-modul, dimana masing-masing modul memiliki peran/fungsi yang khusus. Modul-modul tersebut saling berinteraksi dalam sistem. Pada program yang berorientasi obyek modul-modul tersebut berupa class.

Class ≈ Moduld

Menggunakan kartu kecil meminimalkan kerumitan desain. Ini memfokuskan desainer pada esensi kelas dan mencegah mereka masuk ke detail dan implementasinya pada saat detail seperti itu mungkin kontra-produktif. Itu juga mengecilkan hati memberi kelas terlalu banyak tanggung jawab. Karena kartu ini portabel, kartu dapat dengan mudah diletakkan di atas meja dan diatur ulang saat mendiskusikan desain.

Kartu tersebut dibagi menjadi tiga area:

    1. Di atas kartu, nama kelas
    2. Di sebelah kiri, tanggung jawab kelas
    3. Di sebelah kanan, kolaborator (kelas lain) yang berinteraksi dengan kelas ini untuk memenuhi tanggung jawabnya

### Standard Library

Standard Library adalah kumpulan modul yang mempermudah dalam melakukan tugas tertentu untuk menghasilkan solusi dari suatu permasalahan tertentu. 
Standar Library di Python merupakan kumpulan modul yang sudah terinstall di Python dan dapat kita gunakan langsung dalam sistem dan sudah diuji. 
Standard Library meliputi modul untuk berinteraksi dengan sistem operasi, interpreter, internet, database, struktur data dsb. 
Untuk menggunakan module tersebut dapat menggunakan syntax sebagai berikut import nama_module.

Beberapa aplikasi standard Library di Python:

- Program untuk melakukan backup rutin pada Linux, Solaris dan Mac, library standard yang dapat digunakan adalah os, stat, bz2, gzip, time, datetime, tar dan optparse
- Program Apache log file analysis tool menggunakan modul optparse, urlparse, cgi, datetime, operator, re, sys, and mmap.
- Program sederhana web API clients cukup menggunakan library urllib/urllib2, ElementTree, dan xml package
- Program MySQL backup script menggunakan sys, os, time, shutil, glob, tarfile, dan optparse modules.
