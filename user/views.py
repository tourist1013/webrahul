from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    cdata=cities.objects.all()
    pdata=addplace.objects.all().order_by('-id')[0:8]
    mydict={"city":cdata,'place':pdata}
    return render(request,'user/index.html',mydict)


def about(request):
    return render(request,'user/about.html')

def newplace(request):
    city=cities.objects.all().order_by('-id')
    a=request.GET.get('abc')
    place=""
    if a is None:
        place = addplace.objects.all().order_by('-id')
    else:
        place=addplace.objects.filter(city=a)
    mydict={"city":city,"place":place}
    return render(request,'user/newplace.html',mydict)


def guiderdetails(request):
    city = cities.objects.all().order_by('-id')
    a = request.GET.get('abc')
    gd =""
    if a is None:
        gd = guider.objects.all().order_by('-id')
    else:
        gd = guider.objects.filter(city=a)
    mydict = {"city": city, "guider":gd}
    return render(request,'user/guiderdetails.html',mydict)

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Email=request.POST.get("email","")
        Mobile=request.POST.get("mobile","")
        Message=request.POST.get("msg","")
        x=contact(name=Name,mobile=Mobile,email=Email,message=Message)
        x.save()
        status=True
    return render(request,'user/contactus.html',{'S':status})


def viewdetails(request):
    a=request.GET.get('msg')
    data=addplace.objects.filter(id=a)
    return render(request,'user/viewdetails.html',{"d":data})


def signin(request):
    return render(request,'user/signin.html')

def image(request):
    gdata = gallery.objects.all()
    mydict = {"d": gdata}
    return render(request,'user/gallery.html',mydict)

def videogallery(request):
    vdata=video.objects.all().order_by('-id')

    return render(request,'user/videos.html',{'video':vdata})