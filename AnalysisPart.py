#!/usr/bin/env python
# coding: utf-8

# # Usefull library
# 

# In[46]:


import pandas as pd # use for data manipulation
import numpy as np # use for mathematical thing 
import matplotlib.pylab as plt # use for graph
import seaborn as sns # use for visualization 
import datetime


# # Loading the data 

# In[47]:


data=pd.read_csv("D://Project1//Data//311_Service_Requests_from_2010_to_Present.csv",low_memory=False)


# In[48]:


data.shape
#we have364558 row and 53 clm 


# In[4]:


data.dtypes


# # Formating of data

# In[5]:


#change the data type of some variable 
#Created Date                       object to date
#Closed Date                        object to date
#Due Date                           object to date
#Resolution Action Updated Date     object to date 


# In[49]:


data["Created Date"]=data["Created Date"].astype('datetime64')
data["Closed Date"]=data["Closed Date"].astype('datetime64')
data["Due Date"]=data["Due Date"].astype('datetime64')
data["Resolution Action Updated Date"]=data["Resolution Action Updated Date"].astype('datetime64')


# In[50]:


data.dtypes


# # Feature Selection

# In[59]:


data.drop(["Incident Zip","Unique Key","Agency","Incident Address","Location","Street Name","Community Board","Borough","Agency Name","Cross Street 1","Cross Street 2","Facility Type","Landmark","Intersection Street 1","Intersection Street 2","Address Type","Park Facility Name","School Name","School Number","School Region","School Code","School Phone Number","School Address","School City","School State","Descriptor","School Zip","School Not Found","School or Citywide Complaint"],axis=1,inplace=True)
#Thse Are unusefull data for us 


# # Null Value

# In[60]:


data.isnull().sum()

# if data is in numerical form so we have to replace data with mean or median , else go with mode
Closed Date                         2381# i think i have to delete the entire row bcz we want time period 
City                                2997
Due Date                               3
Resolution Action Updated Date      2402
X Coordinate (State Plane)          4030
Y Coordinate (State Plane)          4030
Vehicle Type                      364558 # remove
Taxi Company Borough              364558 # remove
Taxi Pick Up Location             364558 # remove
Bridge Highway Name               364261 # remove 
Bridge Highway Direction          364261 # remove
Road Ramp                         364296 # remove 
Bridge Highway Segment            364296 # remove
Garage Lot Name                   364558 # remove
Ferry Direction                   364557 # remove
Ferry Terminal Name               364556 # remove
Location                            4030
# In[61]:


data.drop(["Vehicle Type","Taxi Company Borough","Taxi Pick Up Location","Bridge Highway Name","Bridge Highway Direction","Road Ramp","Bridge Highway Segment","Garage Lot Name","Ferry Direction","Ferry Terminal Name"],axis=1,inplace=True)


# In[62]:


data.shape


# In[63]:


data.isnull().sum()


# In[64]:


ClosedDate_null=data[data['Closed Date'].isnull()].index.tolist()


# In[65]:


data.drop(ClosedDate_null,axis=0,inplace=True)


# In[66]:


data.isnull().sum()


# In[81]:


data.isnull().sum()


# In[78]:


data.shape


# In[82]:



xnull=data[data["X Coordinate (State Plane)"].isnull()].index.tolist()


# In[83]:


data.drop(xnull,axis=0,inplace=True)


# In[84]:


data.isnull().sum()


# In[86]:


locationnull=data[data["Location Type"].isnull()].index.tolist()


# In[90]:


data.drop(locationnull,axis=0,inplace=True)


# In[91]:


data.isnull().sum()


# In[92]:


citynull=data[data["City"].isnull()].index.tolist()


# In[94]:


data.drop(citynull,axis=0,inplace=True)


# In[95]:


data.isnull().sum()


# In[96]:


ResolutionActionUpdatedDatenull=data[data["Resolution Action Updated Date"].isnull()].index.tolist()


# In[97]:


data.drop(ResolutionActionUpdatedDatenull,axis=0,inplace=True)


# In[98]:


data.isnull().sum()


# In[99]:


data["City"].value_counts()


# In[114]:


data["City"].value_counts().plot(kind="pie",autopct="%1.1f")
#MAx from Brookyn


# # 1st Bsiness Moment or Measure Of Central Tredency  

# In[102]:


data["Location Type"].value_counts()


# In[101]:


data.mode()


# # Unique Value 
# 

# In[103]:


data["Complaint Type"].unique()


# In[104]:


data["Location Type"].unique()


# In[105]:


data.groupby(["Complaint Type","City"]).size()


# In[106]:


pd.crosstab(data["Complaint Type"],data["City"])


# In[107]:


pd.crosstab(data["Complaint Type"],data["City"]).plot(kind="bar",figsize=(25,15),label=40, stacked = True)


# In[119]:


df_Brooklyn = data[data['City']=='BROOKLYN']
df_Brooklyn


# In[121]:


df_Newyork = data[data['City']=='NEW YORK']
df_Newyork


# In[122]:


df_Bronx = data[data['City']=='BRONX']
df_Bronx


# In[120]:


(df_Brooklyn['Complaint Type'].value_counts()).head().plot(kind='bar',
                                                    figsize=(10,6),title = 'Most Frequent Complaints in Brooklyn')


# In[123]:


(df_Newyork['Complaint Type'].value_counts()).head().plot(kind='bar',
                                                    figsize=(10,6),title = 'Most Frequent Complaints in Newyork')


# In[124]:


(df_Bronx['Complaint Type'].value_counts()).head().plot(kind='bar',
                                                    figsize=(10,6),title = 'Most Frequent Complaints in Bronx')


# # Top 10 complaint types

# In[125]:


data["Complaint Type"].value_counts().head(10)


# In[126]:


data["Complaint Type"].value_counts().head(10).plot(kind="bar")


# # bar graph of count vs. complaint types

# In[127]:


data["Complaint Type"].value_counts().plot(kind="bar")


# In[128]:


data["Complaint Type"].value_counts().plot(kind="pie",autopct="%1.1f")


# In[129]:


data.groupby(["Complaint Type"]).size().plot(kind="bar")


# In[130]:


pd.crosstab(data["Complaint Type"],data["Location Type"]).plot(kind="bar",figsize=(25,15),label=40, stacked = True)


# In[131]:


data["TimePeriod"]=data["Closed Date"]-data["Created Date"]


# In[132]:


data["TimePeriod"]


# In[142]:


data.groupby("Complaint Type")["TimePeriod"].max()


# In[143]:


data.groupby("Complaint Type")["TimePeriod"].min()


# In[149]:



df_Bronx.plot(kind='hexbin', x='Longitude', y='Latitude', gridsize=40,
    colormap = 'jet',mincnt=1,title = 'Max Compalin In Bronx', figsize=(10,6)).axis('equal')


# In[ ]:




