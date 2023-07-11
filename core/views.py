from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'curso': 'Programação ',
        'outro': 'Django'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')