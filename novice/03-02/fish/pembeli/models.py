from django.db import models

class pembeli (models.Model):
    id_pmbli = models.TextField()
    nama_pmbli = models.TextField()
    alamat = models.TextField()
    total_beli = models.TextField()
    


