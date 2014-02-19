from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):
    # get the blog posts that are published
    # posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })



# def post_list(request):
#     f = PostFilter(request.GET, queryset=Post.objects.all())
#     return render_to_response('blog/index_filter.html', {'filter': f})