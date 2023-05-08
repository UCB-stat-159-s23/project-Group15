import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats

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