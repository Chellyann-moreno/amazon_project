import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import yfinance as yf
from scipy.stats import pearsonr
import talib

# ------------------------------------------- EXPLORATION TIME!!!!! -----------------------------------------------------------------




#  ----------------------------------------- QUESTIONS 1 & 2  -----------------------------------------------------------------------
def question_1_2(train):

    # Calculate yearly mean
    yearly_mean = train['adjusted_close'].resample('Y').mean()

    # Plotting
    plt.figure(figsize=(10, 6))
    yearly_mean.plot(label='Yearly Mean', marker='o', linestyle='-', color='blue')
    
    plt.xlabel('Year')
    plt.ylabel('Adjusted Close Price (Mean)')
    plt.title('Yearly Mean of Amazon Stock Price (1999-2023)')
    plt.legend()
    plt.grid(True)
    
    plt.show()

# ----------------------------------------------------- QUESTION 3  ---------------------------------------------------------------- 
    
    
def question_3_month(train, month):
    # Filter the DataFrame for the selected month across all years
    selected_month_data = train[train.index.month == month]

    # Check if data is available for the selected month
    if selected_month_data.empty:
        print(f"No data available for the selected month {month}.")
        return

    # Plotting
    plt.plot(selected_month_data.index, selected_month_data['adjusted_close'], label=f'Amazon Stock Price in {month}')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.title(f'Amazon Stock Price Trends in {month} (1999-2023)')
    plt.legend()
    plt.show()

    # Print message about patterns during the selected month
    print(f"Observing patterns during the month of {month}.")
    
def question_3_months(train, months):
    # Filter the DataFrame for the selected months across all years
    selected_months_data = train[train.index.month.isin(months)]

    # Check if data is available for the selected months
    if selected_months_data.empty:
        print(f"No data available for the selected months {months}.")
        return

    # Plotting
    for month in months:
        month_data = selected_months_data[selected_months_data.index.month == month]
        plt.plot(month_data.index, month_data['adjusted_close'], label=f'Amazon Stock Price in {month}')

    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.title(f'Amazon Stock Price Trends in {", ".join(map(str, months))} (1999-2023)')
    plt.legend()
    plt.show()

#  ------------------------------------------- QUESTION 4  --------------------------------------------------------------------------
def question_4(train):
    # Calculate overall standard deviation
    overall_volatility = train['adjusted_close'].std()

    # Calculate standard deviation for specific periods (e.g., yearly)
    yearly_volatility = train['adjusted_close'].resample('Y').std()

    # Calculate rolling standard deviation with a window of 30 days
    rolling_volatility = train['adjusted_close'].rolling(window=30).std()

    # Calculate percentage change
    percentage_change = train['adjusted_close'].pct_change()

    # Analyze distribution of percentage changes
    descriptive_stats = percentage_change.describe()

    # Plot rolling volatility
    plt.figure(figsize=(10, 6))
    plt.plot(rolling_volatility.index, rolling_volatility, label='Rolling Volatility (30 days)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.title('Rolling Volatility of Amazon Stock Price')
    plt.legend()
    plt.show()

    return print(descriptive_stats)

 # ------------------------------------------------- QUESTION 5  --------------------------------------------------------------------

def question_5(train, month, year):

    # Filter the DataFrame for the selected month and year
    selected_month_data = train[(train.index.month == month) & (train.index.year == year)]

    # Check if data is available for the selected month and year
    if selected_month_data.empty:
        print(f"No data available for the selected month {month} and year {year}.")
        return

    # Plotting with adjusted figure size
    plt.figure(figsize=(10, 6))

    plt.plot(selected_month_data.index, selected_month_data['adjusted_close'],
             label=f'Amazon Stock Price in {month}/{year}')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.title(f'Amazon Stock Price Trends in {month}/{year}')
    plt.legend()

    plt.xticks(selected_month_data.index[::2], rotation=45)

    plt.show()

