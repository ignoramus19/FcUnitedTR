from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import NewsForm
from .models import News
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    news = News.objects.order_by('-created_date')[0:3]
    context = {
        "news":news
    }
    return render(request,"index.html",context)

def history(request):
    return render(request,"history.html")

def membership(request):
    return render(request,"membership.html")

def media(request):
    return render(request,"media.html")
 
def fixtures(request):
    return render(request,"fixtures.html")

def leaguetable(request):
    return render(request,"leaguetable.html")

def yourclub(request):
    return render(request,"yourclub.html")

def squad(request):
    return render(request,"squad.html")

def stadium(request):
    return render(request,"stadium.html")

def news(request):
    news = News.objects.all()
    context = {
        "news":news
    }
    return render(request,"news.html",context)

def detail(request,id):
    news = get_object_or_404(News,id = id)

    #comments = article.comments.all()
    return render(request,"detail.html",{"news":news})
