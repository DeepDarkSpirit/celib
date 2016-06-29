"""celib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include,url
from django.contrib import admin
admin.autodiscover()
from demo import views
#####
from demo.newBookResultView import newBookResult
from demo.loanResultView import loanResult
from demo.editBookResultView import editBookResult
from DJangoHotel.viewspackage.orderView import order
from DJangoHotel.viewspackage.roomInfoView import roomInfo
from django.conf import settings
from django.conf.urls.static import static
#####

urlpatterns = patterns('',
    ('^$', views.home),
    url(r'^books/', views.books), 
    url(r'^loans/', views.loans),    
    url(r'^users/', views.users),        
    url(r'^admin/', admin.site.urls),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^display_meta/$', views.display_meta),
    url(r'^search/$', views.search),
    url(r'^newBooks/$', views.newBooks),
    url(r'^editBooks/$', views.editBooks),
    url(r'^returnbooks/$', views.returnbooks),
    url(r'^newUserResult/$', views.newUserResult),
    url(r'^loanlist/$', views.loanlist),
    
#####
    ##url(r'^$', index),
    url(r'^order/',order),
    url(r'^loanresult/',loanResult),
    url(r'^newBookResult/',newBookResult),
    url(r'^editBookResult/',editBookResult),
    url(r'^deleBooks/',views.deleBooks),
    url(r'^deleUsers/',views.deleUsers),
    
)
