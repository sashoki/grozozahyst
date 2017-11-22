# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from groza.models import Portfolio, Category
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponseRedirect
from django.dispatch import receiver
from django.core.signals import request_finished
from django.conf import settings
from forms import ContactForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def portfolios(request, portfolio_id=1):
    args = {}
    args['portfolios'] = Portfolio.objects.all()
    args['portfolio'] = Portfolio.objects.get(id=portfolio_id)
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.filter(id=portfolio_id)
    return render(request, 'portfolios.html', args)

def callback(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a name.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid email address.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if not errors:
            send_mail(
                request.POST['name'],
                request.POST['message'],
                request.POST['email'],
                ['ideauspeha@gmail.com', 'oleksandr.petrovskyi@radioservice.net.ua',],  # Майл на який буде відправлено лист!
            )
            return render(request, 'thanks.html')
    return render(request, 'portfolios.html', {
        'error': errors,
        'name': request.POST.get('name', ''),
        'email': request.POST.get('email', ''),
        'message': request.POST.get('message', ''),
    })

'''def callback(request):
    args = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Якщо форма заповнена коректно, зберегти всі введені користувачем значення
        if form.is_valid():
            name = form.cleaned_data['name']
            phon = form.cleaned_data['phon']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = settings.EMAIL_HOST_USER
            # Якщо користувач хоче отримати копію собі, додаємо його до списку отримувачів
            if copy:
                recepients.append(email)
            try:
                fullemail = phon + " " + email + " " + "<" + recepients + ">"
                send_mail(name, message, fullemail, ['ideauspeha@gmail.com'])
                return render(request, 'thanks.html')
            except BadHeaderError:  # Захист від вразливості
                return HttpResponse('Invalid header found')
            # Перехід на іншу сторінку, якщо повідомлення відправлено
            return render(request, 'portfolios.html')

        else:
            return render(request, 'portfolios.html')
    else:
        args['form'] = ContactForm()
        # Вивід форми в шаблон
    return render(request, 'portfolios.html', args)'''

'''def callback(request):
    name = request.POST.get('name', '')
    phon = request.POST.get('phon', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')
    if name and phon and email and message:
        try:
            fullemail = phon + " " + email
            send_mail(name, fullemail, message, ['ideauspeha@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('portfolios.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')'''
