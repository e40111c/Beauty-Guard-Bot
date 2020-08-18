"""my_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from foodlinebot import views
from foodlinebot.views import hello_view
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodlinebot/', include('foodlinebot.urls')), #包含應用程式的網址
    url(r'^hello/', hello_view,name='hello_view'),
    
    url(r'^suit',SuitProduct,name='SuitProduct'),
    url(r'^scos',SuitCos,name='SuitCos'),
    url(r'^sfou',SuitFou,name='SuitFou'),
    url(r'^sskin',SuitSkin,name='SuitSkin'),

    url(r'^nsuit',NonSuitProduct,name='NonSuitProduct'),
    url(r'^ncos',NonSuitCos,name='NonSuitCos'),
    url(r'^nfou',NonSuitFou,name='NonSuitFou'),
    url(r'^nskin',NonSuitSkin,name='NonSuitSkin'),

    url(r'^waitpro',WaitProduct,name='WaitProduct'),
    url(r'^wskin',WaitProductCare,name='WaitProductCare'),
    url(r'^wcos',WaitProductCos,name='WaitProductCos'),
    url(r'^wfou',WaitProductFou,name='WaitProductFou'),
    
    
    
]





