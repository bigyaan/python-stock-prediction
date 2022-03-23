#!/usr/bin/env python
# coding: utf-8

# In[1]:



import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

USER_INPUT_start_date = '2020-10-05'
USER_INPUT_end_date = '2021-12-12'


    


tickers_list=[]
closing_prices_list=[] 
stock_info=[]
stock_price = []

#sym=[]

#def get_target_price():
    #global USER_INPUT_target_price
    #USER_INPUT_target_price=float(input("Enter the price target in percent : "))
    
def carry_momentum():
    
    csv_dataframe = pd.read_csv(
        'list.csv', names=['symbols'])
    tickers_list = csv_dataframe.symbols.tolist()
    

    
    # per_high_cal():
    #high_percent=0
    print('\nRetrieving data for top n stocks...')
    print('\ncalculating present data and momentum chance......')
    data=yf.download(tickers_list,period='2d')
    
    for symbol in tickers_list:
        
        # Create a list of closing prices for each symbol
        if data.empty== False:
            closing_prices_list = data['Close'][symbol].tolist()
            for index in range(1, len(closing_prices_list)):
                previous_price = closing_prices_list[index-1]
                current_price = closing_prices_list[index]
                if(current_price>previous_price):
                    high=((current_price-previous_price)/current_price)*100
                    
                   #sym.append(high)
                   #for ind in range(high):
                   #for i in range(high_percent):
                    if(high>2):
                        stock_info.append(symbol)
                        stock_price.append(high)
   # print_data():
    # Store information in a dataframe and export a CSV
    dict={"symbol":stock_info,
           "high":stock_price}
    final = pd.DataFrame(dict)
    
    #rearrange data in ascending order
    final.sort_values("high",axis=0,ascending=True, inplace=True,)
    final.set_index("symbol",inplace=True)
    final.reset_index(inplace=True)
    final.to_csv('%high.csv',index=False)
     
    return final


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




