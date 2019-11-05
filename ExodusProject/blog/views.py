from django.shortcuts import render
from django.htttp import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<h1>Blog Home</h1>')