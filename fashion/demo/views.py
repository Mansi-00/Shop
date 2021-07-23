from django.shortcuts import render, redirect
from .forms import ContactForm
from fashion import settings
from django.core.mail import send_mail
from django.contrib import messages
# from .forms import UserForm, ProfileForm
# from django.contrib.auth.decorators import login_required

# Create your views here.


def demo(request):
    return render(request, 'index.html')


def demo2(request):
    return render(request, 'common.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            # print(contact_name)
            form.save()
            subject = 'Hello ' + contact_name + ' from apparel!'
            message = 'Stay Connected. We would love to hear you!'
            email_from = settings.EMAIL_HOST_1USER
            email_to = [contact_email, ]
            send_mail(subject, message, email_from, email_to)
            messages.success(request, 'Form submitted successfully.')
            return redirect('demo:Demo')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    template = 'form/contact.html'
    return render(request, template, {'demo': form})


