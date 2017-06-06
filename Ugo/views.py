#from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone

# Create your views here.
def hello_world(request):
      return render(request,"hello_World.html",{
      'current_time': str(timezone.localtime(timezone.now())),})

def hello_world2(request):
      return HttpResponse("Hello World!")