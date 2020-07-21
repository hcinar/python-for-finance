import datetime as dt                  #for use datetime
import matplotlib.pyplot as plt     #for charts
from matplotlib import style           #for chart styles
import pandas as pd                    #data analysis library
import pandas_datareader.data as web   #grab data from yahoo api return pandas dataframe

style.use('ggplot')      #plot styles look for more!

def highest_alltime(data_frame):
    """ basic algorithm to get highest all time"""
    highest_alltime=-99
    for item in data_frame['High']:
        if item > highest_alltime:
            highest_alltime = item
            # print(highest_alltime
    print(highest_alltime)  
def getData(stockName):
    """
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame 
    use datareader to get data with 
    api using pandas_datareader.  
    collect them in data frame
    """
    start = dt.datetime(2000,1,1)          #starting date for selection
    end = dt.datetime(2020,7,14)            #end date for selection

    data_frame = web.DataReader(stockName,'yahoo',start,end)
    return data_frame
def getData_csv(stockName,csv_name):
    """
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame 
    use datareader to get data with 
    api using pandas_datareader.  
    collect them in data frame
    """
    start = dt.datetime(2000,1,1)          #starting date for selection
    end = dt.datetime(2020,7,14)            #end date for selection

    data_frame = web.DataReader(stockName,'yahoo',start,end)

    data_frame.to_csv(csv_name)      #data frame to csv file
    print(csv_name," is created!")  #info about job
def readData_fromcsv(csv_name):
    data_frame= pd.read_csv(csv_name,parse_dates=True,index_col=0)  # look for read_csv pandas. clear index in data frame, make date index
    return data_frame

# data_frame=getData('TSLA')     """get stock data with name to dataframe"""


# print(data_frame.head())    #shows first 5 coloums data
# # print(data_frame.head(8))    #shows first 8 coloums data
# # print(data_frame.tail())    #shows last 5 coloums 
# print(data_frame['High'].tail())
# highest_alltime(data_frame)   #to print highest all time

# getData_csv('TSLA','tsla.csv')     #get stock data and puts it into csv file

data_frame = readData_fromcsv('tsla.csv')      #look for read csv pandas.
""" pandas documentation look for that!"""
# print(data_frame['Volume'].head)    #shows first 5 coloums data

data_frame['Open'].plot()    #matplotlib usage for plotting data
plt.show()           #show plotting data at the screen.



