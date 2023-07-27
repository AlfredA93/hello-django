"librarys"
from django.shortcuts import render, redirect
from .models import Item


# Create your views here.
def get_todo_list(request):
    "Call todo_list page"
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    "Call add_item page and add the item to the db"
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
