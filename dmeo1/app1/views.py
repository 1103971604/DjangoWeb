from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import GmaeInfo,CategroyInfo
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')


def single(request,id):
    good=GmaeInfo.objects.get(pk=id)
    good.ReadNum+=1
    good.save()
    return render(request,'single.html',locals())

def game(request):
    return render(request,'games.html')


def contact(request):
    if request.method== 'GET':

        return render(request,'contact.html',locals())
    else:
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        phone=request.POST.get('Phone')
        city=request.POST.get('City')
        msg=request.POST.get('Message')
        send_mail(name,msg,settings.DEFAULT_FROM_EMAIL,[email])
        return redirect(reverse('app1:contact'))

def news(request,id):

    num = request.GET.get('page')
    if num == None:
        num = 1
    Categroys = GmaeInfo.objects.all().order_by('-ReadNum')
    paginator = Paginator(Categroys, 3)
    page = paginator.get_page(num)
    # return render(request, 'index.html', {'page': page})

    return render(request,'news.html',{'page':page,'cat':Categroys})


def fl(request,id):

    games = CategroyInfo.objects.get(pk=id).gmaeinfo_set.all()
    paginator = Paginator(games, 3)
    page = paginator.get_page(1)
    return render(request, 'news.html', {'page': page})
