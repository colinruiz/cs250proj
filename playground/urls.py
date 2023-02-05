from django.urls import path
from . import views

#URL configurtion module
urlpatterns = [
    path('hello/', views.say_hello, name ='hello')
]