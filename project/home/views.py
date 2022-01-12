from django.shortcuts import render,HttpResponse
from pyint import spiketime
from pyint.config import config_spiketime

# Create your views here.
def index(request):
    data = spiketime.TimeSlot()
    return render (request,'index.html',{'data':data})
   #return HttpResponse("This is home page")
def market(request):
    return render (request,'market.html')
def news(request):
    return render (request,'news.html')