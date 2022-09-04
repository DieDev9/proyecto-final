from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Mi primer CRUD en Django</h1>")

def index(request):
    return render(request,'pages/index.html')
