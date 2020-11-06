from django.shortcuts import render, redirect

# def halog(req):
#    return render(req, 'halog.html')

def index(req):
   return render(req, 'index.html')