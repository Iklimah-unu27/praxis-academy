from django.shortcuts import render, redirect

from . import models
def Penjual(req):
    if req.POST:
        models.Penjual.objects.create(
            nm_penjual=req.POST['nm_penjual'],
            alamat=req.POST['alamat'],
            stok_ikan=req.POST['stok_ikan'])
        return redirect('/Penjual')

    adm = models.Penjual.objects.all()
    return render(req, 'penjual.html',                                                
        { 'data': adm,
        })