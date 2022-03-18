#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('FB','2022-05-20',0,238.0,214.70)
s.run_trials(sudden_condition=True)



