from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import CommentForm

from . models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'



# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     context_object_name = 'single_blog_post_detail'


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form})

    
    