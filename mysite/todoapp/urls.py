from django.urls import path, re_path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.todoapp, name='todoapp'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]