from django.shortcuts import render,redirect

from . import models

def index(req):
    if req.POST:
        models.ikan.objects.create(
            jenis=req.POST['jenis'],
            harga=req.POST['harga'],
            diskon=req.POST['diskon'])
        return redirect('/ikan/')

    ikans = models.ikan.objects.all()
    return render(req, 'ikan/index.html',
        { 'data': ikans,
        })

def detail(req, id):
    ikans = models.ikan.objects.filter(pk=id).first()
    return render(req, 'ikan/detail.html',
        { 'data': ikans,
        })

def edit(req, id):
    if req.POST:
        ikan = models.ikan.objects.filter(pk=id).update(
            jenis=req.POST['jenis'],
            harga=req.POST['harga'],
            diskon=req.POST['diskon'])  
        return redirect('/ikan/')

    ikans = models.ikan.objects.filter(pk=id).first()
    return render(req, 'ikan/edit.html',
    {
        'data': ikans,
        })  

def delete(req, id):
    models.ikan.objects.filter(pk=id).delete()
    return redirect('/ikan/')

