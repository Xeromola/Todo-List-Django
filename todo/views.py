import todo
from django.shortcuts import redirect, render
from todo.models import todo_item

# Create your views here.
def home(request):
    if request.method == "POST":
        inp = request.POST['todoitem']
        new = todo_item(title=inp, status="Pending")
        new.save()
        return redirect('/')
    items = todo_item.objects.all()
    return render(request, 'index.html', {'items' : items})

def del_item(request, pk):
    todo_item.objects.get(id=pk).delete()
    return redirect('/')

def edit_item(request, pk):
    if request.method == "POST":
        it = todo_item.objects.get(id=pk)
        it.title = request.POST['todoitem']
        it.save()
    return redirect('/')