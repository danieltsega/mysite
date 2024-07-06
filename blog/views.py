from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

# Post list view
def post_list(request):
    post_list = Post.published.all()
    # Add pagination to post list
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    return render(request, 'blog/post/list.html', {'posts': posts})

# Post detail view
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})