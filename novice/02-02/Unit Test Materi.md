### UNIT TEST 

#### Pengertian Unit Test 

Pengujian unit atau testing adalah proses untuk memastikan bahwa kode yang ditulis sudah beralan dengan seharusnya. Tujuan ini dapat dicapai dengan berbagai cara mulai dari secara manual memasukkan beberapa nilai dan memastikan hasil yang didapat sudah benar, hingga membuat serangkaian tes terstruktur yang berjalan secara otomatis dan memastikan bahwa kesuluruhan program sudah berjalan dengan seharusnya. 

Teknik ini dilakukan dengan cara melakukan pengecekan satu blok kode (biasanya sebuah fungsi) dan memastikan bahwa blok tersebut sudah berjalan dengan benar. 

### Test Driven Development

Saat belajar software development kita harus menulis sebuah tes saat memulai proyek baru. Paradigma ini (dikenal dengan istilah test driven development atau TDD) melakukan pengujian bukan hanya untuk mencari bug, tapi juga membangun spesifikasi program itu sendiri.

Proses TDD mengikuti langkah-langkah berikut:
- Tulis tes baru
- Jalankan semua tes dan lihat apakah ada yang gagal
- Jika satu atau lebih tes gagal, tulis kode untuk mengatasi masalah yang ada
- Jalankan lagi tesnya
- Jika tes yang dijalankan semua lolos, lanjutkan pekerjaan, jika tidak kembali ke langkah pertama.

Perangkat lunak yang dibangun dengan TDD akan berevolusi seiring dengan penambahan tes baru untuk fitur baru. Perangkat lunak ini akan selalu lolos uji karena fitur baru hanya akan ditambahkan jika ada sebuah tes yang dapat menentukan tingkah lakunya dan karena semua tes dijalankan secara otomatis bersama-sama, maka dapat dipastikan perangkat lunak ini teruji

### PyUnittest

Salah satu modul Python yang paling populer untuk melakukan testing yang mempermudah pekerjaan kita dalam mengatur test case. 

### Doctest

pencarian modul untuk potongan teks yang terlihat seperti sesi Python interaktif di docstrings, dan kemudian mengeksekusi mereka sesi untuk memverifikasi bahwa mereka bekerja persis seperti yang ditunjukkan.
Doctests biasanya kurang mendetail dan tidak menangkap kasus khusus atau mengaburkan bug regresi.  biasanya berguna sebagai dokumentasi ekspresif dari kasus penggunaan utama modul dan komponennya. doctests berjalan secara otomatis setiap kali rangkaian pengujian lengkap dijalankan.

### Hipotesis

Hipotesis adalah pustaka yang memungkinkan untuk menulis pengujian yang diparameterisasi oleh sumber contoh. Kemudian menghasilkan contoh sederhana dan dapat dipahami yang membuat pengujian Anda gagal, memungkinkan Anda menemukan lebih banyak bug dengan sedikit pekerjaan

### Tox

tox adalah alat untuk mengotomatiskan pengelolaan lingkungan pengujian dan pengujian terhadap beberapa konfigurasi interpreter. tox memungkinkan Anda mengonfigurasi matriks pengujian multi-parameter yang rumit melalui file konfigurasi gaya sederhana.

### Mock

adalah perpustakaan untuk pengujian dengan Python yang memungkinkan Anda mengganti bagian sistem yang sedang diuji dengan objek tiruan dan membuat pernyataan tentang bagaimana mereka telah digunakan.

#### Fungsi Assert Lain
dengamenggunakan assertEqual untuk menguji apakah sebuah tes berhasil atau gagal. Selain opsi ini ada pula fungsi assert lain yang dapat dipilih. Beberapa yang paling populer adalah assertTrue(statement), assertRaises(exception), assertIsInstance(object, class) dan assertAlmostEqual(value1, value2).
