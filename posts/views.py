from django.shortcuts import render,get_object_or_404,redirect
from django.db import models
from django.forms import ModelForm
import random
from .models import Post,Category,Comments,Reply
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView,TemplateView
from users.models import MyUser
from .models import ViewedList
from bs4 import BeautifulSoup
from requests import get
from django.core.exceptions import ObjectDoesNotExist,FieldDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.urls import reverse



#from .forms import PostModelForm


""" url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
url2 = 'https://www.indiatv.in/india'
#response = get(url)
response = get(url2)
html_soup = BeautifulSoup(response.text, 'html.parser')
#movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
news_container = html_soup.find_all('li', class_ = 'p_news')

#print(type(movie_containers))
#print(len(movie_containers))
first_movie = movie_containers[0]
name=[]
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
print(first_year.text)

for movies in movie_containers:
    b= movies.find('div', class_ = 'lister-item-content')
    n=b.h3.a.text
    name.append(n)

print(name)
#print(first_movie.h3.a)
first_news=news_container[0]

b=first_news.find('div', class_ = 'content')
print(b.h3.text)
 """



def category_view(request):
    return render(request,'category.html',{})


def movie_category(request):
    category = Category.objects.get(name='Movie')
    pk = category.pk
    post = Post.objects.filter(category=pk).all()

    return render(request,'post_list.html',{'post':post})


def music_category(request):
    category = Category.objects.get(name='Music')
    pk = category.pk
    post = Post.objects.filter(category=pk).all()
    #post = Post.objects.all()
    return render(request,'post_list.html',{'post':post})


def global_category(request):
    category = Category.objects.get(name='Global')
    pk = category.pk
    post = Post.objects.filter(category=pk).all()
    #post = Post.objects.all()
    return render(request,'post_list.html',{'post':post})

def sports_category(request):
    category = Category.objects.get(name='Sports')
    pk = category.pk
    post = Post.objects.filter(category=pk).all()
    #post = Post.objects.all()
    return render(request,'post_list.html',{'post':post})

def covid_category(request):
    category = Category.objects.get(name='Covid')
    pk = category.pk
    post = Post.objects.filter(category=pk).all()
    #post = Post.objects.all()
    return render(request,'post_list.html',{'post':post})




def scraped_post(request):
    url2 = 'https://www.thehindu.com/search/?q=covid&order=DESC&sort=publishdate'
    response = get(url2)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    news_container = html_soup.find_all('div', class_ = 'story-card story-card75x1-cont')
    first_news=news_container[0:12]
    """ url = first_news.a.get('href')
    url3 = str(url)
    response2 = get(url3)
    html_soup2 = BeautifulSoup(response2.text, 'html.parser')
    img=news_container_new = html_soup2.find('div', class_ = 'img-container picture').picture.source.get('srcset')
    t= first_news.find('a', class_ = 'story-card75x1-text').text
    Post.objects.create(title=t,url=url3,author=request.user,image=img,slug=slugify(t)) """
    for news in first_news:
        img2=None
        text = news.find('a', class_ = 'story-card75x1-text').text
        url = news.a.get('href')
        url3 = str(url)
        try:
            a = Post.objects.get(url=url3)
        except ObjectDoesNotExist:
            a=None
        if a==None:
            response2 = get(url3)
            html_soup2 = BeautifulSoup(response2.text, 'html.parser')
            try:
                img= html_soup2.find('div', class_ = 'img-container picture').picture.source.get('srcset')
            except Exception as e:
                img2 = 'static/images/the_hindu.png'
                img = None
            Post.objects.create(title=text,url=url3,author=request.user,category=Category.objects.get(name='Covid'),status='PUBLISHED',image=img,image2=img2,slug=slugify(text))
            

        else:
            pass

    return HttpResponseRedirect("http://127.0.0.1:8000/")
        






class post_create_view(CreateView):
        model = Post
        template='post_form.html'
        #form_class = PostModelForm
        fields = ["title","body","category",'image2',"status"]

        def form_valid(self, form):
            form.instance.author = self.request.user
            form.instance.slug = slugify(form.instance.title)
        
            return super().form_valid(form)


class post_update_view(UpdateView):
    model = Post
    template_name ='posts/post_update.html'
    #form_class = PostModelForm
    fields = ["title","body","category","status"]
    #def get_object(self):
     #   return Post.objects.get(pk=self.request.GET.get('pk'))

class post_delete_view(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('posts:post_list')


#@login_required
def post_like(request):
    post=get_object_or_404(Post,id=request.POST.get('id'))
    if request.user in post.like.all():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    print(post.body)
    
    if request.is_ajax():
        html = render_to_string('like_section.html',{'post':post},request=request)
        return JsonResponse({'form':html})

def center(request):
    #return render(request,'h.html',{})
    check = False
    post=get_object_or_404(Post,id=request.POST.get('id'))
    if request.user in post.center.all():
        post.center.remove(request.user)
    else:
        post.center.add(request.user)

    #return HttpResponseRedirect(post.get_absolute_url())
    if request.user in post.center.all():
        post.left.remove(request.user)
        post.right.remove(request.user)
        post.propaganda.remove(request.user)
        post.fake_news.remove(request.user)   
    
    if request.is_ajax():
        html = render_to_string('center_section.html',{'post':post,'check':check},request=request)
        return JsonResponse({'form':html})

        


def left_wing(request):
    #return render(request,'h.html',{})
    post=get_object_or_404(Post,id=request.POST.get('id'))
    if request.user in post.left.all():
        post.left.remove(request.user)
        print(post.title)
    else:
        post.left.add(request.user)
        print(post.body)

    if request.user in post.center.all():
        post.center.remove(request.user)
        post.right.remove(request.user)
        post.propaganda.remove(request.user)
        post.fake_news.remove(request.user)   
        print("Hello")    

    #return HttpResponseRedirect(post.get_absolute_url())
    if request.is_ajax():
        html = render_to_string('left_section.html',{'post':post},request=request)
        return JsonResponse({'form':html})


def right_wing(request):
    #return render(request,'h.html',{})
    post=get_object_or_404(Post,id=request.POST.get('id'))
    if request.user in post.right.all():
        post.right.remove(request.user)
    else:
        post.right.add(request.user)


    if request.user in post.center.all():
        post.left.remove(request.user)
        post.center.remove(request.user)
        post.propaganda.remove(request.user)
        post.fake_news.remove(request.user)   
        print("Hello")    

    #return HttpResponseRedirect(post.get_absolute_url())
    if request.is_ajax():
        html = render_to_string('right_section.html',{'post':post},request=request)
        return JsonResponse({'form':html})

    

def propaganda_section(request):
    #return render(request,'h.html',{})
    post=get_object_or_404(Post,id=request.POST.get('id'))
    if request.user in post.propaganda.all():
        post.propaganda.remove(request.user)
    else:
        post.propaganda.add(request.user)

    if request.user in post.center.all():
        post.left.remove(request.user)
        post.right.remove(request.user)
        post.center.remove(request.user)
        post.fake_news.remove(request.user)   
        print("Hello")    

    #return HttpResponseRedirect(post.get_absolute_url())
    if request.is_ajax():
        html = render_to_string('propaganda_section.html',{'post':post},request=request)
        return JsonResponse({'form':html})
    



def fake_news_section(request):
    #return render(request,'h.html',{})
    post=get_object_or_404(Post,id=request.POST.get('id'))
    if request.user in post.fake_news.all():
        post.fake_news.remove(request.user)
    else:
        post.fake_news.add(request.user)

    if request.user in post.center.all():
        post.left.remove(request.user)
        post.right.remove(request.user)
        post.propaganda.remove(request.user)
        #post.center.remove(request.user)   
        print(Post.objects.filter(center=request.user))    

    #return HttpResponseRedirect(post.get_absolute_url())
    if request.is_ajax():
        html = render_to_string('fake_news_section.html',{'post':post},request=request)
        return JsonResponse({'form':html})


def post_mod(request):
    obj = Post.object.filter()


def post_list(request):
    #post=Post.objects.filter(bookmark=request.user).all()
    #c=Bookmark.objects.filter(id=b.id).all()
    #post = Post.objects.filter(category=p,author=request.user).all()
    post = list(Post.objects.filter(status='PUBLISHED'))
    random.shuffle(post)
    return render(request,'post_list.html',{'post':post})

def post_detail(request,id,year,month,day,post):
    post=get_object_or_404(Post,id=id,slug=post,publish__year=year,publish__month=month,publish__day=day)
    try:
        comments = Comments.objects.filter(post=post).all()
        reply = Reply.objects.filter(post=post).all()
    except ObjectDoesNotExist:
            comments = None  
            reply= None    

    if request.user in MyUser.objects.all():
        try:
            viewed=ViewedList.objects.get(user=request.user,post=post)
        except ObjectDoesNotExist:
            viewed = None

        if viewed == None:
            ViewedList.objects.create(user=request.user,post=post)
        else:
            viewed = ViewedList.objects.get(user=request.user,post=post)
            viewed.delete()
            ViewedList.objects.create(user=request.user,post=post)
            

    #below code is to query all viewed articles by a user
    #a=request.user.viewedlist_set.all()
    #for i in a:
     #   print(i.post.title)

    return render(request, 'post_detail.html',{'post':post,'comments':comments,'reply':reply})



def post_comment(request,id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        Comments.objects.create(author=request.user,body=request.POST['comment'],post=post)
        return HttpResponseRedirect(post.get_absolute_url())

    else:
        post = Post.objects.get(id=id)
        return HttpResponseRedirect(post.get_absolute_url())


def reply(request,id):
    if request.method == "POST":
        comment = Comments.objects.get(id=id)
        post = Post.objects.get(id=comment.post.id)
        Reply.objects.create(author=request.user,body=request.POST['reply'],comment=comment,post=post)
        return HttpResponseRedirect(post.get_absolute_url())

    else:
        comment = Comments.objects.get(id=id)
        post = Post.objects.get(id=comment.post.id)
        return HttpResponseRedirect(post.get_absolute_url())

def comment_delete(requst,id):
    comment=Comments.objects.get(id=id)
    comment.delete()
    post = Post.objects.get(id=comment.post.id)
    return HttpResponseRedirect(post.get_absolute_url())


def reply_delete(requst,id):
    reply=Reply.objects.get(id=id)
    reply.delete()
    post = Post.objects.get(id=reply.post.id)
    return HttpResponseRedirect(post.get_absolute_url())
    
    


    
    






    
    
