from django.shortcuts import render, redirect

from . import models
def Iwak(req):
    if req.POST:
        models.Iwak.objects.create(
            nama_iwak=req.POST['nama_iwak'],
            jenis=req.POST['jenis'],
            harga=req.POST['harga'])
        return redirect('/iwak')

    iwk = models.Iwak.objects.all()
    return render(req, 'iwak.html',                                                
        { 'data': iwk,
        })

def lihat(req, id):
    iwk = models.Iwak.objects.filter(pk=id).first()
    return render(req, 'lihat.html',
        { 'data': iwk,
        })

def ganti(req, id):
    if req.POST:
        Iwak = models.Iwak.objects.filter(pk=id).update(
            nama_iwak=req.POST['nama_iwak'],
            jenis=req.POST['jenis'],
            harga=req.POST['harga'])
        return redirect('/iwak')

    iwk = models.Iwak.objects.filter(pk=id).first()
    return render(req, 'ganti.html',
    {
        'data': iwk,
        })  

def delete(req, id):
    models.Iwak.objects.filter(pk=id).delete()
    return redirect('/iwak')