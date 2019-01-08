
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np 

weather_Df = pd.read_csv('C:/Users/Mahsa/Desktop/data science/ann/2013-AnnArbor-WeatherStats.txt', sep=',')
weather_Df.head(3)

issues_Df = pd.read_csv('C:/Users/Mahsa/Desktop/data science/ann/Improve_Detroit__Submitted_Issues.txt', sep=',')
issues_Df.head(3)

crash_Df = pd.read_csv('C:/Users/Mahsa/Desktop/data science/ann/MTCF Ann Arbor Crash Data.txt', sep=',')
crash_Df.head(3)
#crashs and weather
#issues reported and weather what is the relation between these lets figure out

#may be we don't need day of week because we can figure out on our own but still I keep it because I don't want to add another
#calculation ,
#Since column headers have extra space I want to strip each header first
#first attempt was crash_Df.columns.str.strip() which didn't work and with several tries I noticed that i should assigne the
#results to crash_Df.columns

#crash_Df.rename(columns=lambda x: x.strip())
crash_Df.columns=crash_Df.columns.str.strip()
crash_columns_todrop= ['Accident Month','Accident Day','Accident Year','Day','DateYYYYMMDD']

#I wanted to drop columns, I selected column names, first attempt was crash_Df.drop(crash_columns_todrop,inplace=True)
#which didn't work, noticed I should add columns= to parameter like crash_Df.drop(columns=crash_columns_todrop,inplace=True)
#yay it worked.

crash_Df.drop(columns=crash_columns_todrop,inplace=True)
dfgroup= crash_Df.groupby('DateDDMMYYYY').groups
#now what I want to do is to check inside each group

