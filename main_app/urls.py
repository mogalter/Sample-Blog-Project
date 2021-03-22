from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name='blog-home'),
    path("about/", views.about, name='blog-about'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name='post-detail'),
    path("post/new/", views.PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),
    path("post/<str:username>/", views.UserPostListView.as_view(), name='user-posts')
    # re_path("^.*", views.bad_page, name='404-page')
]