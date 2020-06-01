from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h2>Sites Index Page</h2>')

