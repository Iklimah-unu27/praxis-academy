from django.shortcuts import render, redirect

from . import models
def Penjual(req):
    if req.POST:
        models.Penjual.objects.create(
            nm_penjual=req.POST['nm_penjual'],
            alamat=req.POST['alamat'],
            no_telf=req.POST['no_telf'],
            stok_ikan_hias=req.POST['stok_ikan_hias'],
            stok_ikan_konsum=req.POST['stok_ikan_konsum'],
            total_terjual=req.POST['total_terjual'])
        return redirect('/penjual')

    adm = models.Penjual.objects.all()
    return render(req, 'penjual.html',                                                
        { 'data': adm,
        })

def view(req, id):
    adm = models.Penjual.objects.filter(pk=id).first()
    return render(req, 'view.html',
        { 'data': adm,
        })

def ubah(req, id):
    if req.POST:
        Penjual = models.Penjual.objects.filter(pk=id).update(
            nm_penjual=req.POST['nm_penjual'],
            alamat=req.POST['alamat'],
            no_telf=req.POST['no_telf'],
            stok_ikan_hias=req.POST['stok_ikan_hias'],
            stok_ikan_konsum=req.POST['stok_ikan_konsum'],
            total_terjual=req.POST['total_terjual']) 
        return redirect('/penjual')

    adm = models.Penjual.objects.filter(pk=id).first()
    return render(req, 'ubah.html',
    {
        'data': adm,
        })  

def delete(req, id):
    models.Penjual.objects.filter(pk=id).delete()
    return redirect('/penjual')