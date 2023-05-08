from opioidtools import plots
from opioidtools import computations
import numpy as np
import pandas as pd
import os

gdp_opioid = pd.read_csv('data/gdp_opioid.csv')
   
def test_viz():
    figure_list = ["Deaths.png",
                  "Crude Rate.png"]
    for filename in figure_list:
        assert filename in os.listdir('figures')
        
def test_gdp():
    figure_list = ["Avg_GDP_for_Each_State_Over_Years.png",
                  'Two_Avg_GDP_States.png']
    for filename in figure_list:
        assert filename in os.listdir('figures')