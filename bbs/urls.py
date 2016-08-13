"""My_BBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/(?P<bbs_id>\d)$', views.bbs_detail),
    url(r'^blog/api/$', views.bbs_all),
    url(r'^blog/api/(?P<pk>\d)$', views.bbs_detail_rest),
    url(r'^user/api/$', views.BbsUserView.as_view()),
    url(r'^user/api/(?P<id>\d)$', views.BbsUserDetailView.as_view()),

]
