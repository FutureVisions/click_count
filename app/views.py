from django.shortcuts import render, redirect
from .models import Button

def home(request):
    button = Button.objects.first()
    if not button:
        button = Button.objects.create()
    if request.method == 'POST':
        button.click_count += 1
        button.save()
        return redirect('/')
    return render(request, 'index.html', {'button': button})


# Create your views here.
