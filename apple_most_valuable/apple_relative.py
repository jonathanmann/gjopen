#!/usr/bin/env python
import pandas as pd
import random
import datetime

AAPL_PRES = 2.490
MSFT_PRES = 2.523 
ARAM_PRES = 2.016


expiration_date = '2021-12-31'

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

aapl_shifts = get_shifts('AAPL')
msft_shifts = get_shifts('MSFT')
aram_shifts = get_shifts('ARAM')


ledger = [0,0,0]

for j in range(100000):
    aapl_price = AAPL_PRES
    msft_price = MSFT_PRES
    aram_price = ARAM_PRES
    for i in range(remaining_days):
        aapl_move = random_flip(sample(aapl_shifts)) * aapl_price
        aapl_price = aapl_price + aapl_move
        msft_move = correlated_flip(sample(msft_shifts),aapl_move,.77) * msft_price
        msft_price = msft_price + msft_move
        aram_move = correlated_flip(sample(aram_shifts),aapl_move,.39) * aram_price
        aram_price = aram_price + aram_move

    aapl_end = aapl_price 
    msft_end = msft_price
    aram_end = aram_price

    outcomes = [aapl_end,msft_end,aram_end]
    if max(outcomes) == aapl_end:
        ledger[0] += 1
    if max(outcomes) == msft_end:
        ledger[1] += 1
    if max(outcomes) == aram_end:
        ledger[2] += 1
        """
        if j % 7 == 0:
            print(aapl_end,msft_end,aram_end)
        """
    
print([x/1000 for x in ledger])

