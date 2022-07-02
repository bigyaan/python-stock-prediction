from django.shortcuts import render,HttpResponse
import json
import plotly.express as px
import pandas as pd
import numpy as np
import plotly
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
import os
import plotly.graph_objects as go


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
        for k,v in data.items():
            if searched == k:
                data_1 = v.get('momentum_high')
                data_2 = v.get('time_M_nmper')
                data_3 = v.get('updown_percent')
                data_4 = v.get('time_N_nmper')
                fig_1 = px.line(
        
                    x = [data_2,data_4],
                    y = [data_1,data_3],
                    labels ={'x':'date','y':'data'}
                )
                fig = go.Figure(go.Scatter(
                     x = [data_2,data_4],
                    y = [data_1,data_3],
    
                ))
                

        context = fig.to_html()
       
                
                

        return render (request,'search.html',{'searched':searched,'searched_data':data,'context': context})
    else:
        return render (request, 'search.html')
