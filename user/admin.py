from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id',"cname","cpic","cdate")
admin.site.register(category,categoryAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","passwd",'ppic','address')
admin.site.register(profile,profileAdmin)

class citiesAdmin(admin.ModelAdmin):
    list_display=('id',"cname","cpic","cdate")
admin.site.register(cities,citiesAdmin)

class addplaceAdmin(admin.ModelAdmin):
    list_display=("id","ptitle","city","baplace","pdes","placepic","pdate")
admin.site.register(addplace,addplaceAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display=("id","gname","gpic","gdate")
admin.site.register(gallery,galleryAdmin)

class guiderAdmin(admin.ModelAdmin):
    list_display=("name","city","guiderpic","qualification","gid","gidp","address","gdate","mobile")
admin.site.register(guider,guiderAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display=('id','vtitle','vdes','thumb','vlink','vdate')
admin.site.register(video,videoAdmin)