from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name="home"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('signup/', views.RegisterUser.as_view(), name="signup"),
    path('myposts/', views.MyPosts.as_view(), name="myPosts"),
    path('newpost/', views.NewPost.as_view(), name="newPost"),
    path('profile/', views.ProfileUser.as_view(), name="profile"),
]