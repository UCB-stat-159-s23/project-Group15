from opioidtools import plots
from opioidtools import computations
import numpy as np
import pandas as pd
import os

gdp_opioid = pd.read_csv('data/gdp_opioid.csv')

def test_to_numeric():
    temp_col = computations.to_numeric(gdp_opioid, "Deaths")
    assert type(temp_col[0]) is not str