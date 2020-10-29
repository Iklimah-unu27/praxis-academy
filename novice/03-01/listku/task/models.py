from django.db import models
#setiap merubah model harus melakukan migrate

class Task(models.Model):
    name = models.TextField(default='noname')
    warna = models.TextField(default='pilih warna')
    jenis_makanan = models.TextField(default='default')


