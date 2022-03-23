import pandas as pd
import yfinance as yf
import json


import momentum as mom
import uptrend_downtrend as updowntrend
import highest_difference as h_difference
import decreased_nm_percent as nm_per


momentum_for_json = mom.carry_momentum()



up_down_trend =  updowntrend.task_9_up_down_trend()




high_difference_for_json = h_difference.main_mod()


nm_per_for_json = nm_per.task_7_decreased_nm_per()


# this is main section and used to update value of all ticker listed in our csx and save in stock_pre_output.json
top_n_stocks = pd.read_csv(
        'list.csv', names=['symbols'])
top_n_stocks=top_n_stocks['symbols'].to_list()[2]

dic_json={}
for count,sym_of_stock in enumerate(top_n_stocks):
    dic_json[sym_of_stock] = {}
   
    # section 1 add momentum ----------------------------------------------------------------------------------
    for count_momentum in range (0,len(momentum_for_json)):
        if(sym_of_stock == momentum_for_json['symbol'][count_momentum]):
            dic_json[sym_of_stock]['momentum_high'] = momentum_for_json['high'][count_momentum]
            break
            
        else:
            dic_json[sym_of_stock]['momentum_high'] = ' '
    
    # section 2 updown trend ----------------------------------------------------------------------------------
    for count_updown in range(0,len(up_down_trend)):
        if(sym_of_stock == up_down_trend['uptrend stock'][count_updown]):
            dic_json[sym_of_stock]['stock_trend'] = 'up'
            dic_json[sym_of_stock]['updown_percent'] = up_down_trend['up percent'][count_updown]
            
        if(sym_of_stock == up_down_trend['downtrend stock'][count_updown]):
            dic_json[sym_of_stock]['stock_trend'] = 'down'
            dic_json[sym_of_stock]['updown_percent'] = up_down_trend['down percent'][count_updown]    
            
            
    # section 3 high difference  ----------------------------------------------------------------------------------
    for count_highdiff in range (0,len(high_difference_for_json)):
        if(sym_of_stock == high_difference_for_json['symbol'][count_highdiff]):
            dic_json[sym_of_stock]['high_difference_avg_per'] = high_difference_for_json['avg_per'][count_highdiff]  
            
    # section 4 high difference  ----------------------------------------------------------------------------------
    for count_nmper in range (0,len(nm_per_for_json)):
        if(sym_of_stock == nm_per_for_json['stock'][count_nmper]):
            dic_json[sym_of_stock]['price_down_nmper'] = nm_per_for_json['price down'][count_nmper]
            dic_json[sym_of_stock]['stock_price_at_N_nmper'] = nm_per_for_json['stock price at N'][count_nmper]
            dic_json[sym_of_stock]['time_N_nmper'] = nm_per_for_json['time N'][count_nmper]
            dic_json[sym_of_stock]['stock_price_at_M_nmper'] = nm_per_for_json['stock price at M'][count_nmper]
            dic_json[sym_of_stock]['time_M_nmper'] = nm_per_for_json['time M'][count_nmper]
            dic_json[sym_of_stock]['closing_price_now_nmper'] = nm_per_for_json['closing price now'][count_nmper]
            
with open('stock_pre_output.json','w') as file:
    json.dump(dic_json,file)    
dic_json   














