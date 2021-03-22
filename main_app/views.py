from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
# Create your views here.


def bad_page(request):
    return render(request, 'main_app/404.html')


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': "Home",
    }
    return render(request, 'main_app/home.html', context=context)


class PostListView(ListView):
    model = Post
    # default template = <app>/<model>_<viewtype>.html
    template_name = 'main_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # determines how we chunk the page
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # default template = <app>/<model>_<viewtype>.html
    template_name = 'main_app/user_posts.html'
    context_object_name = 'posts'
    # if query set overridden, this will get overriden too
    # determines how we chunk the page
    paginate_by = 5

    # we can override the retrieval query to filter
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # default template = <app>/<model>_<viewtype>.html


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # this one actually shares a template with the update view!
    # <model>_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'main_app/about.html')
