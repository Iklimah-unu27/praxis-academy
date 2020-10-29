from django.shortcuts import render,redirect

from . import models


#cara nambah data(create)
#nama abis create, itu dr mneyesuaikan model, klo yg dalem kurung mneyesuaikan nama yg ada di template
def index(req):
    if req.POST:
        models.Task.objects.create(
            name=req.POST['nama'],
            warna=req.POST['warna'],
            jenis_makanan=req.POST['jenis_makanan'])
        return redirect('/')

    tasks = models.Task.objects.all()
    return render(req, 'task/index.html',
        { 'data': tasks,
        })
   
#untuk menampilkan / view    
def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html',
        { 'data': task,
        })

#just for edit 
def edit(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(
            name=req.POST['name'],
            warna=req.POST['warna'],
            jenis_makanan=req.POST['jenis_makanan'])  
        return redirect('/')

    tasks = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/edit.html',
    {
        'data': tasks,
        })  

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')