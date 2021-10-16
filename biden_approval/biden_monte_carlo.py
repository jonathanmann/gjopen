#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('approval','2021-08-16',45,50,50.2)
s.run_trials()



