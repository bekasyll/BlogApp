from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordChangeView, PasswordChangeDoneView
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
    path('delete/<int:pk>/', views.DeletePost.as_view(), name="delete_post"),
    path('update/<int:pk>/', views.UpdatePost.as_view(), name="update_post"),
    path('password-change/', views.UserPasswordChange.as_view(), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name="blog/password_change_done.html"), name="password_change_done"),

    # path("password-reset/", PasswordResetView.as_view(template_name="blog/password_reset_form.html"))
]