from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UsernameField,UserChangeForm
from .models import UserBlog

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control reg-form-control",}),label="Enter Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control reg-form-control"}),label="Re-Enter Password")
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control reg-form-control","autofocus":""}),
            "first_name":forms.TextInput(attrs={"class":"form-control reg-form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control reg-form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control reg-form-control"}),
        }
class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class":"form-control reg-form-control","autofocus":""}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control reg-form-control"}))
    
class UserProfile(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","last_login","date_joined"]
        widgets = {
            "username": forms.TextInput(attrs={"readonly":"","class":"form-control"}),
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "last_login": forms.DateTimeInput(attrs={"readonly":"","class":"form-control"}),
            "date_joined": forms.DateTimeInput(attrs={"readonly":"","class":"form-control"}),
        }
        
class UserPassChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control reg-form-control"}),label="Enter Your Old Password:")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control reg-form-control"}),label="Enter New Password:")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control reg-form-control"}),label="Confirm New Password:")

class UserBlogForm(forms.ModelForm):
    class Meta:
        model = UserBlog
        fields = ["blog_title","blog_description","blog_photo"]
        widgets = {
            "blog_title":forms.TextInput(attrs={"class":"form-control"}),
            "blog_description":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "blog_photo":forms.FileInput(attrs={"class":"form-control","accept":None})
        }