
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def top_sellers(reguest):
    return render(reguest, 'top-sellers.html')
# Create your views here.
