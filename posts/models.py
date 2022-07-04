from django.db import models
from users.models import MyUser
from django.utils import timezone
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse




# Create your models here.




class PostQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(status="PUBLISHED")

class PublishedManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return PostQuerySet(self.model,using=self._db)
    def active(self,*args,**kwargs):
        return self.get_queryset().published()


#class PublishedManager(models.Manager):
#    def get_queryset(self):
#        return super(PublishedManager,self).filter(status="published")
    

class Category(models.Model):
    
    name = models.CharField(verbose_name = "Category",max_length=500)
    def __str__(self):
        return self.name



class Post(models.Model):
    STATUS_CHOICES = [
    ('DRAFT', 'Draft'),
    ('PUBLISHED', 'Published'),
    ]
    title = models.CharField(max_length=500)
    body = models.TextField(null=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE,verbose_name = "Category",default='')
    #path = models.CharField(max_length=60,null=True,blank=True)
    url = models.URLField(unique=True,null=True,blank=True,max_length=500)
    datetime = models.DateTimeField(auto_now=True, blank=False,) #todo: auto_now=True
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,verbose_name='Author', on_delete=models.CASCADE,default=None) 
    image=models.ImageField(null=True,blank=True,max_length=500)
    image2=models.ImageField(null=True,blank=True,max_length=500)
    like= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="post_likes")
    center= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="center")
    left=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="left_wing")
    right=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="right_wing")
    propaganda=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="propagana")
    fake_news=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="fake_news")
    slug=models.SlugField(max_length=500,blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    bookmark=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='bookmark')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('posts:post_detail',args=[self.id,self.publish.year,self.publish.month,self.publish.day, self.slug])

def pre_save_post(sender,instance,*args,**kwargs):
        slug=slugify(instance.title)
        instance.slug = slug

pre_save.connect(pre_save_post,sender=Post)


#pre_save.connect(slug_creater,sender=Post)

class ViewedList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    post= models.ForeignKey(Post, on_delete=models.CASCADE,default=None)
    last_viewed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


    class Meta:
        ordering = ('-last_viewed',)


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    body = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default=None)
    like= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="comment_likes")
    dislike= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="comment_dislikes")


    def __str__(self):
        return self.post.title


class Reply(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    body = models.TextField(max_length=500)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE,default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default=None)
    like= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="reply_likes")
    dislike= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name="reply_dislikes")
