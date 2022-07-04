from django.shortcuts import redirect, render
#from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.views.generic import DetailView,ListView,TemplateView
from .models import MyUser,MyUserManager
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist
from posts.models import Post


# Create your views here.

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_registration(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        date_of_birth = request.POST['dob']
        try:
            useremail_check = MyUser.objects.get(email=email).email
        except ObjectDoesNotExist:
            useremail_check = None
        try:
            username_check = MyUser.objects.get(username=username).username
        except ObjectDoesNotExist:
            username_check = None
        if email == useremail_check:
            messages.error(request,('Email already Exists'))
            return HttpResponseRedirect('/register/')

        if username == username_check:
            messages.error(request,('Username already already Exists'))
            return HttpResponseRedirect('/register/')

        if username == username_check and email == useremail_check:
            messages.error(request,('Both Email and Username already already Exists'))
            return HttpResponseRedirect('')

        else:
            MyUser.objects.create_user(username,email,date_of_birth,password)
            user = authenticate(request,email=email,password=password)
            login(request,user)
            return HttpResponseRedirect('http://127.0.0.1:8000/')

    else:
        return render(request,'registration.html',{})






def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        else:
            return render(request,'login.html',{})

    else:
            return render(request,'login.html',{})


def paste(request):
    return render(request, 'h.html')


'''class user_profileview(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['user'] = MyUser.objects.get(username=request.user.username)
        return context'''

def user_profile_view(request,username,year,month,day):

    user = MyUser.objects.get(username=username)
    context={
        'user':user
    }
    return render(request,'profile.html',context)

def viewed_history(request):
    post=request.user.viewedlist_set.all()
    return render(request, 'post_list.html',{'post':post})

def status_check(request):
    form = request.POST.get('Status')

    if form =='Creator':
        MyUser.objects.filter(username=request.user.username).update(creator=True)
        print(MyUser.objects.filter(username=request.user.username))
    elif form == 'Viewer':
        MyUser.objects.filter(username=request.user.username).update(creator=False)
    return HttpResponseRedirect(request.user.get_absolute_url())


def user_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request,'user_posts.html',{'posts':posts})




    