from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# Post list view
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

# Post detail view
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})