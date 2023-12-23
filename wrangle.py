import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import talib




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

    return df

    
    
    
    
# Retrieve combined document
def get_amzn(file_path='/Users/chellyann/my_repos/amazon_project/working docs/combined_amzn.csv'):
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)\
          .rename_axis('date')\
          .rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low',
                           'Close': 'close', 'Adj Close': 'adjusted_close', 'Volume': 'volume'})\
          .round(2)

    return df

#Train/Test Split TSA

def train_test_split(df):
    train_size = 0.70 
    n = df.shape[0] 
    test_start_index = round(train_size * n) 
    train = df.iloc[:test_start_index].copy()  # Make a copy to avoid SettingWithCopyWarning
    test = df.iloc[test_start_index:].copy()  # Make a copy to avoid SettingWithCopyWarning

    # Set the datetime index for train and test
    train.index = pd.to_datetime(train.index)
    test.index = pd.to_datetime(test.index)
    
    # Calculate SMA for 'sma_50' column
    train['sma_50'] = talib.SMA(train['close'], timeperiod=50)
    test['sma_50'] = talib.SMA(test['close'], timeperiod=50)

    # Calculate 14-day Relative Strength Index (RSI) for 'rsi_14' column
    train['rsi_14'] = talib.RSI(train['close'], timeperiod=14)
    test['rsi_14'] = talib.RSI(test['close'], timeperiod=14)

    # Save train and test to CSV
    train.to_csv('train.csv')
    test.to_csv('test.csv')
    
    return train, test

def read_train_test():
    train = pd.read_csv('train.csv', index_col=0, parse_dates=True)
    test = pd.read_csv('test.csv', index_col=0, parse_dates=True)
    
    return train, test

def plotting_train_test(train,test):
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
    

    