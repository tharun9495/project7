from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to app1</h1>")
def sample(request):
    return render(request,"app1/sample_app1.html")