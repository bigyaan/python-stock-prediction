#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import the necessary packages:


import datetime as dt
from datetime import datetime,date,time
import yfinance as yf
import warnings
import pandas as pd

def day_spiketime(tin,High_table):
    #gives the max value for three time slot for a given day 
    tlist=tin.values.tolist()
    
    templist=[]
    high=[]
    for (x,val) in enumerate(tlist):
        templist.append(val[3])
        
        if(x!=0 and (x%30)==0):
            High_in_time=max(templist)
            high.append(High_in_time)
            
            templist=[]
    
    if len(high)==12:
        High_table.loc[len(High_table)]=high
    
    # High_table.loc[len(High_table)]=high
    
    

    return(High_table)


def TimeSlot():
    spike_dict={}
    top_n_stocks = pd.read_csv(
        'list.csv', names=['symbols'])
    top_n_stocks = pd.DataFrame(top_n_stocks )
    if top_n_stocks.index.size:
        #config_global.top_n_stocks_dup = config_global.top_n_stocks.copy(deep = True)
        iterlist=top_n_stocks['symbols'].to_list()
     
        for symbol in iterlist:
            sym=yf.Ticker(symbol)
            sym_info=sym.history(period='7d',interval="1m")
            #print(sym_info)
            sym_info["Date"]=sym_info.index
            
            #initialize the necessary list and columns names
            new_cols=["9:30-10:00","10:00-10:30","10:30-11:00","11:00-11:30","11:30-12:00","12:00-12:30","12:30-13:00","13:00-13:30","13:30-14:00","14:00-14:30","14:30-15:30","15:00-15:30"]
            High_table_init=pd.DataFrame(columns=new_cols)
            
            #create a iteration list for each day in the last 7 days
            datestamp=sym_info["Date"].tolist()
            dayiter=[i.day for (x,i) in enumerate(datestamp) if datestamp[x].day!=datestamp[x-1].day]
            
            #loop through every day getting the maximum value for each time slot 
            
            for i in dayiter:
                criterion = sym_info['Date'].map(lambda x: x.day==i)
                tin=sym_info[criterion]
                
                
                  
                High_table=day_spiketime(tin,High_table_init)
            
            
            #find the average for each slot find the time slot with highest average over last 7 days
            avg_spike_time=High_table.mean(axis=0)
            # print("\n",avg_spike_time)
            if avg_spike_time.dtype =="float64":
                req_slot=avg_spike_time.idxmax()
                spike_dict[symbol] = req_slot
        # print(spike_dict)
        return spike_dict


            





