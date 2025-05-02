from django.shortcuts import render
from .forms import UserRegisterForm,UserLoginForm,UserProfile,UserPassChange,UserBlogForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .models import UserBlog,PublicBlog
# Create your views here.


def RegisterPage(request):
    if request.method == "POST":
        fd = UserRegisterForm(request.POST)
        if fd.is_valid():
            fd.save()
            messages.success(request,"Register Successfully Completed !!!")
    else:
        fd = UserRegisterForm()
    return render(request,"app/register.html",{"form":fd})


def LoginPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fd = UserLoginForm(data=request.POST)
            if fd.is_valid():
                valid_username= fd.cleaned_data["username"]
                valid_password = fd.cleaned_data["password"]
                login_data = authenticate(username=valid_username,password=valid_password)
                if login_data is not None:
                    login(request,login_data)
                    messages.success(request,"login Successfull !!")
                    return HttpResponseRedirect("/profile/")
            else:
                messages.success(request,"Please Enter a correct username and password")
        fd = UserLoginForm()
        return render(request,"app/login.html",{"form":fd})
    else:
        messages.success(request,"You are already logged in User..")
        return HttpResponseRedirect("/profile/")

@login_required(login_url="/login/")
def ProfilePage(request):
    if request.method == "POST":
        fd = UserProfile(data=request.POST,instance=request.user)
        if fd.is_valid():
            fd.save()
            messages.success(request,"your profile successfully Updated")
    else:
        fd = UserProfile(instance=request.user)
    return render(request,"app/profile.html",{"form":fd})


def LogoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully !!")
        return HttpResponseRedirect("/login/")
    else:
        return HttpResponseRedirect("/login/")

@login_required(login_url="/login/")
def PasswordPage(request):
    if request.method == "POST":
        fd = UserPassChange(request.user,request.POST)
        if fd.is_valid():
            fd.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,"Your Password has been successfully Change")
            return HttpResponseRedirect("/profile/")
        else: 
            messages.success(request,"kindly enter a correct password")
    else:
        fd = UserPassChange(request.user)
    return render(request,"app/password.html",{"form":fd})

@login_required(login_url="/login/")
def UserBlogPage(request):
    if request.method == "POST":
        fd = UserBlogForm(request.POST, request.FILES)
        if fd.is_valid():
            valid_user = request.user
            valid_blog_title = fd.cleaned_data["blog_title"]
            valid_blog_description = fd.cleaned_data["blog_description"]
            valid_blog_photo = fd.cleaned_data["blog_photo"]
            print(f"user= {valid_user}, title={valid_blog_title}, description={valid_blog_description}, photo={valid_blog_photo} ")
            UserBlog(blog_title=valid_blog_title,blog_description=valid_blog_description,blog_photo=valid_blog_photo,blog_user=valid_user).save()
            messages.success(request,"Your Blog has been added Successfully !!!")
    else:
        fd = UserBlogForm()
    return render(request,"app/userblog.html",{"form":fd})

@login_required(login_url="/login/")
def DashboardPage(request):
    if request.user.is_superuser:
        md = UserBlog.objects.all()
        md2= PublicBlog.objects.all()     
    else:
        md = UserBlog.objects.filter(blog_user=request.user)
        md2 = PublicBlog.objects.filter(user=request.user)
    return render(request,"app/dashboard.html",{"data1":md,"data2":md2})

@login_required(login_url="/login/")
def Approval(request,id):
    data = UserBlog.objects.get(pk=id)
    public_data = PublicBlog(title=data.blog_title,description=data.blog_description,photo=data.blog_photo,user=data.blog_user).save()
    data.delete()
    messages.success(request,"Approval Successfull !!")
    return HttpResponseRedirect("/dashboard/")

def HomePage(request):
    data = PublicBlog.objects.all()
    return render(request,"app/home.html",{"data":data})

# for public data item details
def ItemDetails(request,id):
    md = PublicBlog.objects.get(pk=id)
    current_user = str(request.user)
    model_user = str(md.user)
    # print(request.user)
    # print(md.user)
    return render(request,"app/itemdetails.html",{"data":md,"current_user":current_user,"model_user":model_user})

# for Userblog data item details
def UserBlogItemDetails(request,id):
    md = UserBlog.objects.get(pk=id)
    current_user = str(request.user)
    model_user = str(md.blog_user)
    # print(request.user)
    # print(md.blog_user)
    return render(request,"app/blogitemdetails.html",{"data":md,"current_user":current_user,"model_user":model_user})

def DeletePublicBlog(request,id=None):
    if id is not None:
        md = PublicBlog.objects.get(pk=id)
        md.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
    
