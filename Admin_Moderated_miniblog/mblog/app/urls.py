from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.HomePage,name="home"),
    path("register/",views.RegisterPage,name="register"),
    path("login/",views.LoginPage,name="login"),
    path("profile/",views.ProfilePage,name="profile"),
    path("logout/",views.LogoutPage,name="logout"),
    path("password/",views.PasswordPage,name="password"),
    path("userblog/",views.UserBlogPage,name="add_blog"),
    path("dashboard/",views.DashboardPage,name="dashboard"),
    path("approval/<int:id>/",views.Approval,name="approval"),
    path("itemdetials/<int:id>/",views.ItemDetails,name="itemdetails"),
    path("userblogitemdetails/<int:id>/",views.UserBlogItemDetails,name="userblogitem"),
    path("deletepublicblog/<int:id>/",views.DeletePublicBlog,name="deletepublicblog"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
