from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response
#request handler
#action
#django its called a view

def say_hello(request):
    #pull data from database
    #Transform
    #Send email
    return render(request, 'hello.html', {'name': 'Mosh'})