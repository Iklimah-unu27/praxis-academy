## OOP ( Pemrograman Berorientasi Objek )

OOP adalah paradigma pemrograman dan bukan konsep Python. Lebih mudahnya OOP adalah teknik pemrograman di mana semua hal dalam program dimodelkan seperti objek dalam dunia nyata. Objek di dunia nyata memiliki ciri atau attribut juga aksi atau kelakuan.Fitur objek adalah prosedur objek itu sendiri dapat mengakses dan sering kali memodifikasi bidang datanya sendiri. 

Bahasa pemrograman berorientasi objek (OOP) dibuat, seperti Simula, Smalltalk, C++, C #, Eiffel, 
PHP, dan Java. Dalam bahasa ini, data dan metode untuk memanipulasinya disimpan sebagai satu unit 
yang disebut objek. Salah satu fitur yang membedakan dari OOP yaitu satu-satunya cara bahwa objek 
lain atau pengguna akan dapat mengakses data melalui metode objek. 

Semua unit dalam program bisa dianggap sebagai objek. Objek besar dibangun dari objek–objek yang 
lebih kecil. Objek yang satu berinteraksi dengan objek yang lain, sehingga semua menjadi sebuah 
kesatuan yang utuh. Python menggunakan paradigma pemrograman lama yaitu pemrograman terstruktur. 
Oleh karena itu, Python disebut bersifat hibrid.

#### Berikut istilah yang berkaitan dengan tentang OOP:
- Kelas – Kelas adalah cetak biru atau prototipe dari objek dimana kita mendefinisikan atribut dari suatu objek. Atribut ini terdiri dari data member (variabel) dan fungsi (metode).
- Variabel Kelas – Variabel kelas adalah variabel yang dishare atau dibagi oleh semua instance (turunan) dari kelas. Variabel kelas didefinisikan di dalam kelas, tapi di luar metode-metode yang ada dalam kelas tersebut.
- Data member – Data member adalah variabel yang menyimpan data yang berhubungan dengan kelas dan objeknya
- Overloading Fungsi – Overloading fungsi adalah fungsi yang memiliki nama yang sama di dalam kelas, tapi dengan jumlah dan tipe argumen yang berbeda sehingga dapat melakukan beberapa hal yang berbeda.
- Overloading operator – Overloading operator adalah pembuatan beberapa fungsi atau kegunaan untuk suatu operator. Misalnya operator + dibuat tidak hanya untuk penjumlahan, tapi juga untuk fungsi lain.
Variabel instansiasi – Variabel instansiasi adalah variabel yang didefinisikan di dalam suatu metode dan hanya menjadi milik dari instance kelas.
- Pewarisan/Inheritansi – Inheritansi adalah pewarisan karakteristik sebuah kelas ke kelas lain yang menjadi turunannya.
- Instance – Instance adalah istilah lain dari objek suatu kelas. Sebuah objek yang dibuat dari prototipe kelas Lingkaran misalnya disebut sebagai instance dari kelas tersebut.
- Instansiasi – Instansiasi adalah pembuatan instance/objek dari suatu kelas
Metode – Metode adalah fungsi yang didefinisikan di dalam suatu kelas
- Objek – Objek adalah instansiasi atau perwujudan dari sebuah kelas. Bila kelas adalah prototipenya, dan objek adalah barang jadinya

### Pengertian Class
class adalah mekanisme yang digunakan untuk membuat struktur data pengguna baru yang ditentukan. Ini berisi data serta metode yang digunakan untuk memproses data tersebut.

### Pengertian Instance
Instance adalah salinan class dengan nilai sebenarnya , secara harfiah merupakan objek class tertentu.
Sementara class adalah cetak biru yang digunakan untuk menggambarkan bagaimana membuat sesuatu, instance adalah objek yang dibuat dari cetak biru tersebut.
class PythonclassName:
CamelCase notasi, dimulai dengan huruf kapital — yaitu, PythonclassName()
Anda menggunakan nama class, diikuti dengan tanda kurung. Jadi jika nama classnya Kucing(), contoh Kucingnya adalah - my_class = Kucing().
Dengan notasi titik — misalnya, instance_name.attribute_name
Sebuah fungsi yang didefinisikan di dalam class.
Argumen pertama dari setiap metode merujuk pada instance class saat ini, yang menurut konvensi, diberi nama self. Dalam __init__metode ini, selfmengacu pada objek yang baru dibuat; sementara dalam metode lain, selfmengacu pada contoh yang metode namanya disebut. 

#### Pengertian Init
__init__Metode menginisialisasi sebuah instance dari class.
class child mewarisi semua atribut dan perilaku parents