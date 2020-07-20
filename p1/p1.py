import datetime as dt                  #for use datetime
import matplotlib.pyplot as pyplot     #for charts
from matplotlib import style           #for chart styles
import pandas as pd                    #data analysis library
import pandas_datareader.data as web   #grab data from yahoo api return pandas datafream

style.use('ggplot')                    #plot styles look for more!

start = dt.datetime(2000,1,1)          #starting date for selection
end = dt.datetime(2015,1,1)            #end date for selection

data_frame = web.DataReader('TSLA','yahoo',start,end) 
"""
use datareader to get data with 
api using pandas_datareader.  
collect them in data frame
"""

print(data_frame.head())    #shows first 5 coloums data
# print(data_frame.head(8))    #shows first 8 coloums data
# print(data_frame.tail())    #shows last 5 coloums data