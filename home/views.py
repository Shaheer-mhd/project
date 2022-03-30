from django.shortcuts import render, redirect

# Create your views here.
from home.models import Member, Feedback


def fun(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        name1 = request.POST.get('name1')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    Feedback.objects.create(NAMAM=name1, Email=email, Subject=subject, Message=message)
    return redirect('home:fun')


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    else:
        name = request.POST.get('name')
        place = request.POST.get('place')
        age = request.POST.get('age')
        ph = request.POST.get('ph')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
    Member.objects.create(Name=name, Place=place, Age=age, Ph=ph, Height=height, Weight=weight)
    return redirect('home:fun')
