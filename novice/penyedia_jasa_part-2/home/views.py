from django.shortcuts import render, redirect
from .models import UserProfileInfo
from django.db.models import CharField, Count
from django.db.models import Sum
from home.models import dataguru, datamurid
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import imgform


# Create your views here.

def Htampil(request):
    if request.user.is_authenticated:
        #x=UserProfileInfo.objects.aggregate(Max('nodata'))
        #y=x.objects.annotate(diff=F(x) + F(1))

        usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
        dtgr = dataguru.objects.all()
        dtms = datamurid.objects.all()
        idx = usr.id
        tmp = 0
        for p in dtgr:
            if p.no_id==idx:
                tmp += 1
        tmp2 = 0 
        for z in dtms:
            if z.no_id==idx:
                tmp2 += 1
        data = {
            'usrx':usr,
            'datax':dtgr,#data
            'temp':tmp,
            'temp2':tmp2,
            # 'cstm':priv,#custom
            # 'test': x
            # 'testy': y
        }
        return render(request, 'vhome/index.html',data)

def Hguru(request):
    return render(request, 'vhome/guru.html')

def Habout(request):
    return render(request, 'vhome/about.html')

def sd(request):
    return render(request, 'vhome/sd.html')

def smp(request):
    return render(request, 'vhome/smp.html')

def profilgr(request,id):
    task = dataguru.objects.filter(pk=id).first()
    return render(request, 'vhome/profil.html',{ 
        'list' : task,
    })

    # if request.POST:
    #     dataguru.objects.filter(pk=id).first()
        
    # dtguru = models.murid.objects.all()
    # return render(request, 'vhome/profil.html',
    #     { 'data': dtguru,
    #     })
    

def form(request,no):
    x=no
    # if request.method == 'POST': 
    #     iform = imgform(data=request.POST)
    #     if iform.is_valid():
    #         # file is saved
    #         iform.save()
    if request.POST:
        dataguru.objects.create(
         nama=request.POST['nama'],
         alamat=request.POST['alamat'],
         biaya=request.POST['biaya'],
         no_id=x,
         nohp=request.POST['nohp'],
         usia=request.POST['usia'],
         link=request.POST['link'],
         img=request.FILES['image'],
         )
        
        return redirect('home')
    uy = dataguru.objects.all()
    return render(request,'vhome/form.html',{ 
        'd' : uy,
        # 'iform':iform,
        })
def formklien(request,no):
    
    # if request.method == 'POST': 
    #     iform = imgform(data=request.POST)
    #     if iform.is_valid():
    #         # file is saved
    #         iform.save()
    if request.POST:
        datamurid.objects.create(
         nama=request.POST['nama'],
         alamat=request.POST['alamat'],
         no_id=no,
         nohp=request.POST['nohp'],
         pnd=request.POST['pnd'],
         usia=request.POST['usia'],

         )
        
        return redirect('home')
    ey = dataguru.objects.all()
    return render(request,'vhome/formklien.html',{ 
        'e' : ey,
        # 'iform':iform,
        })

    # if request.POST:
    #     dataguru.objects.filter(no_id=no).update(
    #     nama=request.POST['nama'],
    #     alamat=request.POST['alamat'],
    #     biaya=request.POST['biaya'],
    #     nohp=request.POST['nohp'],
    #     )
    #     return redirect('masuk')
    # task = models.datamasuk.objects.filter(no_id=no).first()
    # return render(request, 'vhome/form.html',
    # { 'data' : task,
    # })
