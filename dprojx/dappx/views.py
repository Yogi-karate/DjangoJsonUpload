from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
import json
from .forms import PostForm,PostCreateForm
def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})
def upload_posts_screen(request,flag=0):
    context = {'post_list':Post.objects.all().order_by('id')}
    return render(request,"dappx/uploaded_posts.html",context)

def upload_post(request,id=0):
        form = PostForm()
        print(request.FILES)
        if 'file' in request.FILES:
            x = request.FILES['file']
            m = str(x)
            print(m)
            n = m.split('.')
            if n[1] == 'json':
                post_data = json.load(x)
                for i in post_data:
                    if 'userId' not in i or 'id' not in i or 'title' not in i or 'body' not in i:
                            return render(request,"dappx/upload.html",{'form':form,'mes':True,'tex':"make sure json file has title,body,user_id and id fields"})
                    post = Post(user_id = i['userId'],title = i['title'],body = i['body'],id= i['id'])
                    j = post.save()
                print("--------------------------------------")
                print("=======XXXXXXXXXXX=========X===================")
                return render(request,"dappx/upload.html",{'form':form,'mes':False,'tex':"Data Uploaded Successfully"})
            return render(request,"dappx/upload.html",{'form':form,'mes':True,'tex':"Enter Only JSON File"})
        return render(request,"dappx/upload.html",{'form':form,'mes':False,'tex':''})