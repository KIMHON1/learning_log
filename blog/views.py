from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    article = Article.objects.all()
    return render(request,'blog/home.html',context={'article_list':article})


def show(request, id,**kwargs):
    article_detail = Article.objects.get(id)
    return render(request, 'blog/show.html',context={'article_detials':article_detail})