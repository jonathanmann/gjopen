#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('coincap','2021-12-09',2.5,2.5,2.59)
s.run_trials()



