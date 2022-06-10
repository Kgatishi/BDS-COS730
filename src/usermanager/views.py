from multiprocessing import context
from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User, Account
from .forms import UserForm, AccountForm

login_ = False

def index(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        userform = UserForm()
        accountform = AccountForm()
    print("-----------------------------")
    print(login_)
    print("------------------------------")
    context = {
        'userinfo': userform,
        'useraccount': accountform,
        'session': login_,
        'username': 'Tlou'
    }

    template = loader.get_template('landing.html')
    return HttpResponse(template.render( context, request ))

def login(request):
    login_ = True
    print("-------login(request)--------------")
    print(login_)
    print("------------------------------")
    return HttpResponseRedirect(reverse('index'))

def logout(request):
    login_ = False
    return HttpResponseRedirect(reverse('index'))

def register(request):
    login_ = False
    return HttpResponseRedirect(reverse('index'))


def bookings(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def scm(request):
    template = loader.get_template('scm.html')
    return HttpResponse(template.render())

def crm(request):
    template = loader.get_template('crm.html')
    return HttpResponse(template.render())