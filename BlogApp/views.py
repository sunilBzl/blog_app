from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from datetime import timezone
from .forms import CommentForm


from . models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-id')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'single_blog_post_detail'

    