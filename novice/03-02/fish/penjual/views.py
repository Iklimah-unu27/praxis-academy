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

# def edit(req, id):
#     if req.POST:
#         pembeli = models.pembeli.objects.filter(pk=id).update(
#             nama_pmbli=req.POST['nama_pmbli'],
#             alamat=req.POST['alamat'],
#             total_beli=req.POST['total_beli'])  
#         return redirect('/')

#     buyer = models.pembeli.objects.filter(pk=id).first()
#     return render(req, 'edit.html',
#     {
#         'data': buyer,
#         })  

# def delete(req, id):
#     models.pembeli.objects.filter(pk=id).delete()
#     return redirect('/')
