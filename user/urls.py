from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('newplace/',views.newplace),
    path('guiderdetails/',views.guiderdetails),
    path('viewdetails/',views.viewdetails),
    path('signin/',views.signin),
    path('gallery/',views.image),
    path('video/',views.videogallery),

]