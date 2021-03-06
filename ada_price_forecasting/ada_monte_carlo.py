#!/usr/bin/env python
import pandas as pd
import random
import datetime

u = lambda: 1 #[-1,1,1][random.randrange(3)] # 1 / 3 chance of flipping the sign
sample = lambda data: random.sample(data,1)[0] # Pull a random sample from a set
get_price = lambda ticker: float(pd.read_html('https://finance.yahoo.com/quote/' + ticker + '/history')[0]["Close*"].iloc[0])

EXPIRATION = datetime.date(2021,7,2)
CURR_PRICE = get_price('ADA-USD')
REMAINING_DAYS = (EXPIRATION - datetime.date.today()).days
TRIALS = 10000
CURR_PRICE_WEIGHT = .2 # Bias toward today's price
SIMULATED_PRICE_WEIGHT = 1 - CURR_PRICE_WEIGHT

df = pd.read_csv("ADA-USD.csv")
df["Previous"] = df.Close.shift()
df.dropna(inplace=True) 
shifts = set((df.Close/df.Previous).apply(lambda x: x - 1)) # Make a set of historical price shifts
lowest = low = middle = high = highest = 0 # Initialize possible outcomes 

for j in range(TRIALS):
    price = CURR_PRICE
    for i in range(REMAINING_DAYS):
        price = price + sample(shifts) * (CURR_PRICE_WEIGHT * CURR_PRICE + SIMULATED_PRICE_WEIGHT * price) * u()
    if price < .5:
        lowest += 1
    if price >= .5 and price <= 1:
        low += 1
    if price > 1 and price <= 2.5:
        middle += 1
    if price > 2.5 and price <= 5:
        high += 1
    if price > 5:
        highest += 1

inputs = [x * 100 / TRIALS for x in [lowest,low,middle,high,highest]]
print("LOWEST:{}%,LOW:{}%,MIDDLE:{}%,HIGH:{}%,HIGHEST:{}%".format(*inputs))
