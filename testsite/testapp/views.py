from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'landing.html')

def course(request):
	return render(request,'course2.html')

def content_fetch(request):
	return render(request,'content.html')

def chapter2(request):
    return render(request,'chapter2.html')	

def simulation1(request):
	return render(request,'simulation_load_balancing.html')

def simulation2(request):
    return render(request,'simulation_distributed_caching.html')	


	