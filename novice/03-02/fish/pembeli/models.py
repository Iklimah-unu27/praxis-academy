from django.db import models

class pembeli (models.Model):
    id_pmbli = models.TextField(default='')
    nama_pmbli = models.TextField(default='default')
    alamat = models.TextField(default='default')
    total_beli = models.TextField(default='default')
    


