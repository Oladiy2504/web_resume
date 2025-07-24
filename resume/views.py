from django.shortcuts import render

def home(request):
    context = {
        'name': 'Maksim Kopnev',
        'position': 'Backend‑разработчик',
    }
    return render(request, 'resume/home.html', context)