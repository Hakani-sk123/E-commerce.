"""Project16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app16 import views
from Project16 import settings

urlpatterns = [
    path('', views.showIndex, name='main'),
    path('Usersite/',views.Usersite,name='Usersite'),
    path('usercreateAc/',views.usercreateAc,name='usercreateAc'),
    path('UserAcSave/',views.UserAcSave,name='UserAcSave'),
    path('userLogin/',views.userLogin,name='userLogin'),
    path('UserLogin1/',views.UserLogin1,name='UserLogin1'),
    path('Adminsite/',views.Adminsite,name='Adminsite'),
    path('AdmincreateAc/',views.AdmincreateAc,name='AdmincreateAc'),
    path('AdminAcSave/',views.AdminAcSave,name='AdminAcSave'),
    path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
    path('AdminLogin1/',views.AdminLogin1,name='AdminLogin1'),
    path('save_product/',views.save_product,name='save_product'),
    path('AddtoCart/',views.AddtoCart,name='AddtoCart'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

