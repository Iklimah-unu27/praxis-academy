from django.shortcuts import render, redirect

from . import models
def index(req):
    if req.POST:
        models.pembeli.objects.create(
            nama_pmbli=req.POST['nama_pmbli'],
            alamat=req.POST['alamat'],
            total_beli=req.POST['total_beli'])
        return redirect('/pembeli/')

    buyer = models.pembeli.objects.all()
    return render(req, 'indexx.html',                                                
        { 'data': buyer,
        })

def detail(req, id):
    buyer = models.pembeli.objects.filter(pk=id).first()
    return render(req, 'detail.html',
        { 'data': buyer,
        })

def edit(req, id):
    if req.POST:
        pembeli = models.pembeli.objects.filter(pk=id).update(
            nama_pmbli=req.POST['nama_pmbli'],
            alamat=req.POST['alamat'],
            total_beli=req.POST['total_beli'])  
        return redirect('/pembeli')

    buyer = models.pembeli.objects.filter(pk=id).first()
    return render(req, 'edit.html',
    {
        'data': buyer,
        })  

def delete(req, id):
    models.pembeli.objects.filter(pk=id).delete()
    return redirect('/pembeli')