from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse ("""<html><body bgcolor=cyan><h/><center>welcome to sudheerit </center></h1></body></html> """)
# Create your views here.
