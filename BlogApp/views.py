from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import CommentForm

from . models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class SportListView(ListView):
    template_name = 'sports.html'
    context_object_name = "sports_posts"

    def get_queryset(self):
        return Post.objects.filter(category__title = 'Sports').order_by('-pub_date')


class NewsListView(ListView):
    template_name = 'news.html'
    context_object_name = "news_posts"

    def get_queryset(self):
        return Post.objects.filter(category__title = 'News').order_by('-pub_date')


class MusicListView(ListView):
    template_name = 'music.html'
    context_object_name = "music_posts"

    def get_queryset(self):
        return Post.objects.filter(category__title = 'Music').order_by('-pub_date')


def aboutus(request):
    return render(request, 'aboutus.html')




def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'comments': post.comments.all(),
        'post': post,
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('BlogApp:post_detail', slug=post.slug)
    else:
        form = CommentForm()
        context.update({
            'form':form
        })

        return render(request, 'post_detail.html', context)
    