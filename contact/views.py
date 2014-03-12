from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            return redirect('/thanks/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'contact/contact.html', {
        'form': form,
    })


def thanks(request):
    return render(request, 'contact/thanks.html')