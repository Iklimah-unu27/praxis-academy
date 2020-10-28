from django.db import models
#setiap merubah model harus melakukan migrate

class Task(models.Model):
    name= models.TextField(null=True, blank=False)
    Warna = models.TextField(default='hijau')
    Jenis_Makanan = models.TextField(default='default')


