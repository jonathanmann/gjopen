#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import seaborn as sns

CURRENT_SALES_WEEK = '2021-06-13'

def get_dt_obj(str_dt):
    split_date = [int(x) for x in str_dt.split('-')]
    return datetime.date(*split_date)

def format_ranks(rank,filler=16):
    if rank > 0:
        return int(rank)
    return filler

df = pd.read_csv('ThinkAgainWeeks.csv')
df.reset_index()
df['DATE'] = df.DATE.apply(get_dt_obj)
df['RANK'] = df.RANK.apply(format_ranks)
df['VIS_RANK'] = 16 - df.RANK
df['WEEK'] = df.index + 1
df = df[df.DATE <= get_dt_obj(CURRENT_SALES_WEEK)]
week_range = (range(1,len(df.RANK)))
ax = sns.regplot(df.WEEK,df.VIS_RANK,ci=95)
ax.set_yticks(range(-4,20))
ax.set_xticks(range(1,len(df.DATE) + 1))
ax.set_xticklabels(df.DATE,rotation= 45)
ax.set_yticklabels(range(1,21)[::-1])
plt.show()
