from django.db import models

class Penjual (models.Model):
    id_penjual = models.TextField(default='')
    nm_penjual = models.TextField(default='default')
    alamat = models.TextField(default='default')
    stok_ikan = models.TextField(default='default')
    