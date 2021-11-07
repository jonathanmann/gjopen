#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('approval','2022-03-31',45,45,42.7)
s.run_trials()



