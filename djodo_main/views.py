from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoItem, SignInForm
from django.contrib.auth.views import LoginView

def home(request):
    todo_item = []
    if request.method == "GET":
        todo_form = TodoItem()
        return render(request, 'index.html', {"todo_form": todo_form, "items": todo_item})
    elif request.method == "POST":
        todo_form = TodoItem(request.POST)
        if todo_form.is_valid():
            todo_item.append(todo_form.cleaned_data["todo"])
            return render(request, 'index.html', {"todo_form": todo_form, "items": todo_item})
        else:
            return render(request, 'index.html', {"todo_form": todo_form, "items": todo_item})


class SignInView(LoginView):

    template_name = 'accounts/login.html'
    form_class = SignInForm
