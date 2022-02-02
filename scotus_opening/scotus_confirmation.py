#!/usr/bin/env python
import pandas as pd
import datetime

EXPIRATION = datetime.date(2022,8,1)
REMAINING_DAYS = (EXPIRATION - datetime.date.today()).days
DAYS_IN_YEAR = 365
REMAINING_SCALAR = REMAINING_DAYS/DAYS_IN_YEAR

mortality = dict(pd.read_csv('mortality.tsv',sep='\t'))
mortality['F'] = dict(mortality['F'])
mortality['M'] = dict(mortality['M'])

senators = {
    'Mark Kelley':['M',57],
    'Krysten Sinema':['F',45],
    'Maggie Hassan':['M',63],
    'Jeanne Shaheen':['F',75],
    'Jon Ossoff':['M',34],
    'Raphael Warnock':['M',52],
    'Tim Kaine':['M',63],
    'Mark Warner':['M',67],
    'Jon Tester':['M',65],
    'Sherrod Brown':['M',69],
    'Joe Manchin':['M',74],
    }

p = 1
for s in senators:
    g,a = senators[s]
    p = p * (1 - mortality[g][a]) 

print(1 - (1 - p) * REMAINING_SCALAR)
