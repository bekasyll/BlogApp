from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from blog.forms import LoginUserForm, RegisterUserForm, NewPostForm, ProfileUserForm
from blog.models import Posts


@login_required
def home(request: HttpRequest):
    context = {
        "posts": Posts.objects.all(),
        "title": "Home"
    }
    return render(request, 'blog/home.html', context)


def login_user(request: HttpRequest):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return redirect("home")
            else:
                return redirect("login")
    else:
        form = LoginUserForm()

    return render(request, "blog/login_user.html", {"title":"Log in", "form":form,})

@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("login")

def signup_user(request: HttpRequest):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password2"])
            user.save()
            print(user)
            return redirect("login")
    else:
        form = RegisterUserForm()

    return render(request, "blog/signup_user.html", {"title": "Sign up", "form": form})

@login_required
def my_posts(request: HttpRequest):
    posts = Posts.objects.filter(author=request.user)
    return render(request, "blog/my_posts.html", {"posts": posts})

@login_required
def new_post(request: HttpRequest):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
            except:
                form.add_error(None, "Error creating post!")
    else:
        form = NewPostForm()
    return render(request, "blog/new_post.html", {"title": "New Post", "form": form})


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