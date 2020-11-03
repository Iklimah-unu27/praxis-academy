from django.shortcuts import render, redirect

from . import models
def index(req):
    if req.POST:
        models.penjual.objects.create(
            nm_penjual=req.POST['nm_penjual'],
            email=req.POST['email'],
            no_telf=req.POST['no_telf'],
            data_ikan=req.POST['data_ikan'],
            ikan_terjual=req.POST['ikan_terjual'],
            stok=req.POST['stok'])
        return redirect('/')

    seller = models.penjual.objects.all()
    return render(req, 'index.html',                                                
        { 'data': seller,
        })

def detail(req, id):
    seller = models.penjual.objects.filter(pk=id).first()
    return render(req, 'detail.html',
        { 'data': seller,
        })
        