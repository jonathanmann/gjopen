#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

BTC_START = 38717.77
ADA_START = 1.66
ETH_START = 2774.54
XRP_START = 0.979175

BTC_PRES = 60700.2
ADA_PRES = 2.15
ETH_PRES = 4158.32
XRP_PRES = 1.12

btc_ratio = BTC_PRES / BTC_START
ada_ratio = ADA_PRES / ADA_START
eth_ratio = ETH_PRES / ETH_START
xrp_ratio = XRP_PRES / XRP_START

print(btc_ratio)
print(ada_ratio)
print(eth_ratio)
print(xrp_ratio)

"""
s = mc('BTC','2021-11-29',BTC_START * (btc_ratio + eth_ratio)/2,BTC_PRES,BTC_PRES)
down_prob,up_prob = s.run_trials()

#s = mc('ADA','2021-11-29',ADA_PRES,ADA_START * (ada_ratio + btc_ratio)/2,ADA_PRES)
#s = mc('ADA','2021-11-29',ADA_PRES,ADA_START * btc_ratio,ADA_PRES)
s = mc('XRP','2021-10-29',XRP_PRES,XRP_START * btc_ratio,XRP_PRES)
down_prob,up_prob = s.run_trials()
"""


