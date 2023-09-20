from django.shortcuts import render

# Create your views here.
 
def mainshow(request):
    return render(request,"main/index.html")