from django.contrib import admin
from django.urls import path
from .views import user_profile_view
from django.conf import settings
from django.conf.urls.static import static

from .views import user_profile_view,status_check,viewed_history,user_posts


app_name='users'

urlpatterns = [
    path('<str:username>/<int:year>/<int:month>/<int:day>/',user_profile_view,name='profile_view'),
    path('status/',status_check,name='status_check'),
    path('viewed_history/',viewed_history,name='viewed_history'),
    path('user-post/',user_posts,name='user_posts'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
