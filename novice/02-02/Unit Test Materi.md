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