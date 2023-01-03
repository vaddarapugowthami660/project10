from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function(request):
    return render(request,'file1.html')