##  Singkat Perpustakaan Standar

Bawaan dir()dan help()fungsi berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os:

>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>

Untuk file harian dan tugas manajemen direktori, shutilmodul menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'

#### File Wildcard
The globmodul menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard:
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']

#### Command Line Arguments (Argumen Baris Perintah)
Skrip utilitas umum sering kali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut argvsys modul sebagai daftar. Misalnya hasil keluaran berikut dari berjalan di baris perintah:python demo.py one two three
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']

Modul menyediakan mekanisme yang lebih canggih untuk argumen baris perintah proses. Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional untuk ditampilkan:
import argparse
parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
Saat dijalankan pada baris perintah dengan , skrip disetel ke dan ke .python top.py --lines=5 alpha.txt beta.txtargs.lines5args.filenames['alpha.txt', 'beta.txt']

#### Error Output Redirection & Program Termination (Kesalahan Pengalihan Output & Penghentian Program)
Modul juga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan:
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one

Cara paling langsung untuk menghentikan skrip adalah dengan menggunakan sys.exit().

#### String Pattern Matching (Pencocokan Pola String)
Modul menyediakan alat ekspresi reguler untuk pengolahan string yang canggih. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi ringkas dan dioptimalkan:

>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

####  Mathematics (Matematika)
modul memberikan akses ke mendasari C fungsi perpustakaan untuk floating point matematika:
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0

The randomModul menyediakan alat untuk membuat pilihan acak:
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4

The statisticsModul menghitung sifat statistik dasar (mean, median, varians, dll) dari data numerik:
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095

#### Internet Access (Akses Internet)
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua cara yang paling sederhana adalah urllib.requestuntuk mengambil data dari URL dan smtplibuntuk mengirim email:
>>> from urllib.request import urlopen
>>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
...     for line in response:
...         line = line.decode('utf-8')  # Decoding the binary data to text.
...         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...             print(line)

<BR>Nov. 25, 09:43:32 PM EST

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()

#### Dates and Times (Tanggal dan Waktu)
The datetimepersediaan modul kelas untuk memanipulasi tanggal dan waktu di kedua sederhana dan cara yang kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasinya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang peka zona waktu.
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368

#### Data Compression (Kompresi Data)
Pengarsipan data umum dan kompresi format secara langsung didukung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfiledan tarfile.
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979

#### Performance Measurement (Pengukuran Kinerja)
Python menyediakan alat pengukuran untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. The timeit Modul cepat menunjukkan keunggulan kinerja yang sederhana:

>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791

Berbeda dengan timeittingkat perincian yang bagus, modul profiledan pstatsmenyediakan alat untuk mengidentifikasi bagian waktu yang penting dalam blok kode yang lebih besar.

#### Quality Control(Kontrol Kualitas)
Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah menulis pengujian untuk setiap fungsi saat dikembangkan dan menjalankan pengujian tersebut secara sering selama proses pengembangan.
The doctestmodul menyediakan alat untuk memindai modul dan memvalidasi tes tertanam dalam docstrings program ini. Konstruksi pengujian sesederhana memotong dan menempelkan panggilan biasa beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi:

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   

The unittestModul ini tidak mudah seperti doctestmodul, tetapi memungkinkan satu set yang lebih komprehensif dari tes untuk dipertahankan dalam file terpisah:

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()

#### Batteries Included(Baterai Termasuk)
Python memiliki filosofi "termasuk baterai". Hal ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket yang lebih besar. Sebagai contoh:

- The xmlrpc.clientdan xmlrpc.servermodul membuat melaksanakan prosedur panggilan jarak jauh ke dalam tugas yang hampir sepele. Terlepas dari nama modul, tidak diperlukan pengetahuan langsung atau penanganan XML.

- The emailpaket perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis RFC 2822 . Tidak sepertismtplibdan poplibyang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat yang lengkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk mengimplementasikan encoding internet dan protokol header.

- The jsonpaket menyediakan dukungan kuat untuk parsing format data interchange populer ini. The csvdukungan modul membaca langsung dan menulis file dalam format Nilai Comma-Separated, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh xml.etree.ElementTree, xml.domdan xml.saxpaket. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

- The sqlite3modul pembungkus untuk perpustakaan basis data SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL sedikit tidak standar.

-Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan codecspaket.
