
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
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

crash_Df.head(5)#lets see if it dropped the columns\


# In[108]:


dfgroup= crash_Df.groupby('DateDDMMYYYY')
#dfgroup.size().max()
#maxval= dfgroup

dfgroup.size().sort_values(ascending=False)


# In[109]:


weather_Df['EST'].is_unique
weather_Df.set_index('EST')
weather_Df.head(5)

#accessing row based on column valuse:
weather_Df.loc[weather_Df['EST'] == '1/31/2013']
weather_Df.columns=weather_Df.columns.str.strip()
weather_Df.columns
#based on columns questions could be asked are, which days was extremely windy? 
#which days visibility was poor?
#dfgroupbla = dfgroup['weight'].mean()
#now what I want to do is to check inside each group


# In[110]:


issues_Df.head(5)
issues_Df.columns


min(crash_Df['DateDDMMYYYY'])#1/1/2013
max(crash_Df['DateDDMMYYYY'])#9/9/2013

min(weather_Df['EST'])#'1/1/2013'
max(weather_Df['EST'])#'9/9/2013'

min(issues_Df['ticket_created_date_time'])#'01/01/2015 05:14:49 PM'
max(issues_Df['ticket_created_date_time'])#'12/31/2015 12:02:03 PM'

#after getting max and min of date columns noticed that issues is not connected to other two! so I need to dig into crash and
#weather. about issues_Df i can check dataset itself to see what can I get from it.


# In[111]:


#weather_Df.loc[('1/30/2013'< weather_Df['EST'] < '2/01/2013')]
#mask = (weather_Df['EST'] >= '1/30/2013') & (weather_Df['EST'] < '2/01/2013')
#weather_Df.loc[mask]
weather_Df.sort_values(by=['EST'], ascending=True)

weather_Df.columns #Min VisibilityMiles
weather_Df['Mean VisibilityMiles'].min()
weather_Df.sort_values(by=['Mean VisibilityMiles'], ascending=True)

weather_Df.columns
#weather_Df.columns remove spaces from columns names


# In[112]:


crash_Df['DateDDMMYYYY'] = pd.to_datetime(crash_Df['DateDDMMYYYY'])
crash_Df.head(5)
crash_Df.rename(columns={'DateDDMMYYYY': 'IndexDate'},inplace = True)
crash_Df
weather_Df.head(5)
weather_Df['EST']=pd.to_datetime(weather_Df['EST'])
weather_Df.rename(columns={'EST': 'IndexDate'},inplace = True)
weather_Df.head(5)
weather_Df.set_index('IndexDate',inplace=True)
crash_Df.set_index('IndexDate',inplace=True)
weather_Df.head(5)


# In[113]:



#merge them 
merge_Df= pd.merge(left=crash_Df, right=weather_Df,left_index=True, right_index=True, how="inner")
merge_Df.head(5)
mergGroups = merge_Df.groupby('IndexDate')
mergGroups.groups
mergGroups.size()
#time to draw a plot
merge_Df.columns
merge_Df['Road Conditions']
roadCond_groups = merge_Df.groupby('Road Conditions')
roadCond_groups.groups
roadCond_groups.size() #surprisingly when it is dry we have more accidents 
#after this line noticed that I need to make format of all dates same, like with zeros
#I googled alot but couldnot get any successful result
#yaaaay found an answer 
#it is important that to come to conclusion, all these datasets should be in same date range, unless we want to 


# In[116]:


#lets limit our data set to 1/1/2013 and 9/9/2013 <=== Actually no need for this because we already merged datasets 
test_Df = weather_Df
weatherTest= pd.read_csv('C:/Users/Mahsa/Desktop/data science/ann/2013-AnnArbor-WeatherStats.txt', sep=',')
weatherTest.head(3)
weatherTest['EST']= pd.to_datetime(weatherTest['EST'])
weatherTest.head(3)


weatherTest['EST'].min()
weatherTest['EST'].max()


# In[117]:


#Now it is time for playing with some plotting 


# In[118]:


#and questions like which day had the most crash and why 


# In[119]:


#what are the axis of the plot, weather , degree and crash?? dry and wet bar chart?? no first ask a questionm
merge_Df.columns #time of day is good, see which hours mostly crash happens (it is more like prove :D )
#which highway mostly crash happens (maybe it needs a repair)
#what is the weather column :)))
#which crash type happens in which weather
#don't see a need for crash type: 
#interesting GPS Coordinat
#to make sure merged dataset is within the specified date range, test
#which of the weathers result in fatal crash??
#what is events column?
#trim column names!



# In[2]:


highwayGroups= merge_Df.groupby('Highway Number')
highwayGroups.size()

timeGroups = merge_Df.groupby('Time Of Day')
timeGroups.size() #todo: it is a good practice to parse time of day and then categorize based on morning afternoon and night!!

weatherGroups= merge_Df.groupby('Weather')
weatherGroups.size()

merge_Df['Crash: Fatal Crash']
fatalGroups = merge_Df.groupby('Crash: Fatal Crash')
fatalGroups.size()

gpsGroups = merge_Df.groupby(['Gps X Coordinate', 'Gps Y Coordinate'])
gpsGroups.size().max() # which coordinate is this that has maximum crashes

eventGroups = merge_Df.groupby('Events')
eventGroups.size() #well this is little bit surprising if we compare it to the weather

#how to say among fatals how percent of them was snow weather!!
#merge_Df['IndexDate'].min()
crash_Df.groupby('IndexDate').size() #I thought with inner join I should get only date range between 1-1-2013 and 9-9-2013????

#how to get index between date Range
#slicedMerge = merge_Df.iloc['2013-01-01' : '2013-09-09'  ]
#slicedMerge['IndexDate']

#how to plot groupby result
#merge_Df.plot.line(x='Time Of Day', y='Weather')
#axes = merge_Df.plot.line(x='Time Of Day', y='Weather')
#merge_Df['Weather'].plot()


# In[11]:


import matplotlib.pyplot as plt
#merge_Df.plot(x='Mean Wind SpeedMPH',y='Mean VisibilityMiles',kind='scatter')
#merge_Df[['Mean Wind SpeedMPH']].plot().scatter
##plt.scatter(merge_Df['Time Of Day'], merge_Df['Crash: Fatal Crash'])
#plt.show()
#numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
#newdf = merge_Df.select_dtypes(include=numerics)
#,'Mean Wind SpeedMPH'
#newdf.columns

gpsGroups.size().plot()
#weatherGroups[['Gps X Coordinate', 'Gps Y Coordinate']].corr()
gpsGroups.size().max()
gpsGroups.filter(lambda x: x.count()>45)


# In[12]:


import matplotlib.pyplot as plt
merge_Df.plot(x='Mean Wind SpeedMPH',y='Mean VisibilityMiles')
merge_Df[['Mean Wind SpeedMPH']].plot()
#plt.scatter(merge_Df['Time Of Day'], merge_Df['Crash: Fatal Crash'])
plt.show()
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = merge_Df.select_dtypes(include=numerics)
#,'Mean Wind SpeedMPH'
newdf.columns


# In[13]:



eventGroups.count()['Time Of Day']
fig, ax = plt.subplots(figsize=(15,7))
gpsGroups.count()['Time Of Day'].plot(ax=ax)

#fig, ax = plt.subplots(figsize=(15,7))
# use unstack()
#gpsGroups.count()['Time Of Day'].unstack().plot(ax=ax)


# In[14]:



dayGroups= merge_Df.groupby('IndexDate')
dayGroups.size()
fig, ax = plt.subplots(figsize=(15,7))
dayGroups.count()['Time Of Day'].plot(ax=ax)


# In[15]:



crashdayGroup= crash_Df.groupby('IndexDate')
fig, ax = plt.subplots(figsize=(15,7))
crashdayGroup.count()['Weather'].plot(ax=ax)


# In[29]:



fig, ax = plt.subplots(figsize=(15,7))
weatherGroups.count()['Time Of Day'].unstack().plot(ax=ax)
#ask in stack overflow


# In[17]:


weatherGroups['Time Of Day'].size()


# In[18]:


weatherGroups['Time Of Day'].count()


# In[19]:


weather_Df.corr()


# In[20]:


monthgroups= merge_Df.groupby(['Month','Weather'])
monthgroups.size()


# In[21]:


fig, ax = plt.subplots(figsize=(15,7))
monthgroups.count()['Time Of Day'].unstack().plot(ax=ax)


# In[22]:


gpsweathergroups= merge_Df.groupby(['Gps X Coordinate', 'Gps Y Coordinate','Weather'])
gpsweathergroups.size()


# In[23]:


fig, ax = plt.subplots(figsize=(15,7))
gpsweathergroups.count()['Time Of Day'].unstack().plot(ax=ax)


# In[24]:


merge_Df.columns


# In[25]:


dayweathergroups=merge_Df.groupby(['Day Of Week', 'Weather'])
dayweathergroups.size()

fig, ax = plt.subplots(figsize=(15,7))
dayweathergroups.count()['Time Of Day'].unstack().plot(ax=ax)
#need to show monday, friday and etc on the plot


# In[26]:


dayweathergroups=merge_Df.groupby(['Weather','Day Of Week'])
dayweathergroups.size()

#thanks to https://scentellegher.github.io/programming/2017/07/15/pandas-groupby-multiple-columns-plot.html finally I plotted groupbys

fig, ax = plt.subplots(figsize=(15,7))
dayweathergroups.count()['Time Of Day'].unstack().plot(ax=ax) #it is important which column is first at groupby


# In[27]:


#now what can I select instead of gps x and gps y, because values of these two are too detailed that you can make decision only
#for the amounts that are too high or too low.

crashweathergroups= merge_Df.groupby(['Crash Type','Weather'])
crashweathergroups.size()
fig, ax = plt.subplots(figsize=(15,7))
crashweathergroups.count()['Time Of Day'].unstack().plot(ax=ax)


# In[28]:


citymonthgroups= merge_Df.groupby(['County','Month'])
citymonthgroups.size()

