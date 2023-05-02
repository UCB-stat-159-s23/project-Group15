import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def to_numeric(df, col_name):
    return pd.to_numeric(df[col_name])

def viz(df, col_name):
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

