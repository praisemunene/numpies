"""
URL configuration for csveditor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('removefiltered', views.removefiltered, name="removefiltered"),
    path('savefiltered', views.savefiltered, name="savefiltered"),
    path('split', views.split, name="split"),
    path('merge', views.merge, name="merge"),
    path('mergefiles', views.mergefiles, name="mergefiles"),
    path('converttocsv', views.converttocsv, name="converttocsv"),
    path('tocsv', views.tocsv, name="tocsv"),
    path('cleandata', views.cleandata, name="cleandata"),
]
