from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def welcome(request):
    return HttpResponse('<h1>Welcome Master</h1>')

def hello(request):
    band = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': band})


