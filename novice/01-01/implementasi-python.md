### Implementasi Python

Python adalah bahasa pemrograman interpretatif multiguna dengan filosofi perancangan yang 
berfokus pada tingkat keterbacaan kode. CPython adalah implementasi Python asli. Disebut CPython 
untuk membedakannya dari implementasi Python yang lain, lalu, untuk membedakan penerapan bahasa 
mesin dari bahasa pemrograman Python itu sendiri.

CPython mengkompilasi kode python kamu menjadi bytecode (transparan) dan menafsirkan bytecode 
dalam lingkaran evaluasi. CPython juga yang pertama menerapkan fitur baru. Pengembangan Python 
sebagai bahasa menggunakan basis CPython, implementasi lainnya mengikuti dari pengembangan ini

Jython, IronPython dan PyPy adalah implementasi 'lain' dari bahasa pemrograman Python. Jython diimplementasikan di Java, C# dan RPython (subset dari Python), di implementasika pada lingkungan masing-masing. Jython mengkompilasi kode Python ke Java bytecode, jadi kode Python kamu dapat 
berjalan di JVM. IronPython memungkinkan kamu menjalankan Python di Microsoft CLR. Dan PyPy, yang diimplementasikan di (subset dari) Python, memungkinkan kamu menjalankan kode Python lebih 
cepat dari CPython menggunakan JIT Compiler.

Jadi CPython tidak menerjemahkan kode Python ke C dengan sendirinya. Ini menjalankan sebuah 
interpreter loop. Ada sebuah proyek yang menerjemahkan kode Python ke C, dan itu disebut Cython. 
Cython menambahkan beberapa ekstensi ke bahasa Python, dan memungkinkan untuk mengkompilasi kode 
ke ekstensi C, kode yang dihubungkan ke interpreter CPython. 