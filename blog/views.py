from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView

from blog.forms import LoginUserForm, RegisterUserForm, NewPostForm, ProfileUserForm
from blog.models import Posts


class BlogHome(LoginRequiredMixin, ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    extra_context = {"title": "Home"}

    def get_queryset(self):
        return Posts.objects.all()


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "blog/login_user.html"
    extra_context = {"title": "Log in"}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/signup_user.html'
    extra_context = {"title": "Sign up"}
    success_url = reverse_lazy("login")


class MyPosts(LoginRequiredMixin, ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    extra_context = {"title": "My Posts"}

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)


class NewPost(LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy("home")
    extra_context = {"title": "New post", "heading": "Make a new post"}

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'blog/profile.html'
    extra_context = {
        "title": "My Profile",
    }

    def get_success_url(self):
        return reverse_lazy('home')

    def get_object(self, queryset = None):
        return self.request.user