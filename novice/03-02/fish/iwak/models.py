from django.db import models

class Iwak (models.Model):
    id_iwak = models.TextField(default='')
    nama_iwak = models.TextField(default='default')
    harga = models.TextField(default='default')
    stok = models.TextField(default='default')
    