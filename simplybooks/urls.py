"""simplybooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from simplybooksapi.views.author import AuthorView
from simplybooksapi.views.books import BookView
from simplybooksapi.views.genre import GenreView
from simplybooksapi.views.book_genre import BookGenreView
from django.urls import path
from simplybooksapi.views.auth import register_user, check_user

#USE BUILT IN CLASS IN DJANO SO THE SERVER RESPONDS WITH APPRORIATE METHOD
#DFR SETS THE RESOURCE FOR EACH METHOD IN THE VIEW
#TRUE/FALSE TELLS ROUTER TO TO ACCEPT 'AUTHORS'/'BOOKS'/'GENRE'
#1ST PARAM SETS UP URL, 2ND TELLS SERVER WHICH URL, 3RD BASE NAME OR NICK NAME-SINGULAR VERSION OF URL
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'authors', AuthorView, 'author')
router.register(r'books', BookView, 'books')
router.register(r'genre', GenreView, 'genre')
router.register(r'bookGenres', BookGenreView, 'bookGenre')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
