from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)
    def __str__(self):
        return self.email
class category(models.Model): # category is table name
    cname=models.CharField(max_length=30)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()

class profile(models.Model):
    name=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=100)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=2000)

class cities(models.Model):
    cname=models.CharField(max_length=100)
    cpic=models.ImageField(upload_to='static/city',default="")
    cdate=models.DateField()

    def __str__(self):
        return self.cname


class addplace(models.Model):
    ptitle=models.CharField(max_length=200)
    city=models.ForeignKey(cities,on_delete=models.CASCADE)
    baplace=models.CharField(max_length=400)
    pdes=models.TextField(max_length=5000)
    placepic=models.ImageField(upload_to='static/place/',default="")
    pdate=models.DateField()

    def __str__(self):
        return self.baplace

class guider(models.Model):
    name=models.CharField(max_length=100)
    city=models.ForeignKey(cities,on_delete=models.CASCADE)
    guiderpic=models.ImageField(upload_to='static/guider/',default="")
    qualification=models.CharField(max_length=100)
    gid=models.CharField(max_length=30)
    gidp=models.CharField(max_length=30)
    mobile=models.CharField(max_length=20)
    address=models.TextField(max_length=1000)
    gdate=models.DateField()

class gallery(models.Model):
    gname=models.CharField(max_length=200)
    gpic=models.ImageField(upload_to='static/gallery',default="")
    gdate=models.DateField()

class video(models.Model):
    vtitle=models.CharField(max_length=200)
    vdes=models.TextField(max_length=600)
    thumb=models.ImageField(upload_to='static/thumbnail/',default="")
    vlink=models.CharField(max_length=500)
    vdate=models.DateField()