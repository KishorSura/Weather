#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[104]:


df=pd.read_csv("C:/Users/DELL/Desktop/1. Weather Data.csv",parse_dates=["Date/Time"])
df.head()


# In[17]:


df.info()


# In[18]:

# describes the table 
df.describe()


# In[19]:

#prints number of rows and columns
df.shape


# In[20]:

#prints the column names
df.columns


# In[21]:

#Index range
df.index


# In[22]:

#type of each column
df.dtypes


# In[24]:


df["Weather"].unique()


# In[25]:

#finds uniques values
df.nunique()


# In[26]:

#count of rows
df.count()


# In[31]:

#count the different values in the rescpective column
df["Weather"].value_counts()


# In[32]:


#find the unique values of windspeed


# In[35]:


df["Wind Speed_km/h"].unique()


# In[36]:


# to count the unique values 
df["Wind Speed_km/h"].nunique()


# In[63]:


#find the number of times when the "weather is exactly clear"
df["Weather"][df["Weather"]=="Clear"].count()


# In[64]:


df["Weather"].value_counts()


# In[78]:


df.groupby("Weather").get_group("Clear").count()


# In[79]:


#Number of times the windspeed was extractly 4 kmph 
df.head(2)


# In[87]:


df["Wind Speed_km/h"][df["Wind Speed_km/h"]==4].count()


# In[88]:


#Null values
df.isnull().sum()


# In[89]:


df.notnull().sum()


# In[92]:


#To rename Weather column name to "Weather Condition"
new_df=df.rename(columns={"Weather":"Weather Condition"})
new_df


# In[93]:


# what is mean for "Visibilty"
df["Visibility_km"].mean()


# In[94]:


#What is standard deviation of pressure?
df["Press_kPa"].std()


# In[95]:


#What is Variance of relative humdity?
df["Rel Hum_%"].var()


# In[97]:


#Find the instance when snow is recorded?
df.head(2)


# In[105]:


df["Weather"][df["Weather"]=="Snow"].count()


# In[107]:


df["Weather"][df["Weather"]=="Snow"].value_counts()


# In[110]:


# when snow word is present
df[df["Weather"].str.contains("Snow")]


# In[121]:


#Find instance where windspeed is above 24 and visiblity is 25
df[(df["Wind Speed_km/h"]>=24) & (df["Visibility_km"]==25)].count()


# In[122]:


df[(df["Wind Speed_km/h"]>=24) & (df["Visibility_km"]==25)]


# In[123]:


#What is the mean value of each column against each weather condition.
df.groupby("Weather").mean()


# In[124]:


#What is the max and min value of each column against each weather condition.
df.groupby("Weather").max()


# In[125]:


df.groupby("Weather").min()


# In[127]:


#Show all condition where weather is fog 
df[df["Weather"]=="Fog"]


# In[128]:


#Find the all instance where weather is clear or visbilty is above 40 
df[(df["Weather"]=="Clear")|(df["Visibility_km"]>40)]


# In[129]:


#Find all instance where 
#Weather is clear and humdity is above 50 or
#visbilty is above 40 
df[((df["Weather"]=="Clear") & df["Rel Hum_%"]>50)|(df["Visibility_km"]>40)]


# In[ ]:




