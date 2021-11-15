from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'single_blog_post_detail'