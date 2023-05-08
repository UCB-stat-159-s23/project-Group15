from opioidtools import utils
import numpy as np
import pandas as pd
import os

gdp_opioid = pd.read_csv('data/gdp_opioid.csv')

def test_to_numeric():
    temp_col = to_numeric(gdp_opioid, "Deaths")
    assert temp_col is not none
    assert temp_col[0] is not str
    
def viz():
    figure_list = ["Avg_GDP_for_Each_State_Over_Years.png",
                  "State_Deaths.png",
                  "State_Crude_Rates"]
    for filename in fitur_list:
        assert filename is in os.listdir('figures')
