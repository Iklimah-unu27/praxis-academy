from django.db import models

class Penjual (models.Model):
    id_penjual = models.TextField(default='')
    nm_penjual = models.TextField(default='default')
    alamat = models.TextField(default='default')
    no_telf = models.TextField(default='default')
    stok_ikan_hias = models.TextField(default='default')
    stok_ikan_konsum = models.TextField(default='default')
    total_terjual = models.TextField(default='default')
    