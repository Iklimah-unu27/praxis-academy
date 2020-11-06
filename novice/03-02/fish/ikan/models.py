from django.db import models

class ikan (models.Model):
    id_ikan = models.TextField(default='')
    nama = models.TextField(default='')
    jenis = models.TextField(default='default')
    harga_satuan = models.TextField(default='default')
    harga_kiloan = models.TextField(default='default')
    diskon = models.TextField(default='default')
