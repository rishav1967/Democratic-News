from django.contrib import admin
from django.urls import path
from .views import (post_list,post_detail,post_mod,post_like,center,left_wing,right_wing,propaganda_section
,fake_news_section,scraped_post,comment_delete,reply_delete)
from django.conf import settings
from .views import post_create_view,post_update_view,post_delete_view,post_comment,reply

app_name='posts'

urlpatterns = [
    path('',post_list,name='post_list'),
    path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
    path('post-like#-148@-hello/like/',post_like,name='post_like'),
    path('post-section#-5543@/centre/',center,name='center_section'),
    path('post-section#-5543@/left/',left_wing,name='left_section'),
    path('post-section#-5543@/right/',right_wing,name='right_section'),
    path('post-section#-5543@/propaganda/',propaganda_section,name='propaganda_section'),
    path('post-section#-5543@/fake_news/',fake_news_section,name='fake_news_section'),
    path('create/',post_create_view.as_view(),name='post_create'),
    path('<int:pk>/<slug:slug>/update/',post_update_view.as_view(),name='post_update'),
    path('<int:pk>/<slug:slug>/delete/',post_delete_view.as_view(),name='post_delete'),
    path('scraped/',scraped_post,name='scraped_post'),
    path('<int:id>/comment/',post_comment,name='post_comment'),
    path('<int:id>/reply/',reply,name='comment_reply'),
    path('<int:id>/comment-delete/',comment_delete,name='comment_delete'),
    path('<int:id>/reply-delete/',reply_delete,name='reply_delete'),



]