from django.shortcuts import render
from django.shortcuts import render, redirect
from home.models import dataguru,datamurid
from django.contrib import messages
from pengelola.forms import FormGuru, FormMurid

# Create your views here.

def tampil(request):
    return render(request, 'index.html')

def murid(request):
    return render(request, 'murid.html')

# PENGAJAR

def tampilguru(request):
    if request.POST:
        dataguru.objects.all()
        
    ptampil = dataguru.objects.all()
    return render(request, 'pengajar.html',
		{ 'data': ptampil,
		})

def detailguru(request, id):
	gdetail = dataguru.objects.filter(pk=id).first()
	return render(request, 'detailpengajar.html',
		{ 'data': gdetail,
		})

def editguru(request, id):
    juduls = dataguru.objects.get(pk=id)
    template = 'editguru.html'
    if request.POST:
        form = FormGuru(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            return redirect('/pengelola/tampilguru', id=id)
    else:
        form = FormGuru(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def deleteguru(request, id):
    delete_d = dataguru.objects.filter(pk=id).delete()
    return redirect('/pengelola/tampilguru')

# MURID

def tampilmurid(request):
    if request.POST:
        datamurid.objects.all()
        
    mtampil = datamurid.objects.all()
    return render(request, 'murid.html',
		{ 'data': mtampil,
		})

def detailmurid(request, id):
	mdetail = datamurid.objects.filter(pk=id).first()
	return render(request, 'detailmurid.html',
		{ 'data': mdetail,
		})

def editmurid(request, id_murid):
    juduls = datamurid.objects.get(id=id_murid)
    template = 'editmurid.html'
    if request.POST:
        form = FormMurid(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            return redirect('/pengelola/tampilmurid', id_murid=id_murid)
    else:
        form = FormMurid(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def deletemurid(request, id):
    delete_d = datamurid.objects.filter(pk=id).delete()
    return redirect('/adminapp/tampilmurid')