from django.urls import path

from . import views

app_name = 'myinfo'
urlpatterns = [
    path('', views.main_screen, name='main_screen'),
    path('about/', views.about_me, name='about_me'),
    path('my_jobs/', views.my_jobs, name='my_jobs'),
    path('contacts/', views.my_contacts, name='my_contacts'),

]