from django.shortcuts import render

def home(request):
    timeline = [
        {'year': '2018', 'title': 'Окончил университет', 'description': 'Бакалавр в Computer Science'},
        {'year': '2019–2022', 'title': 'Компания X', 'description': 'Backend-разработчик Python/Django'}
    ]
    skills = [
        {'name': 'Python', 'level': 'Advanced'},
        {'name': 'Django', 'level': 'Advanced'}
    ]
    projects = [
        {'title': 'MySite', 'description': 'Сайт-портфолио', 'tech': 'Django, Tailwind',
         'url': 'https://github.com/...'}
    ]
    bio_text = "lorem ipsum"
    context = {
        'name': 'Maksim Kopnev',
        'position': 'Backend‑разработчик',
        'timeline': timeline,
        'skills': skills,
        'projects': projects,
        'bio_text': bio_text
    }
    return render(request, 'resume/home.html', context)