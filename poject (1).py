#!/usr/bin/env python
# coding: utf-8

# In[1]:


import alpaca_trade_api as tradeapi
import time

# Set your Alpaca API key and secret
api_key = 'API KEY'
api_secret = 'API SECRET'
base_url = 'https://paper-api.alpaca.markets'  # Use paper trading base URL for testing

# Initialize Alpaca API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')


# In[2]:


import datetime
import time

import alpaca_trade_api as tradeapi
import numpy as np
import pandas as pd

pd.options.display.max_rows = 999


from datetime import timedelta

from pytz import timezone

tz = timezone('EST')

#----Frequency-----#
freq = '1Min'
symbol = 'AAPL'
#----Moving average-----#
slow = 20
fast = 1


# In[3]:


data = api.get_bars(symbol, freq,start='2024-02-13',end='2024-02-13').df
data


# In[4]:


#20min avg
#data.loc[:, (x, 'fast_ema_1min')] = data[x]['close'].rolling(window=fast).mean()
data['slow_ema_20min'] = data['vwap'].rolling(window=20).mean()
data=data.dropna()
data


# In[11]:


start_time = '09:30:00'
end_time = '16:00:00'

times = data.index.strftime('%H:%M:%S')

is_within_trading_hours = pd.Series(times).between(start_time, end_time).values

data= data[is_within_trading_hours]
data


# In[13]:


import time
specific_time = pd.Timestamp('2024-02-13 09:31:00+00:00')

def cancel_pending_orders(symbol):
    open_orders = api.list_orders(status='open')
    for order in open_orders:
        if order.symbol == symbol:
            api.cancel_order(order.id)
            print(f"Cancelled open order for {order.symbol}")

# 
if specific_time in data.index:
    cancel_pending_orders(symbol)  # 
    
    open_price = data.at[specific_time, 'open']
    api.submit_order(
        symbol=symbol,
        qty=5,
        side='buy',
        type='market',
        time_in_force='gtc'  #
    )
    print(f"Submitted order to buy 5 shares of {symbol} at {specific_time}")

for timestamp, row in data.iterrows():
    if timestamp > specific_time:  # after9.31
       # time.sleep(2)
        vwap = row['vwap']
        slow_ema = row['slow_ema_20min']
        last_close_price = row['close']
        
        cancel_pending_orders(symbol)  # cancel exist order in case of potential wash trade
        print(timestamp)
        if vwap < slow_ema:
            # buy
            api.submit_order(
                symbol=symbol,
                qty=2,
                side='buy',
                type='market',
                time_in_force='gtc',  #
                #limit_price=round(vwap,2)
            )
            print(f"Buy order placed for {symbol} at {round(last_close_price * 1.01, 2)}")
        elif vwap >= slow_ema:
            
            # sell
            api.submit_order(
                symbol=symbol,
                qty=1,
                side='sell',
                type='market',
                time_in_force='gtc',  
                #limit_price=round(vwap,2)
            )
            print(f"Sell order placed for {symbol} at {round(last_close_price * 0.99, 2)}")
            


# In[ ]:





# In[ ]:




