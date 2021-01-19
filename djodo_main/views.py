from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
