from django.shortcuts import render

def index(request):
    return render(request, 'mainapp\index.html')

def about(request):
    return render(request, 'about\index.html')