from django.urls import path, re_path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.todoapp, name='todoapp'),
    path('add_todo/', views.add_todo),
    re_path(r'^delete_todo/(?P<todo_id>[0-9]{2})/$', views.delete_todo),
]