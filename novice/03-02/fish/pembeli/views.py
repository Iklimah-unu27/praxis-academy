from django.shortcuts import render, redirect

from . import models
def index(req):
    if req.POST:
        models.pembeli.objects.create(
            nama_pmbli=req.POST['nama_pmbli'],
            alamat=req.POST['alamat'],
            total_beli=req.POST['total_beli'])
        return redirect('/')

    buyer = models.pembeli.objects.all()
    return render(req, 'index.html',                                                
        { 'data': buyer,
        })

# def detail(req, id):
#     ikans = models.ikan.objects.filter(pk=id).first()
#     return render(req, 'ikan/detail.html',
#         { 'data': ikans,
#         })

# def edit(req, id):
#     if req.POST:
#         ikan = models.ikan.objects.filter(pk=id).update(
#             jenis=req.POST['jenis'],
#             harga=req.POST['harga'],
#             diskon=req.POST['diskon'])  
#         return redirect('/')

#     ikans = models.ikan.objects.filter(pk=id).first()
#     return render(req, 'ikan/edit.html',
#     {
#         'data': ikans,
#         })  

# def delete(req, id):
#     models.ikan.objects.filter(pk=id).delete()
#     return redirect('/')