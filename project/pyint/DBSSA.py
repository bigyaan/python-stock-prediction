#!/usr/bin/env python
# coding: utf-8

# In[5]:



import yfinance as yf
import pandas as pd


USER_INPUT_SINGLE_STOCK_ANALYSIS_STOCK_SYMBOL = 'V'
USER_INPUT_start_date = '2020-10-05'
USER_INPUT_end_date = '2021-12-12'


def single_stock_analysis():
    """
    Function for analyzing a single stock
    """
    data = yf.download(USER_INPUT_SINGLE_STOCK_ANALYSIS_STOCK_SYMBOL, USER_INPUT_start_date,
                       end=USER_INPUT_end_date, group_by='ticker')

    closing_prices_list = data['Close'].to_list()

    # Same compute function can work for single and multiple stocks.
    # Another function is required if variables are different.
    symbol = USER_INPUT_SINGLE_STOCK_ANALYSIS_STOCK_SYMBOL
    

#compute() all_operation()
    all_operation(symbol,closing_prices_list)

    

    


# In[6]:


def all_operation(symbol,closing_prices_list):
    """
    This function is split only to be used both by the single stock and the multiple stocks.
    """
    # Clear all variables before analyzing every stock symbol
    days_count_for_up_trend = 0
    days_count_for_down_trend = 0

    LIST_amount_change_per_uptrend = []
    LIST_amount_change_per_downtrend = []

    DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend = []
    DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend = []

    DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend = []
    DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend = []

    DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up = 0
    DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down = 0

    was_downtrend = 0
    was_uptrend = 0

    DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends = []
    DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends = []

    no_of_up_trend = 0
    no_of_down_trend = 0

    DAY_DATA_ALL_IND_STOCK_average_up_amount_in_up_trends = 0
    DAY_DATA_ALL_IND_STOCK_average_down_amount_in_down_trends = 0

    DAY_DATA_ALL_IND_STOCK_average_up_days_in_up_trends = 0
    DAY_DATA_ALL_IND_STOCK_average_down_days_in_down_trends = 0

    DAY_DATA_IND_STOCK_last_closing_price = 0
    DAY_DATA_IND_STOCK_average_price_input_Period = 0

    last_day_price_change = 0.0
    percent_change = 0.0

    uptrend_flag = 0
    trend =[]

    all_stock_info =pd.DataFrame()
    # Process closing price list for current symmbol
    for index in range(1, len(closing_prices_list)):
        previous_price = closing_prices_list[index-1]
        current_price = closing_prices_list[index]

        if (current_price > previous_price):
            # Count number of days stock price goes up
            days_count_for_up_trend += 1
            # Store amount difference for up trend
            LIST_amount_change_per_uptrend.append(
                current_price - previous_price)
            # Check if there was a down trend
            is_price_down(days_count_for_down_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend,trend,DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,LIST_amount_change_per_downtrend,DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down,was_uptrend)
        else:
            # Count number of days stock price goes down
            days_count_for_down_trend += 1
            # Store amount difference for down trend
            LIST_amount_change_per_downtrend.append(
                current_price - previous_price)
            # Check if there was an up trend
            is_price_up(days_count_for_up_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,trend,DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,LIST_amount_change_per_uptrend,DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up,was_downtrend)

        # Check for up and down trend
        is_updown_trend(was_uptrend, was_downtrend,DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends,DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend)

    # Trends are only recorded after a break.
    # So, the following 3 calls are to check for the last change.
    if is_price_up(days_count_for_up_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,trend,DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,LIST_amount_change_per_uptrend,DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up,was_downtrend):
        # This flag is used to represent the start of an up trend.
        # Used when deciding to compute the percent chance.
        uptrend_flag = 1 if DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend[
            -1] == 1 else 0
    else:
        is_price_down(days_count_for_down_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend,trend,DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,LIST_amount_change_per_downtrend,DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down,was_uptrend)

    # Check for up and down trend
    is_updown_trend(was_uptrend, was_downtrend,DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends,DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend)

    # Number of up trend = Length of list of number of days price went up per up trend
    no_of_up_trend = len(
        DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend)
    # Number of down trend = Length of list of number of days price went down per down trend
    no_of_down_trend = len(
        DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend)

    # If there are no up trends, will result in a zero division error
    if no_of_up_trend:
        # Average up amount in up trends = sum of list of amount per up trend / total up trend
        DAY_DATA_ALL_IND_STOCK_average_up_amount_in_up_trends = sum(
            DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend) / no_of_up_trend

        # Average number of days in up trends = total days stock went up / number of up trends
        DAY_DATA_ALL_IND_STOCK_average_up_days_in_up_trends = DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up /             no_of_up_trend
    else:
        DAY_DATA_ALL_IND_STOCK_average_up_amount_in_up_trends = 0
        DAY_DATA_ALL_IND_STOCK_average_up_days_in_up_trends = 0

    # If there are no down trends, will result in a zero division error
    if no_of_down_trend:
        # Average down amount in down trends = sum of list of amount per down trend / total down trend
        DAY_DATA_ALL_IND_STOCK_average_down_amount_in_down_trends = sum(
            DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend) / no_of_down_trend

        # Average number of days in down trends = total days stock went down / number of down trends
        DAY_DATA_ALL_IND_STOCK_average_down_days_in_down_trends = DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down /             no_of_down_trend
    else:
        DAY_DATA_ALL_IND_STOCK_average_down_amount_in_down_trends = 0
        DAY_DATA_ALL_IND_STOCK_average_down_days_in_down_trends = 0

    # Total days = length of list of closing prices
    total_days = len(closing_prices_list)

    # Last closing price = last item of closing prices list
    DAY_DATA_IND_STOCK_last_closing_price = closing_prices_list[
        total_days - 1]

    last_day_price_change = current_price - previous_price

    percent_change = (
        last_day_price_change/previous_price)*100

    # Average price in given period = total of closing prices list / total days
    DAY_DATA_IND_STOCK_average_price_input_Period = sum(
        closing_prices_list)/total_days
    
    # Store all computed information in a dataframe
    all_stock_info = all_stock_info.append({'symbol': symbol,
                                                                        'total_days': total_days,
                                                                        'DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up': DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up,
                                                                        'DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down': DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down,
                                                                        'no_of_up_trend': no_of_up_trend,
                                                                        'no_of_down_trend': no_of_down_trend,
                                                                        'DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend': DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,
                                                                        'trend': trend,
                                                                        'DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend': DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend,
                                                                        'DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend': DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,
                                                                        'DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend': DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,
                                                                        'DAY_DATA_ALL_IND_STOCK_average_up_amount_in_up_trends': DAY_DATA_ALL_IND_STOCK_average_up_amount_in_up_trends,
                                                                        'DAY_DATA_ALL_IND_STOCK_average_down_amount_in_down_trends': DAY_DATA_ALL_IND_STOCK_average_down_amount_in_down_trends,
                                                                        'DAY_DATA_ALL_IND_STOCK_average_up_days_in_up_trends': DAY_DATA_ALL_IND_STOCK_average_up_days_in_up_trends,
                                                                        'DAY_DATA_ALL_IND_STOCK_average_down_days_in_down_trends': DAY_DATA_ALL_IND_STOCK_average_down_days_in_down_trends,
                                                                        'DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends': DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends,
                                                                        'DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends': DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends,
                                                                        'DAY_DATA_IND_STOCK_last_closing_price': DAY_DATA_IND_STOCK_last_closing_price,
                                                                        'last_day_price_change': last_day_price_change,
                                                                        'percent_change': percent_change,
                                                                        'DAY_DATA_IND_STOCK_average_price_input_Period': DAY_DATA_IND_STOCK_average_price_input_Period,
                                                                        'uptrend_flag': uptrend_flag
                                                                        }, ignore_index=True)
    
    
    
    
    
    
    
    all_stock_info.to_csv('single_stock_analysis.csv')
    
    
    
    


# In[7]:


def is_price_up(days_count_for_up_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,trend,DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,LIST_amount_change_per_uptrend,DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up,was_downtrend):
    """
    This function checks if the price of the stock had rose before the current drop in price.
    The uptrend is only recorded after detecting a drop in price.
    Therefore, this function is only called when the stock price drops.
    """
    # Following variable represents the no of times price had risen before a drop.
    # So an up trend is considered if the stock price had risen
    if days_count_for_up_trend:
        # Store total days for this up trend
        
        DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend.append(
            days_count_for_up_trend)
        trend.append(days_count_for_up_trend)   
        # Store amount changed for this up trend
        DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend.append(
            sum(LIST_amount_change_per_uptrend))
        # Clearing for another trend
        LIST_amount_change_per_uptrend = []
        # Store number of times stock went up
        DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_up += days_count_for_up_trend
        # Clearing for another trend
        days_count_for_up_trend = 0

        # This flags the end of an up trend and start of a down trend
        was_downtrend = 1
        
        return 1
    else:
        return 0

#DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend
# Check if there was a down trend
def is_price_down(days_count_for_down_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend,trend,DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,LIST_amount_change_per_downtrend,DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down,was_uptrend):
    """
    This function checks if the price of the stock had dropped before the current rise in price.
    The downtrend is only recorded after detecting a rise in price.
    Therefore, this function is only called when the stock price rises.
    """
    # Following variable represents the no of times price had dropped before a rise.
    # So a down trend is considered if the stock price had dropped
    if days_count_for_down_trend:
        # Store total days for this down trend
        DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend.append(
            days_count_for_down_trend)
        trend.append(-days_count_for_down_trend)    
        
        
        # Store amount changed for this down trend
        DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend.append(
            sum(LIST_amount_change_per_downtrend))
        # Clearing for another trend
        LIST_amount_change_per_downtrend = []
        # Store number of times stock went down
        DAY_DATA_ALL_IND_STOCK_no_of_times_price_went_down += days_count_for_down_trend
        # Clearing for another trend
        days_count_for_down_trend = 0

        # This flags the end of down trend and start of up trend
        was_uptrend = 1
        
        return 1
    else:
        return 0


# In[ ]:





# In[8]:



# Check for up and down trend
def is_updown_trend(was_uptrend, was_downtrend,DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends,DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend,DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend,DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend):
    """
    This function checks for up and down trend.
    If both was_uptrend and was_ downtrend variables are 1, it is an up and down trend.
    """
    if was_uptrend and was_downtrend:
        # Store amount change for up and down trend
        # Adding because the amount is stored as negative values for down trend
        DAY_DATA_LIST_IND_STOCK_amount_change_per_up_and_down_trends.append(
            DAY_DATA_LIST_IND_STOCK_total_up_amount_per_up_trend[-1] +
            DAY_DATA_LIST_IND_STOCK_total_down_amount_per_down_trend[-1]
        )
        # Clear if an up and down trend was detected
        was_uptrend = was_downtrend = 0
        # Store total number of days in up and down trend
        DAY_DATA_LIST_IND_STOCK_no_of_days_per_up_and_down_trends.append(
            DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_up_per_up_trend[-1] +
            DAY_DATA_LIST_IND_STOCK_no_of_days_price_went_down_per_down_trend[-1]
        )


# In[9]:


single_stock_analysis()


# In[ ]:





# In[ ]:





# In[326]:





# In[ ]:




