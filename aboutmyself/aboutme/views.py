from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.
def name(request):
	return render(request,'yesha.html')
	
def aboutme(request):
	return render(request,'resume.html')

