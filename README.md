# Project Description: 
This project features a comprehensive dataset documenting Amazon Inc.'s historical stock performance from January 1, 1999, to December 20, 2023. Including daily records of open, high, low, close prices, and trading volumes, the dataset serves analysts, investors, and data enthusiasts for in-depth analyses, trend assessments, and predictive modeling specific to AMZN stock. With structured data points such as Date, Open, High, Low, Close, and Adjusted Close prices, researchers can explore historical trends, build predictive models, and study trading volumes. Users are encouraged to employ the dataset for research, education, and analytical purposes, attributing Yahoo Finance as the source and exercising caution in interpreting historical stock data for decision-making due to market complexities.







# Project Goals:
accurately forecaste both daily and quarterly adjusted close prices, enabling comprehensive comparison with real-time data for enhanced insights and decision-making in the realm of AMZN stock analysis.


# Inital Questions:
1. How has the overall trend in Amazon stock prices evolved over the entire period available in the dataset?
2. Are there any noticeable long-term patterns, upward or downward trends, and what factors might have contributed to these trends?
3. Are there any discernible seasonal patterns or cyclical trends in Amazon stock prices over different periods, such as months, quarters, or years?
4. How do key events or seasons (e.g., holiday seasons, earnings reports) correlate with fluctuations in stock prices?
5. How variable are Amazon stock prices over time, and has there been any significant change in volatility during specific periods?
6. Can you identify and analyze any major events (e.g., earnings announcements, market shifts, global events) that coincide with notable spikes or declines in volatility?
# Data Dictionary:
![Alt text](https://github.com/Chellyann-moreno/amazon_project/blob/main/working%20docs/Data_Dictionary.png)

# Project Planning, Layout of Science Pipeline:
## Acquire
- Acquire Dataset through [Finance Yahoo](https://finance.yahoo.com/quote/AMZN/history/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADoeU72IYcqoxMGsIB4K4K6DrF0HY2tYC81Ur_A5oKjlb7aCP8WOW7Nj_nOdmrDugB3pTDQV-tU2RIvWGC0AnigHJxy1FsKtZdY5WfrKAZHR00T-ln4Ck3XLGsW4IqW242K7qb-oSmwiA2qOLZUqnKVyrSeI0hrmRM9uJMoxo-ez)
- 6283 rows x 5 columns
## Prepare
- Clean the data
- Drop Columns
- Rename columns
- Remove nulls
- Split data (70/30)
## Explore
- Answer initial questions
- Utilized plotting methods for data visualization
- Explore impactful events throughout the timelines such as 9/11, the 2008 stock market drop, the Covid-19 pandemic, etc...
## Model
- Resampled Data Quarterly
- Perform various methods of predictions with machine learning: ARIMA, Polynomial Regression, OLS
- Accessed accuracy 

# Instructions on How to Reproduce this Project:

# Summary

# Takeaways:
