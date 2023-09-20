from django.shortcuts import render

# Create your views here.

def bookshow(request):
    return render(request,"book/index.html")