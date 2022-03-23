#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf

import numpy as np
##import matplotlib.pyplot as plts
def main_mod():
    start_date_highest_range = '2020-12-12' 
    end_date_highest_range = '2021-01-01'
    el =[]
    symbol_list=[]
    average_list=[]
    th = pd.read_csv('list.csv' , names=['symbols'])
    it=th["symbols"].tolist()
   
    for sym in it:
        x_df = yf.download(tickers=sym,start=start_date_highest_range,end=end_date_highest_range,progress=False)
        #print(x_df)
        check=x_df.empty
        #print(check)
    
        if(check==False):
            high_list=x_df["High"].tolist()
            low_list=x_df["Low"].tolist()
            
            zip_file=zip(high_list,low_list)
            for list1,list2 in zip_file:
                ranges=abs(((list1-list2)/list2)*100)
                #print(ranges)
                el.append(ranges)
                
                #print(el)
            symbol_list.append(sym)
            #print(el)    
            average=sum(el)/len(el)
            average_list.append(average)
    #print(symbol_list)
        #print("The average for {} is {}".format(sym,average))
    df_for_higest_range = pd.DataFrame(columns =['symbol','avg_per'])
    df_for_higest_range["symbol"]=symbol_list
    df_for_higest_range["avg_per"]=average_list
    df_for_higest_range[df_for_higest_range["avg_per"]>3]                                               
    return df_for_higest_range


# In[2]:





# In[ ]:




