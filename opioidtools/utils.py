# Standard numerical analysis imports
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

def viz(df, col_name):
    """creates pointplot of column for each state in dataframe
    Parameters
    ----------
    df: dataframe
        The dataframe with a column of states, 'State', and a numeric column
    col_name: str
        The numeric column to plot as the y-value
        """
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
            axs[row,col].set_ylim(0,(max(df[col_name])//5+1)*5)
    plt.savefig('figures/'+col_name)
    plt.show()

def vis_avg_gdp_for_each_state(df):
    """plots the average GDP from 2010-2014 for each state in dataframe
    Parameters
    ----------
    df: dataframe
        The dataframe containing the average GDP for each state
        """
    # Sorted the data to make the graph clearer
    df = df.sort_values(ascending=False)

    # Plot the data
    plt.figure(figsize=(6,10))
    plt.barh(df.index, df.values)
    plt.xlabel('Average GDP')
    plt.ylabel('States')
    plt.title('Average GDP Value for Each State over 2010-2014')
    plt.savefig('figures/'+'Avg_GDP_for_Each_State_Over_Years')
    plt.show()
    
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

def vis_two_avg_gdp_states(df, state1, state2):
    """plots the average GDP of 2 states for 2010-2014
    Parameters
    ----------
    df: dataframe
        The dataframe containing the average GDP for the two states
    state1: str
        The first state to plot
    state2: str
        The second state to plot
    """
    # Select the two states to plot plotting
    gdp_state1 = df[(df["State"] == state1)][["Year", "GDP_0101"]]
    gdp_state2 = df[(df["State"] == state2)][["Year", "GDP_0101"]]
    
    # Create a line plot of the GDP over years for the two states
    plt.plot(gdp_state1["Year"], gdp_state1["GDP_0101"], label= state1)
    plt.plot(gdp_state2["Year"], gdp_state2["GDP_0101"], label= state2)
    plt.xlabel("Year")
    plt.ylabel("GDP")
    plt.title("GDP over Years for {} and {}".format(state1, state2))

    # x ticks format
    years = df["Year"].unique()
    plt.xticks(list(range(int(years.min()), int(years.max())+1)))
    
    plt.legend()
    plt.savefig('figures/'+'Two_Avg_GDP_States')
    plt.show()
    
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