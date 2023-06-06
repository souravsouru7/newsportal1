from django.shortcuts import render
from .models import news

def index(request):
    News = news.objects.all().order_by('date_field')
    return render(request,"news/index.html",{'News':News})

def detail(request,id):
    det=news.objects.get(pk=id)
    return render(request,"news/single.html",{"det":det})




# Create your views here.
