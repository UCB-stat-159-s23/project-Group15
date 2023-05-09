import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats

def to_numeric(df, col_name):
    """converts column of dataframe to numeric
    Parameters
    ----------
    df: dataframe
        The dataframe containing the column to convert 
    col_name: str
        The column to convert to numeric
    """
    return pd.to_numeric(df[col_name])

def cal_print_min_median_max_gdp(df):
    """returns the states with the minimum, median, and maximum GDP in & the values
    Parameters
    ----------
    df: dataframe
        The dataframe containing the average GDP for each state
    """
    #Find the Minimum, Median, and Maximum avg GDP among states over 2010 to 2014
    median_gdp = df.median()
    median_gdp_states = df[df.eq(median_gdp)].index.tolist()

    min_gdp = df.min()
    min_gdp_states = df[df.eq(min_gdp)].index.tolist()

    max_gdp = df.max()
    max_gdp_states = df[df.eq(max_gdp)].index.tolist()

    # Print the results
    print(f"Minimum: {min_gdp:.2f} " f"State: {', '.join(min_gdp_states)}")
    print(f"Median: {median_gdp:.2f} " f"State: {', '.join(median_gdp_states)}")
    print(f"Maximum: {max_gdp:.2f} " f"State: {', '.join(max_gdp_states)}")
    
def cal_print_t_test_CR(df, state1, state2):
    """returns t-statistics for crude rate between 2 states and the p-value
    Parameters
    ----------
    df: dataframe
        The dataframe containing the crude rate for each state
    state1: str
        The first state to use in the t-test
    state2: str
        The second state to use in the t-test
    """
    #T test for Crude Rate between two states
    t_stat, p_value = scipy.stats.ttest_ind(df[df['State']== state1]['Crude Rate'],
                     df[df['State']== state2]['Crude Rate'],
                     axis=0)
    # Print results
    print("T-statistic:", t_stat)
    print("p-value:", p_value)
    
def cal_print_t_test_CR_for_two_groups(df):
    """returns t-statistics for crude rate between high GDP & low GDP state groups and its p-value
    Parameters
    ----------
    df: dataframe
        The dataframe containing the average GDP and crude rate for each state
    """
    # Calculate the average GDP for each state over 2010 to 2014
    state_avg_gdp_2010_to_2014 = df.groupby('State')['GDP_0101'].mean()
    
    # Filter out the high avg GDP and low avg GDP states (> or < than the median)
    median_gdp = state_avg_gdp_2010_to_2014.median()
    high_gdp_states = state_avg_gdp_2010_to_2014[state_avg_gdp_2010_to_2014 >= median_gdp].index
    low_gdp_states = state_avg_gdp_2010_to_2014[state_avg_gdp_2010_to_2014 < median_gdp].index
    high_low_gdp = df[df['State'].isin(high_gdp_states.union(low_gdp_states))]

    # Obtain the crude rate from high and low avg GDP from states.
    high_gdp_crude_rate = high_low_gdp.loc[high_low_gdp['State'].isin(high_gdp_states), 'Crude Rate']
    low_gdp_crude_rate = high_low_gdp.loc[high_low_gdp['State'].isin(low_gdp_states), 'Crude Rate']

    # T-test
    t_stat_for_two_groups_states, p_value_for_two_groups_states = scipy.stats.ttest_ind(high_gdp_crude_rate, low_gdp_crude_rate)

    # Print results
    print("T-statistic:", t_stat_for_two_groups_states)
    print("p-value:", p_value_for_two_groups_states)