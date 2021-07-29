#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

s = mc('approval','2021-08-13',50,55,51.89)
s.run_trials()



