from django.shortcuts import render

# Create your views here.
def hola(request):
    context = {
        "hola": "Hola desde Kubernetes!"
    }
    return render(request, 'hola.html', context)
