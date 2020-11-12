from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def todoapp(request):
    category_list = Todo.objects.all().values_list('category', flat=True).distinct()
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'todoapp/index.html', {"todo_items": todo_items, "category_list": category_list })




def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    title = request.POST['title']
    category = request.POST['category']
    Todo.objects.create(added_date=current_date, text=content, title=title, category=category)
    return HttpResponseRedirect('/todoapp')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todoapp')
