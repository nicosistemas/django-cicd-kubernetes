from django.shortcuts import render

# Create your views here.
def hola(request):
    context = {
        "hola": "Hola desde Kubernetes pero deployado con github actions, una locura esto!"
    }
    return render(request, 'hola.html', context)
