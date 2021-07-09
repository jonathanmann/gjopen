#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('BZ=F','2021-07-16',74.39,74.39,75.59)
s.run_trials()



