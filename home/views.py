from django.shortcuts import render


# Create your views here.
def fun(request):
    return render(request, 'index.html')


def gain(request):
    return render(request, 'gain.html')
