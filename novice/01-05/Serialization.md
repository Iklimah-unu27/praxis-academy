## Serialization

### Pengertian Serialization

Serialisasi adalah proses pengubahan suatu objek menjadi urutan bit agar dapat disimpan pada media penyimpanan (komputer atau memori) atau ditransmisikan melalui saluran koneksi jaringan.

Rangkaian bit ini dibaca ulang sesuai dengan format serialisasinya. ia dapat digunakan untuk menciptakan klon identik semantis dari objek asalnya. Bagi banyak objek kompleks, misalnya objek yang banyak menggunakan rujukan, proses ini tidak dapat dilakukan begitu saja

Proses serialisasi suatu obyek ini dapat juga disebut pengempisan (deflating) atau penyusunan(marshalling) obyek. Operasi kebalikannya, pembuatan struktur data dari rangkaian bita, adalah deserialisasi, atau disebut juga penggembungan (inflating) atau pembongkaran (unmarshalling) obyek.

Serialisasi digunakan sebagai:

- Cara untuk melakukan penyimpanan objek yang lebih mudah dibandingkan menuliskan properti atas objek-objek tersebut ke dalam berkas teks, dan mengembalikannya sebagai objek.
- Salah satu proses yang dilakukan dalam pemanggilan prosedur jarak jauh 
- Salah satu cara untuk mendistribusikan objek, khususnya dalam arsitektur berbasis komponen
- Salah satu cara untuk mendeteksi perubahan data dalam satu periode waktu tertentu.

### Pickle

Pickly adalah sebuah modul pada standard library python, yang dapat digunakan untuk menyimpan 
dan membaca data ke dalam /dari sebuah file.

Pickle dapat digunakan untuk menyimpan data ke dalam sebuah file, membacanya kembali dari 
file tersebut saat dibutuhkan

####  Pengertian JSON

JSON adalah salah satu bahasa markup yang dapat melakukan pertukaran data dimana JSON ini dibuat berdasarkan javascript dan pastinya sintaknya lebih ke javascript. Dengan membuat sebuah JSON sama halnya dengan kita membuat sebuah object pada javascript itu sendiri. Di dalam membuat JSON pasti kita bakal berkenalan dengan yang namanya array pada javascript sehingga memudahkan bagi para deveploper/programmer.

#### Pengertian XML 

XML adalah bahasa markup untuk dokumen yang berisi informasi yang terstruktur.

Adapun perbedaan dari keduanya :
JSON :
1. Mendukung array
2. Mendukung pembuatan Object
3. Sintak pendek
4. Dapat berpadu dengan AJAX
5. Akses data cepat

XML :
1. Tidak mendukung array
2. Tag dibuat manual/dideklarasikan oleh programmer
3. Ukuran data besar
4. Harus menggunakan XML DOM jika ingin memetakan teks/data
5. Dapat berpadu dengan AJAX

Dapat simpulkan bahwa JSON lebih unggul dari pada xml itu sendiri karena ketika mengakses sebuah data dengan menggunakan xml maka kita memerlukan yang namanya DOM XML dab DOM HTML. Disini membutuhkan request dari server dan menyebabkan si XML itu sendiri akan lambat dalam akses sebuah data.
jika kita menggunakan JSON kita hanya butuh akses melalui javascript dan jika ingin ditampilkan hanya dengan menggunakan HTML DOM yaitu dengan cara kita ambil data dari JSON melalui array javascript lalu kita set datanya ke HTML maka data akan tampil

<!-- https://docs.python-guide.org/scenarios/serialization/ -->