#!/usr/bin/env python
import pandas as pd
import random
import datetime

BTC_START = 38717.77
ADA_START = 1.66
ETH_START = 2774.54
XRP_START = 0.979175

BTC_PRES = 67412.23
ADA_PRES = 2.29
ETH_PRES = 4747.74
XRP_PRES = 1.26

btc_ratio = BTC_PRES / BTC_START
ada_ratio = ADA_PRES / ADA_START
eth_ratio = ETH_PRES / ETH_START
xrp_ratio = XRP_PRES / XRP_START

print(btc_ratio)
print(ada_ratio)
print(eth_ratio)
print(xrp_ratio)


expiration_date = '2021-11-29'

split_date = [int(x) for x in expiration_date.split('-')]
expiration = datetime.date(*split_date)
remaining_days = (expiration - datetime.date.today()).days

def get_shifts(symbol):
    df = pd.read_csv(symbol + ".csv")
    df["Previous"] = df.Close.shift()
    df.dropna(inplace=True)
    shifts = set((df.Close/df.Previous).apply(lambda x: x - 1)) # Make a set of historical price shifts
    return shifts

def random_flip(move,cx=1):
    chance_array = [-1] + [1]*cx
    if move == 0 or 1 == chance_array[random.randrange(cx + 1)]: # 1 / (cx + 1) chance of flipping the sign
        return move
    return (1 / (1 + move) - 1)


def correlated_flip(move,btc_move,prob):
    if random.random() < prob:
        if move * btc_move > 0:
            return move
        return (1 / (1 + move) - 1)
    if move * btc_move > 0:
        return (1 / (1 + move) - 1)
    return move

sample = lambda data: random.sample(data,1)[0] # Pull a random sample from a set
btc_shifts = get_shifts('BTC')
ada_shifts = get_shifts('ADA')
eth_shifts = get_shifts('ETH')
xrp_shifts = get_shifts('XRP')

ledger = [0,0,0,0]

for j in range(100000):
    btc_price = BTC_PRES
    ada_price = ADA_PRES
    eth_price = ETH_PRES
    xrp_price = XRP_PRES
    for i in range(remaining_days):
        btc_move = random_flip(sample(btc_shifts)) * btc_price
        btc_price = btc_price + btc_move
        ada_move = correlated_flip(sample(ada_shifts),btc_move,.75) * ada_price
        ada_price = ada_price + ada_move
        eth_move = correlated_flip(sample(eth_shifts),btc_move,.8) * eth_price
        eth_price = eth_price + eth_move
        xrp_move = correlated_flip(sample(xrp_shifts),btc_move,.73) * xrp_price
        xrp_price = xrp_price + xrp_move

    btc_end = btc_price / BTC_START
    ada_end = ada_price / ADA_START
    eth_end = eth_price / ETH_START
    xrp_end = xrp_price / XRP_START

    outcomes = [btc_end,ada_end,eth_end,xrp_end]
    if max(outcomes) == btc_end:
        ledger[0] += 1
    if max(outcomes) == ada_end:
        ledger[1] += 1
    if max(outcomes) == eth_end:
        ledger[2] += 1
    if max(outcomes) == xrp_end:
        ledger[3] += 1
        """
        if j % 7 == 0:
            print(btc_end,ada_end,eth_end,xrp_end)
        """
    
print([x/1000 for x in ledger])

