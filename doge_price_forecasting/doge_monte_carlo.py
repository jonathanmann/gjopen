#!/usr/bin/env python
import pandas as pd
import random
import datetime

u = lambda: [-1,1,1][random.randrange(3)] # 1 / 3 chance of flipping the sign
sample = lambda data: random.sample(data,1)[0] # Pull a random sample from a set
get_price = lambda ticker: float(pd.read_html('https://finance.yahoo.com/quote/' + ticker + '/history')[0]["Close*"].iloc[0])

EXPIRATION = datetime.date(2021,8,1)
CURR_PRICE = get_price('DOGE-USD')
REMAINING_DAYS = (EXPIRATION - datetime.date.today()).days
TRIALS = 10000
CURR_PRICE_WEIGHT = .1 # Bias toward today's price
SIMULATED_PRICE_WEIGHT = 1 - CURR_PRICE_WEIGHT

df = pd.read_csv("DOGE-USD.csv")
df["Previous"] = df.Close.shift()
df.dropna(inplace=True)
shifts = set((df.Close/df.Previous).apply(lambda x: x - 1)) # Make a set of historical price shifts

low = 0 
high = 0
for j in range(TRIALS):
    price = CURR_PRICE
    for i in range(REMAINING_DAYS):
        move = sample(shifts) * (CURR_PRICE_WEIGHT * CURR_PRICE + SIMULATED_PRICE_WEIGHT * price) * u()
        price = price  + move
        if price <= .25:
            low += 1
            break
        if price >= 1:
            high += 1
            break

inputs = [x * 100 / TRIALS for x in [low,high]]
print("LOW:{}%,HIGH:{}%".format(*inputs))
