from django.shortcuts import render
from . models import Place
from . models import Photo
# Create your views here.
def travel(request):
    obj=Place.objects.all()
    ob = Photo.objects.all()
    return render(request,'index.html',{'result':obj,'res': ob})