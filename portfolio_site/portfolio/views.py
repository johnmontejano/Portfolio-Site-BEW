from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {'message':'Welcome to the home page'}
    return render(request, 'portfolio/index.html', context=context)

def contact(request):
    context = {'message':'Contact Me'}
    return render(request,'portfolio/contact.html', context=context)
def greet_by_name(request, name):
    return render(request, 'portfolio/greeting.html', context={'name':name})