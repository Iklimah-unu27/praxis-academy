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