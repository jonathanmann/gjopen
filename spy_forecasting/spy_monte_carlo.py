#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc
s = mc('SPY','2021-12-31',366.8,366.8,454.29)
s.run_trials(sudden_condition='low')
