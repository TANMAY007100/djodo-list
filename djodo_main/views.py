from django.shortcuts import render
from .forms import TodoItemForm, SignInForm
from django.contrib.auth.views import LoginView

from .models import TodoItem

from django.urls import reverse_lazy

def home(request):
    todo_items = []
    if request.method == "GET":
        todo_form = TodoItemForm()
        if request.user:
            todo_items = TodoItem.objects.filter(user=request.user).values("id", "content")
        return render(request, 'index.html', {"todo_form": todo_form, "items": todo_items})
    elif request.method == "POST":
        todo_form = TodoItemForm(request.POST)
        if todo_form.is_valid():
            if request.user:
                TodoItem.objects.create(content=todo_form.cleaned_data["todo"], user=request.user)
                todo_items = TodoItem.objects.filter(user=request.user).values("id", "content")
            else:
                todo_items.append(todo_form.cleaned_data["todo"])
            return render(request, 'index.html', {"todo_form": todo_form, "items": todo_items})
        else:
            return render(request, 'index.html', {"todo_form": todo_form, "items": todo_items})


class SignInView(LoginView):

    template_name = 'accounts/login.html'
    form_class = SignInForm
