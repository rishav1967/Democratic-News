"""news_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from users.views import paste
from django.conf.urls.static import static
from django.conf import settings
from posts.views import category_view,movie_category,music_category,covid_category,global_category,sports_category
from users.views import user_login,user_registration,user_logout




urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',user_registration,name='register'),
    path('',include('posts.urls'),name='posts'),
    path('',include('users.urls'),name='users'),
    path('category/',category_view,name='category'),
    path('category/movie',movie_category,name='movie'),
    path('category/music',music_category,name='music'),
    path('category/sports',sports_category,name='sports'),
    path('category/covid',covid_category,name='covid'),
    path('category/global',global_category,name='global'),
    #path('like/',post_like,name='post_like'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

