"""wt_site2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from blogs import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^blogs', views.blog_index),
    url(r'^index.html', views.default_index),
    url(r'^$', views.default_index),
    url(r'^charts.html', views.charts_index),
    url(r'^tables.html', views.tables_index),
    url(r'blank.html', views.blank),
    url(r'cards.html', views.cards),
    url(r'forgot-password.html',views.forgot_password),
    url(r'login.html', views.login),
    url(r'navbar.html', views.navbar),
    url(r'register.html', views.register),

]
