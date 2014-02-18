from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Post, PostFilter


def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})


def post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render_to_response('blog/index_filter.html', {'filter': f})