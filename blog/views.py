from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post, Category, ContactForm


def index(request):
    return render(request, 'blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()
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
        'posts': Post.objects.filter(category=category)
    })


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'blog/contact.html', {
        'form': form,
    })