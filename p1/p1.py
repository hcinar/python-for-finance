import datetime as dt                  #for use datetime
import matplotlib.pyplot as pyplot     #for charts
from matplotlib import style           #for chart styles
import pandas as pd                    #data analysis library
import pandas_datareader.data as web   #grab data from yahoo api return pandas datafream


def highest_alltime(data_frame):
    """ basic algorithm to get highest all time"""
    highest_alltime=-99
    for item in data_frame['High']:
        if item > highest_alltime:
            highest_alltime = item
            # print(highest_alltime
    print(highest_alltime)
    """ basic algorithm to get highest all time"""  


style.use('ggplot')                    #plot styles look for more!

start = dt.datetime(2000,1,1)          #starting date for selection
end = dt.datetime(2020,7,14)            #end date for selection

data_frame = web.DataReader('TSLA','yahoo',start,end)   
"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame 
use datareader to get data with 
api using pandas_datareader.  
collect them in data frame
"""

print(data_frame.head())    #shows first 5 coloums data
# print(data_frame.head(8))    #shows first 8 coloums data
# print(data_frame.tail())    #shows last 5 coloums 
print(data_frame['High'].tail())
highest_alltime(data_frame)   #to print highest all time


