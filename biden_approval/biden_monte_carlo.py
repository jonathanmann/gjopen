#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('approval','2022-03-31',40,50,42.8)
s.run_trials()



