from django.shortcuts import render

# Create your views here.

def authorshow(request):
    return render(request,"author/index.html")