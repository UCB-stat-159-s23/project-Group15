# Standard numerical analysis imports
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats

def to_numeric(df, col_name):
    return pd.to_numeric(df[col_name])

def state_viz(df, col_name):
    fig, axs = plt.subplots(figsize=(8,45), nrows=17, ncols=3)

    # create state name array and reshape it
    state_name = df['State'].unique()
    state_name = np.reshape(state_name, (-1, 3))

    for col in range(3):
        for row in range(17):
            sns.pointplot(data = df[df['State']==state_name[row,col]], 
                          x='Year', y=col_name, ax = axs[row,col])
            axs[row,col].set_title(state_name[row,col])

            # add y ticks for only the first column of plots
            if col != 0:
                axs[row,col].set_yticks([])

            # add x ticks for only the last row of plots
            if row != 16:
                axs[row,col].set_xticks([])

            axs[row,col].set_xlabel('')
            axs[row,col].set_ylabel('')
            axs[row,col].set_ylim(0,(max(df[col_name])%5+1)*5)
    plt.savefig('figures/'+col_name)
    plt.show()

def avg_gdp_states(gdp_avg_df):
    #Find the Minimum, Median, and Maximum avg GDP among states over 2010 to 2014
    median_gdp = gdp_avg_df.median()
    median_gdp_states = gdp_avg_df[gdp_avg_df.eq(median_gdp)].index.tolist()

    min_gdp = gdp_avg_df.min()
    min_gdp_states = gdp_avg_df[gdp_avg_df.eq(min_gdp)].index.tolist()

    max_gdp = gdp_avg_df.max()
    max_gdp_states = gdp_avg_df[gdp_avg_df.eq(max_gdp)].index.tolist()

    # Print the results
    print(f"Minimum: {min_gdp:.2f} " f"State: {', '.join(min_gdp_states)}")
    print(f"Median: {median_gdp:.2f} " f"State: {', '.join(median_gdp_states)}")
    print(f"Maximum: {max_gdp:.2f} " f"State: {', '.join(max_gdp_states)}")

def high_low_crude_rates_ttest(gdp_avg_df,df):
    # Filter out the high avg GDP and low avg GDP states (> or < than the median)
    median_gdp = gdp_avg_df.median()
    high_gdp_states = gdp_avg_df[gdp_avg_df >= median_gdp].index
    low_gdp_states = gdp_avg_df[gdp_avg_df < median_gdp].index
    high_low_gdp = df[df['State'].isin(high_gdp_states.union(low_gdp_states))]

    # Obtain the crude rate from states with high and low avg GDP
    high_gdp_crude_rate = high_low_gdp.loc[high_low_gdp['State'].isin(high_gdp_states), 'Crude Rate']
    low_gdp_crude_rate = high_low_gdp.loc[high_low_gdp['State'].isin(low_gdp_states), 'Crude Rate']
    
    # T-test
    t_stat_for_two_groups_states, p_value_for_two_groups_states = scipy.stats.ttest_ind(high_gdp_crude_rate, low_gdp_crude_rate)
    
    # Print results
    print("T-statistic:", t_stat_for_two_groups_states)
    print("p-value:", p_value_for_two_groups_states)