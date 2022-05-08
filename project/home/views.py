from django.shortcuts import render,HttpResponse
import json

# Create your views here.
def index(request):
    # data = spiketime.TimeSlot()
   
    return render (request,'index.html')
   #return HttpResponse("This is home page")
def market(request):
    f = open('pyint//stock_pre_output.json')
    data = json.load(f)
    # Iterating through the json
    # # list
    # for i in data['A']:
    #     print(i)
    # print(data)
    # print (data['A']['spike_time'])
    return render (request,'market.html',{'market':data})

def news(request):
    return render (request,'news.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        f = open('pyint//stock_pre_output.json')
        data = json.load(f)
        return render (request,'search.html',{'searched':searched,'searched_data':data})
    else:
        return render (request, 'search.html')
