from django.shortcuts import render


def index(request):
    data = {
        'title': 'Notes | Main page'
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Notes | About page'
    }
    return render(request, 'main/about.html', data)
