#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta







def task_9_up_down_trend():
    up_percent =[]
    down_percent = []
    up_trend_sym = []
    down_trend_sym = []
#load csb
    csv_dataframe = pd.read_csv(
        'list.csv', names=['symbols'])
    tickers_list = csv_dataframe.symbols.tolist()

# get date
    #get current date and day
    now = datetime.today()
    day=now.strftime("%A")
    print(day)
    USER_INPUT_end_date_today = now.strftime("%Y-%m-%d")
     # This is to ensure that a data is available for comparision.
    if(day=='Sunday'):
        USER_INPUT_end_date = str(datetime.strptime(
            USER_INPUT_end_date_today, '%Y-%m-%d').date() - timedelta(days=2))
    elif(day=='Saturday'):
        USER_INPUT_end_date = str(datetime.strptime(
            USER_INPUT_end_date_today, '%Y-%m-%d').date() - timedelta(days=1))
    else:
        USER_INPUT_end_date = str(datetime.strptime(
            USER_INPUT_end_date_today, '%Y-%m-%d').date() - timedelta(days=0))        
    # Using timedelta of 5 because the stock market might be colsed before the end data.
   
    USER_INPUT_start_date = str(datetime.strptime(
        USER_INPUT_end_date, '%Y-%m-%d').date() - timedelta(days=5))  

    
    
    
# filter
  
    #download today's data
   # data=yf.download(config_global.tickers_list,period='1d', interval='1m')
    #for getting yesterday's data
    #data2 = yf.download(config_global.tickers_list, start=config_global.USER_INPUT_start_date,
            #    end=config_global.USER_INPUT_end_date, group_by='ticker')
    #print(data2)
    for symbol in tickers_list:
        data=yf.download(symbol,period='1d', interval='1m')
        data2 = yf.download(symbol, start=USER_INPUT_start_date,
                end=USER_INPUT_end_date, group_by='ticker')
        print(data2)
        if data2.empty == False:
            # Create a list of closing prices for each symbol and get yesterday's closing price
            closing_price = data2['Close'].tolist()
            
            yesterday_close_price = closing_price[-2]
        print(yesterday_close_price)   
        if data.empty== False:    
         # Create a list of closing prices for each symbol
            closing_prices_list = data['Close'].tolist()
            
            order=sorted(closing_prices_list,reverse=True)
            N,M=order[0],order[-1]
            
            

 #operation in loop
    
        time = len(closing_prices_list)
        current_price = closing_prices_list[time-1]
        print(current_price)
        if (yesterday_close_price > current_price):
            #check if the price is down than today's highest price
            down_recent,down_first = down_trend(current_price,yesterday_close_price,N)
            if(down_recent > down_first):
                down_percent.append((down_recent/yesterday_close_price)*100)
                down_trend_sym.append(symbol)

        else:
            #check if the price is up than today's lowest price
            up_recent,up_first = up_trend(current_price,yesterday_close_price,M)
            print("up-rec",up_recent)
            print("up-fr",up_first)
            if(up_recent > up_first):
                
                up_percent.append((up_recent/yesterday_close_price)*100)
                up_trend_sym.append(symbol)

                

    # Store information in a dataframe and export a CSV
    d={"uptrend stock":up_trend_sym,
           "up percent" : up_percent,
           "downtrend stock":down_trend_sym,
           "down percent" : down_percent}
    
   
        
    final = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
     #rearrange data in descending order
   
    final.sort_values('up percent',axis=0,ascending=False, inplace=True,)
     #final.sort_values("down percent",axis=1,ascending=False, inplace=True,)
     
    final.set_index("uptrend stock",inplace=True)
    final.reset_index(inplace=True) 
    final.to_csv('uptrend and downtrend stocks.csv',index=False)
     
    print(final)  
    print(USER_INPUT_start_date,USER_INPUT_end_date)
    return final
   


def down_trend(current_price,yesterday_close_price,N):
    down_recent = yesterday_close_price - current_price
    down_first = yesterday_close_price - N 
    return(down_recent, down_first)

def up_trend(current_price,yesterday_close_price,M):
    up_recent = current_price - yesterday_close_price
    up_first = M - yesterday_close_price
    return(up_recent, up_first)


# In[2]:





# In[ ]:





# In[ ]:





# In[ ]:




