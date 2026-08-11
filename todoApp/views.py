from django.shortcuts import redirect

def index(request):
    return redirect('/todos')

def add(a, b):
    return a + b
