## Materi Hari Pertama

#### Keterkaitan antara bahasa pemrograman, kompiler dan interpreter

Bahasa pemrograman merupakan bahasa yang digunakan untuk menerjemahkan bahasa manusia menjadi bahasa komputer dengan tujuan tertentu. Bahasa pemograman terdiri dari serangkaian aturan sintaks dan semantik yang digunakan untuk mendefinisikan program komputer. Sistemnya terdiri dari beberapa tingkatan untuk memberi perintah pada setiap peranti, utilitas, dan aplikasi yang dipakai dalam pengoperasian komputer.

Setiap jenis bahasa memiliki struktur penyusunnya, berupa prosedur sistematis yang dinyatakan dalam kode untuk membuat perintah. Ini disebut dengan algoritma, dan setiap jenis bahasa pemograman menerapkan kategori struktur berikut ini.
1. Runtutan
Struktur runtutan dimulai dari langkah awal, yaitu instruksi pertama, kedua, ketiga, dan seterusnya secara berurutan. Setiap instruksi hanya bisa dimulai setelah instruksi sebelumnya selesai dijalankan. Struktur ini selalu dipakai dalam jenis bahasa pemograman apa saja.
2. Perulangan
Struktur perulangan membuat program dapat menjalankan perintah secara berkelanjutan hingga berhenti pada kondisi tertentu. Penghentian perulangan pun dapat diatur sedemikian rupa dengan kode-kode perintah khusus.
3. Percabangan
Di sini, bahasa pemograman mulai beranjak ke tingkat lanjut. Struktur bahasa pemograman dapat berupa percabangan yang berarti menginstruksikan pada komputer agar dapat membuat keputusan sendiri berdasarkan pilihan syarat-syarat tertentu.

Pengoperasian program melibatkan beberapa peranti keras komputer. Program terlebih dulu disimpan dalam memori (RAM) sebelum sistem operasi dapat menjalankannya. Sedang prosesor  berperan untuk mengeksekusi perintah demi perintah pada saat program tersebut dioperasikan. Fungsi dasar dari bahasa pemograman adalah agar komputer dapat mengolah data sesuai dengan alur yang dibuat secara sistematis oleh penyusunnya.Produksi bahasa pemograman dilakukan melalui proses yang cukup kompleks. Dimulai dengan penyusunan, pengujian, analisis, penyuntingan, hingga optimalisasi. Kode sumber disusun, kemudian diubah menjadi kode mesin, lalu diterjemahkan oleh prosesor sebagai perintah.

Selain itu, bahasa pemograman juga diklasifikasikan berdasarkan kedekatannya dengan perangkat komputer. Terdapat empat jenis bahasa pemograman dalam kategori ini, di antaranya:
    1. Bahasa Mesin. Berupa bahasa biner dengan kode angka 0 dan 1.
    2. Bahasa Tingkat Rendah. Istilah lain dari bahasa rakitan dengan kode huruf singkat.
    3. Bahasa Tingkat Menengah. Menggabungkan kode kata-kata dan simbol.
    4. Bahasa Tingkat Tinggi. Menggunakan kode dari istilah yang biasa dipakai manusia.

## INSTALASI PIP 
PIP merupakan Packed Manageent System yang digukana  unutk mengnduhu dan mengelola packed python. 
Cara isntall PIP Python sebagai berikut

### Cara Install PIP sebagai berikut
1. Unduh PIP (PIP Installs Package) pada official websitenya.

atau bisa klik link berikut https://bootstrap.pypa.io/get-pip.py
kemudian simpan file tersebut disuatu folder. Pada kasus ini get-pip.py terdapat pada folder 
Downloads.

2. Install PIP pada python

Selanjutnya buka power shall atau CMD dan pastikan python path telah terinstall pada local machine
Kemudian tuliskan perintah ini
'python get-pip.py'
pastikan path folder pada power shall berada di folder downloads karena get-pip.py berada pada folder downloads

3. Tunggu proses download & instalasi PIP selesai

Pada powershale tanggulah hingga proses instalasi PIP dan proses downloadnya selesai. 
Ini akan memakan waktu berdasarkan kecepatan internet. 

4. Tambahkan wheel & pip pada windows path

PIP membutuhkan wheel terdaftar pada environment variables. Tambahkan path wheel ini pada windows 
enviroment variables. Lokasi wheel.exe / pip.exe ini akan terlihat di console powershell saat pip 
telah berhasil terinstal.
Kemudian tambahkan lokasi path diatas windows environment variables. 

5. verifikasi PIP berhasil terinstall

Langkah terakhir adalah melakukan verifikasi bahwa PIP telah terinstall pada local machine.
Pertama tutup semua windows powershell, kemudian tuliskan perintah dibawah ini
'pip --version'
Jika instalasi berhasil maka akan muncul versi pip yang telah terinstall pada local machine 

## Sekilas COmpiler dan Interpreter
Compiler adalah sebuah program komputer yang berguna untuk menerjemahkan program komputer yang 
ditulis dalam bahasa pemrograman tertentu menjadi program yang ditulis dalam bahasa pemrograman lain. 

Compiler biasa digunakan untuk program komputer yang menerjemahkan program yang ditulis dalam bahasa pemrograman tingkat tinggi seperti bahasa Pascal, C++, basic, fortran, visual basic, visual c#, java, 
xBase, atau cobol menjadi bahasa mesin yang biasanya menggunakan bahasa  assembly sebagai perantara
lebih ringkasnya. Compiler itu sendiri yang menerima kode sumber dan menghasilkan 
bahasa tingkal tingkat rendah (bahasa assembly). 

Assembler yang menerima keluaran kompiler dan menghasilkan berkas objek dalam bahsa mensin. kemudian linker yang nemerima berkas objek keluaran assembler untuk kemudain digabungkan dengan putaka-pustaka yang diperlukan dan menghasilkan program yang dapat dieksekusi 

Interpreter merupakan perangkat lunak yang berfungsi melakukan eksekusi sejumlah instruksi yang ditulis dalam suatu bahasa pemrograman tanpa terlebih dahulu menyusunnya menjadi program bahasa mesin. cara kerja interpreter untuk menjalanakan program yaitu dengan mengeksekusii kode sumber secara langsung atau m
proses atau cara kerja antara compiler dengen interpreter sangat berbeda. 

## Pengenalan Python
Python merupakan bahasa pemrograman tingkat tinggi yang dikembangkan oleh Guido van Rossum pada awal tahun 1990-an. Bahasa python terinspirasi dari bahasa pemrograman ABC.Di tahun 1995, Guido melanjutkan pembuatan python di Corporation for National Research Initiative (CNRI) di Virginia Amerika dimana dia merilis beberapa versi dari python. Semua versi python yang dirilis bersifat open source. Dalam sejarahnya, hampir semua rilis python menggunakan lisensi GFL-compatible. Berikut adalah versi mayor dan minor python beserta dengan tanggal rilisnya:

    Python 1.0 – Januari 1994
        Python 1.2 – 10 April 1995
        Python 1.3 – 12 Oktober 1995
        Python 1.4 – 25 Oktober 1996
        Python 1.5 – 31 Desember 1997
        Python 1.6 – 5 September 2000
    Python 2.0 – 16 Oktober 2000
        Python 2.1 – 17 April 2001
        Python 2.2 – 21 Desemberg 2001
        Python 2.3 – 29 Juli 2003
        Python 2.4 – 30 Nopember 2004
        Python 2.5 – 19 September 2006
        Python 2.6 – 1 Oktober 2008
        Python 2.7 – 3 Juli 2010
    Python 3.0 – 3 Desember 2008
        Python 3.1 – 27 Juni 2009
        Python 3.2 – 20 Februari 2011
        Python 3.3 – 29 September 2012
        Python 3.4 – 16 Maret 2014
        Python 3.5 – 13 September 2015
        Python 3.6 – 23 Desember 2016
        Python 3.7 – 27 Juni 2018

Bahasa Pemrorgaman Python mempunyai konsep sederhana dan bagus dari desainnya yang terfokus untuk kemudahan penggunaan. Kode dalam bahasa Python dirancang supaya lebih mudah untuk membaca, mempelajari dan bisa digunakan ulang.
Selain itu Python juga mendukung berbagai pemograman yang berorientasi kepada objek serta pemograman secara fungsional. Pgram yang tertulis di penggunakan Python ini bisa dijalankan pada semua jenis sistem operarosi (Windows, Unix, Mac OS X, dan lain sebagainya) dan juga bisa digunakan untuk perangkat-perangkat di mobile.

Python juga memiliki banyak keuntungan diantara lain ialah mode interaktif, mode skrip, mode idle.Dalam tiga rangkaian mode tersebut akan dapat memudahkan anda untuk mempelajari bagaimana belajar bahasa pemrograman Python distro linux.Python mempunyai berbagai dukungan pustaka dan dikembangkan dan dirancang oleh pihak ketiga, contohnya para pustaka dengan kegunaan pengembangan web, serta pengembangan sebuah aplikasi secara visual dengan basis GUI, melakukan pengembangan dalam permainan komputer atau game, juga banyak yang lainnya


Referensi 
https://id.wikipedia.org/wiki/Python_(bahasa_pemrograman)
https://www.pythonindo.com/sejarah-python/