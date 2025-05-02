from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def initial(request):
    msg = "<h1> hello world! <h1>"
    return HttpResponse(msg)

def htmlt(request):
    return render(request,"new.html",{"name":"prakashraj" })