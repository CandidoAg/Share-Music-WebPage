"""webPage URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from shareMusic import views as p_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('social_django.urls')),
    path('', include('django.contrib.auth.urls')),

    path('', p_views.login, name="login"),
    path('index', p_views.home, name='home'),
    path('Playlist', p_views.playlist, name='playlist'),
    path('Descubrimiento', p_views.descubrimiento, name='descubrimiento'),
    path('Descubrimiento/category/<categoryId>', p_views.categoryDetails, name='categoryDetails'),
    path('Descubrimiento/playList/<playListId>', p_views.songByCategoryPlayList, name='songByCategoryPlayList'),
    path('Perfil', p_views.perfil, name='perfil'),
]