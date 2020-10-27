### Pengertian Django 

Django merupakan sebuah framework untuk membuat aplikasi atau website dengan menggunakan python sebagai base programmingny. Django di desain untuk python agar bisa membuat aplikasi dengan menerapkan MTC (Model Template Controller)

### Cara Install Django 

1. Sebelum meninstall django, terlebih dahulu kita harus menginstall python dalam linux  kita. Jika belum punya ketik di terminal 'sudo apt install python3' unutk menginstal python.

2. kemudian install pip
pip adalah package manager untuk Python packages. Dengan pip kita install dan mengatur libraries dan dependencies tambahan yang dibutuhkan oleh aplikasi yang kita kembangkan.
cara install pip 'sudo apt install python3-pip -y'. 
untuk memverifikasi pip telah terinstall ketik 'Verifikasi install pip' nanti akan muncul versi dari pip

3. kemudian install virtualenv
virtualenv adalah virtual environment yang ditujukan untuk aplikasi Python. Dengan menggunakan virtualenv, setiap proyek aplikasi Python terisolasi dengan global environment dari sistem operasi. Isolasi Python environment ini dapat mencegah package conflict antar proyek aplikasi Python dan envrionment sistem operasi.
cara instal virtualenv dengan mnegetik 'sudo su pip3 install virtualenv'
untuk memverifikasi install virtualenv ketik 'virtualenv --version'

4. Menginstal Django
KIta akan menginstall django di dalam virtualenv dengan menggunakan pip, caranya
- Membuat direktori django-apps dengan mengetik 
'mkdir django-apps
cd django-apps'.
- Membuat virtual environment dengan nama env
'virtualenv env'
- Kita aktifkan virtual environment yang tadi telah diinstall dengan 
'source env/bin/activate'
- Setelah mengaktifkan virtual environment, terdapat prefix (env) sebagai tanda bahwa virtual environment telah aktif.
- Lalu install django menggunakan pip
'pip install Django==()'. dalam kurung tulis versi yang kita inginkan
- Verifikasi install Django dengan 
'django-admin --version'. 

### Cara Membuat Projek pada django

Membuat Django project dengan nama (nama_projek)
'django-admin startproject (nama_projek)'.

Jalankan Django dengan menggunakan development server
'cd nama_projek
python manage.py runserver'

Hasil perintah menjalankan development server 
Development server berjalan di port 8000
Lalu browsing http://127.0.0.1:8000. Jika berhasil akan muncul gambar roket.
Untuk menghentikan development server tekan CTRL+C.
Untuk menonaktifkan virtual environment jalankan perintah deactivate.

