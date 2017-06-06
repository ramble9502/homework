"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from one.views import *
from django.contrib.auth.views import login
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^accounts/login/$', login, {'template_name': 'login_index.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
    url(r'^accounts/profile/$',get_user_profile),
    url(r'^divelayout/',divelayout),
    url(r'^bartenderstory/',bartenderstory),
    url(r'^brewwine/',brewwine),
    url(r'^lmessage/$', create_lmessage),
    url(r'^divescore/$',record_dive_score),
    url(r'^lmessage_layout/',lmessage_layout),
    url(r'^questionask/',questionask),
    url(r'^deletecomment/(?P<id>\d+)/$', deletecomment),
    url(r'^testscore/$',record_test_score),
    url(r'^testscorelayout/',testscorelayout),
    url(r'^divescorelayout/',divescorelayout),

]  
