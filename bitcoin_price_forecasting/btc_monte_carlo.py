#!/usr/bin/env python
import pandas as pd
import random
import datetime

EXPIRATION = datetime.date(2021,7,1)
CURR_PRICE =  54585.40
REMAINING_DAYS = (EXPIRATION - datetime.date.today()).days
TRIALS = 10000
CURR_PRICE_WEIGHT = .2 # Bias toward today's prices
SIMULATED_PRICE_WEIGHT = 1 - CURR_PRICE_WEIGHT

u = lambda: [-1,1,1][random.randrange(3)] # 1 / 3 chance of flipping the sign
sample = lambda data: random.sample(data,1)[0] # Pull a random sample from a set

df = pd.read_csv("BTC-USD.csv")
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
        if price < 25000:
            low += 1
            break
        if price > 100000:
            high += 1
            break

inputs = [x * 100 / TRIALS for x in [low,high]]
print("LOW:{}%,HIGH:{}%".format(*inputs))

