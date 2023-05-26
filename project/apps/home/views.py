from django.shortcuts import render, redirect
from . import forms

def index(request):
    return render(request, 'home/index.html')

def crear_autor(request):
    if request.method == 'POST':
        form = forms.AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.AutorForm()
        context = {"form": form}
        return render(request, 'home/crear_autor.html', context)

def crear_post(request):
    return render(request, 'home/crear_post.html')