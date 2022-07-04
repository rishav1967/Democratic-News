from django.contrib import admin
from .models import Post,Category,ViewedList

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(ViewedList)

#admin.site.register(Bookmark)
