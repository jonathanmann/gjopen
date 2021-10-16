#!/usr/bin/env python
import sys
sys.path.append('..')
from monte_carlo_forecasting.MonteCarlo import Simulation as mc

#s = mc('SPY','2021-12-31',361.392,565.36,442.42)
s = mc('SPY','2021-12-31',361.4,565.36,442.42)
s.run_trials(sudden_condition=True)



