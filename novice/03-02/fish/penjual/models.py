from django.db import models

class penjual (models.Model):
    id_pnjual = models.TextField(default='')
    nm_penjual = models.TextField(default='default')
    email = models.TextField(default='default')
    no_telf = models.TextField(default='default')    
    data_ikan = models.TextField(default='default')
    ikan_terjual = models.TextField(default='default')
    stok = models.TextField(default='default')
