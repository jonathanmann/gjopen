#!/usr/bin/env python
import pandas as pd
import random

BTC_PRICE = 55838.80
REMAINING_DAYS = 51
OBSERVATIONS = 10000

btc = pd.read_csv("BTC-USD.csv")
btc.dropna(inplace=True)

btc["Previous"] = btc.Close.shift()
btc.dropna(inplace=True)
btc = btc[["Date","Close","Previous"]]
btc["Move"] = (btc.Close/btc.Previous) 
shifts = set(btc.Move)

low = 0 
high = 0
for j in range(OBSERVATIONS):
    price = BTC_PRICE
    for i in range(REMAINING_DAYS):
        shift = random.sample(shifts,1)[0] - 1
        move = .5 * shift * BTC_PRICE + .5 * shift * price 
        if (random.randrange(0,1) == 1):
            move = move * (-1)
        price = price  + move
        if price < 25000:
            low += 1
            break
        if price > 100000:
            high += 1
            break

print("LOW:{}%,HIGH:{}%".format(low * 100  / OBSERVATIONS ,high * 100 / OBSERVATIONS))

