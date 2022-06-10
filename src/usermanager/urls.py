from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.index, name='index'),
    path('home', views.index, name='index'),
    path('signin', views.login, name='login'),
    path('signout', views.logout, name='logout'),
    path('signup', views.register, name='register'),
    path('scm', views.scm, name='scm'),
    path('crm', views.crm, name='crm'),
]