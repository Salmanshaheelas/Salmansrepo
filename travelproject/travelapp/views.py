from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import people


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=people.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1})
