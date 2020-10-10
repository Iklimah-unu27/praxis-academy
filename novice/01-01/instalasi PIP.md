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