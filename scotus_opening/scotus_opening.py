#!/usr/bin/env python
import pandas as pd
import datetime

EXPIRATION = datetime.date(2023,1,4)
REMAINING_DAYS = (EXPIRATION - datetime.date.today()).days
DAYS_IN_YEAR = 365
REMAINING_SCALAR = REMAINING_DAYS/DAYS_IN_YEAR
BREYER_PLANNED_RETIREMENT_ESTIMATE = .3333

mortality = dict(pd.read_csv('mortality.tsv',sep='\t'))
mortality['F'] = dict(mortality['F'])
mortality['M'] = dict(mortality['M'])

justices = {
    'Stephen Breyer': ['M',83],
    'Clarence Thomas':['M',73],
    'Samuel Alito':['M',71],
    'Sonia Sotomayer':['F',67],
    'John Roberts':['M',66],
    'Elena Kagan':['F',61],
    'Brett Kavanaugh':['M',56],
    'Neil Gorsuch':['M',54],
    'Amy Barrett':['F',49],
    }

p = (1 - BREYER_PLANNED_RETIREMENT_ESTIMATE) # tracks the probability that no one leaves

for j in justices:
    g,a = justices[j]
    p = p * (1 - mortality[g][a]) 

print(1 - (1 - p) * REMAINING_SCALAR)
