import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns




#----------LET'S GET READY TO WRANGLE-------


def create_combined_file():
    # Read the CSV files
    df1 = pd.read_csv('AMZN_data.csv', index_col=0)
    df2 = pd.read_csv('AMZN_2023.csv', index_col=0)

    # Combine DataFrames while preserving the original indices
    combined_df = pd.concat([df1, df2], ignore_index=False)

    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv('combined_amzn.csv')

    # Read the combined CSV file into a DataFrame
    df = pd.read_csv('combined_amzn.csv', index_col=0)

    return df.head(3)

    
    
    
    
# Retrieve combined document
def get_amzn():
    df = pd.read_csv('combined_amzn.csv', index_col=0, parse_dates=True)\
          .rename_axis('date')\
          .rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low',
                           'Close': 'close', 'Adj Close': 'adjusted_close', 'Volume': 'volume'})\
          .round(2)

    return df.head()

#Train/Test Split TSA

def train_test_split(df):
    train_size = 0.70 
    n = df.shape[0] 
    test_start_index = round(train_size * n) 
    train = df.iloc[:test_start_index]  # end at the test_start_index
    test = df.iloc[test_start_index:]  # start at the test_start_index
    
    # Plotting
    plt.plot(train.index, train.adjusted_close, label='Train')
    plt.plot(test.index, test.adjusted_close, label='Test')
    
    # Adding labels and legend
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.title('Train-Test Split of Adjusted Close Prices')
    plt.legend()
    
    # Display the plot
    plt.show()

    