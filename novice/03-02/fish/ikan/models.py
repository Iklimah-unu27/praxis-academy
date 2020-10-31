from django.db import models

class ikan (models.Model):
    id_ikan = models.TextField(default='')
    jenis = models.TextField(default='default')
    harga = models.TextField(default='default')
    diskon = models.TextField(default='default')
