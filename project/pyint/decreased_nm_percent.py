#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf
import pandas as pd
from datetime import datetime

def task_7_decreased_nm_per():
    calculated_change = []
    down_stock_sym = []
    down_stock_val = []
    stock_price_at_N = []
    time_N = []
    stock_price_at_M = []
    time_M = []
    closing_price_now = []
#start_code    
     # get the N-M vaule from the user in negative value
    
    # use below code for asking input for for now we consider -0.05
    #USER_INPUT_percent_price_down=float(input('Enter the percent price down in negative value : '))
    USER_INPUT_percent_price_down = -0.05
    
    csv_dataframe = pd.read_csv(
        'list.csv', names=['symbols'])
    tickers_list = csv_dataframe.symbols.tolist()
    
    for symbol in tickers_list:
        data2=pd.DataFrame()
        closing_prices_list = []
        date_time = []
        date_time_for = []
        date_for = []
           
         # Create a list of closing prices for each symbol
        data=yf.download(symbol,period='1d', interval='1m')
        if data.empty== False:
            closing_prices_list = data['Close'].tolist()
            date_time=list(data.index.tolist())
    
            #format the timestamp
            for itr in date_time:
                date_time_for.append(datetime.strftime(itr,"%m/%d/%Y, %H:%M:%S"))   
            #create dataframe for sorting date with respect to price
            dict={'Datetime':date_time_for,
                  'Close':closing_prices_list}

            data2=pd.DataFrame(dict)
            data2.sort_values(by='Close',ascending=False,inplace=True)
#operation            
            # Clear all variables before analyzing every stock symbol
            percent_price_down=0.0
            average=0.0
            N,M=0.0,0.0

            #sort dataframe with respect to closing price
            data2.sort_values(by='Close',ascending=False,inplace=True)
            date_for = data2['Datetime'].tolist()

            #sorting closing price in descending order
            order=sorted(closing_prices_list,reverse=True)
            down=[]         
            N,M=order[0],order[-1]

            #calculate percent change between M and N  
            change=((M-N)/M)*100
            calculated_change.append(change)

            # Process percent price down for current symmbol starting from last date

            for index in range(len(closing_prices_list),0,-1):
                #previous_price = closing_prices_list[index-2]
                current_price = closing_prices_list[index-1]
                percent_price_down=((current_price-N)/N)*100

                if (percent_price_down < USER_INPUT_percent_price_down):
                    down.append(percent_price_down)
            try:    
                average=sum(down)/len(down)       
            except ZeroDivisionError:
                print('----------')
            # Store all computed information in a dataframe        
            if (average < USER_INPUT_percent_price_down):        
                down_stock_sym.append(symbol)
                down_stock_val.append(average)    
                stock_price_at_N.append(N)
                time_N.append(date_for[0])
                stock_price_at_M.append(M)
                time_M.append(date_for[-1])
                closing_price_now.append(closing_prices_list[-1])

                

#print_data:
     # Store information in a dataframe and export a CSV
    dict={"stock":down_stock_sym,
          "price down":down_stock_val,
          "stock price at N":stock_price_at_N,
          "time N":time_N,
          "stock price at M":stock_price_at_M,
          "time M":time_M,
          "closing price now":closing_price_now}
    final = pd.DataFrame(dict)
    #rearrange data in ascending order
    final.sort_values("price down",axis=0,ascending=True, inplace=True,)
    final.set_index("stock",inplace=True)
    final.reset_index(inplace=True)
    final.to_csv('N-M_down_stocks.csv',index=False)
     

    
    try:
        calculated_change_average=sum(calculated_change)/len(calculated_change)
        print(f"the average percent diffenrence between N and M as seen in the meket is {calculated_change_average}")
    
    except ZeroDivisionError:
        print("zero division")
        
        
    return final    


# In[ ]:





# In[ ]:





# In[ ]:




