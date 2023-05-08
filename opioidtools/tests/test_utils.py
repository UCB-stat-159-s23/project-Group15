from opioidtools import utils
import numpy as np
import pandas as pd
import os

gdp_opioid = pd.read_csv('data/gdp_opioid.csv')

def test_to_numeric():
    temp_col = utils.to_numeric(gdp_opioid, "Deaths")
    assert temp_col is not None
    assert temp_col[0] is not str
    
def test_viz():
    figure_list = ["Avg_GDP_for_Each_State_Over_Years.png",
                  "Deaths.png",
                  "Crude Rate.png"]
    for filename in figure_list:
        assert filename in os.listdir('figures')
