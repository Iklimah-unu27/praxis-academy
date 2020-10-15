### CRD Card (responsibility )

Kartu CRC (Class Responsibility Collaborator) sendiri merupakan kumpulan kartu indeks standar yang telah dibagi menjadi tiga bagian yaitu class, responsibilities, dan collaborator. 
Sebelum membuat kartu CRC kita sudah harus tahu terlebih dahulu kelas apa saja yang ada dalam sistem yang kita buat, oleh karena itu kita perlu membuat terlebih dahulu Class Diagram dari sistem yang kita analisis

CRC Card adalah satu cara untuk pengaambaran diagram UML sederhana dimana crd card dapat 
digunakan untuk mengetahui reponsibility dan kolaborasi yang ada dr sebuah kelas.
Kelas mewakili sekumpulan objek serupa. 
Tanggung jawab adalah sesuatu yang diketahui atau dilakukan kelas, dan 
kolaborator adalah kelas lain yang berinteraksi dengan kelas untuk memenuhi tanggung jawabnya

Responsibilities merupakan hal-hal yang dikerjakan dan yang diketahui oleh suatu Class. 
Collaborator merupakan class lain yang berinteraksi untuk dapat memenuhi Responsibilities suatu Class. Untuk skema bagaimana bentuk dari CRC card ini sendiri dapat dilihat di bawah ini.

Software system terdiri dari modul-modul, dimana masing-masing modul memiliki peran/fungsi yang khusus. Modul-modul tersebut saling berinteraksi dalam sistem. Pada program yang berorientasi obyek modul-modul tersebut berupa class.

Class ≈ Moduld

CRC Card

Kartu tersebut dibagi menjadi tiga area:

    1. Di atas kartu, nama kelas
    2. Di sebelah kiri, tanggung jawab kelas
    3. Di sebelah kanan, kolaborator (kelas lain) yang berinteraksi dengan kelas ini untuk memenuhi tanggung jawabnya

Elemen card ada dua bagian yitu bagian depan dan bagian belakang
Bagian Depan 
- Kelas nama => nama dari sbuah kelas harus berupa kata benda
- ID => identitas dr DRD Card yang dapat digunakan sebegai identifikasi sebuah CRD
- Type => tipe dr setiap CRD Card
- Deskription => definisi tertulis dari sebuah class dan hanya berupa keterangan pendek
- Assosiated Use Case => jumlah use case yang terkait dengan sebuah clas
- responsibilities  => oprasion yg dilakkukan oleh sebuah klass
- collaborators => hubungan dengan kelas lain 

Bagian Belakang 
- Attributes => representasi dari sebuah class agar dapat mengetahui responsibilities dari 
setiap instance class lain 
- Relationship => hubungan dengan kelas lain ter diri dari 3 ( generalization, aggregation, 
other association)

Menggunakan kartu kecil meminimalkan kerumitan desain. Ini memfokuskan desainer pada esensi kelas dan mencegah mereka masuk ke detail dan implementasinya pada saat detail seperti itu mungkin kontra-produktif. Itu juga mengecilkan hati memberi kelas terlalu banyak tanggung jawab. Karena kartu ini portabel, kartu dapat dengan mudah diletakkan di atas meja dan diatur ulang saat mendiskusikan desain.


Contoh nya bisa dilihat di https://faishal15.wordpress.com/2016/09/29/crc-modelling-dan-class-diagram-dari-sistem-manajaemen-informasi-destinasi-wisata-bagi-turis/s

