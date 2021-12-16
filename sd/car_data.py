#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


pre_data = pd.read_csv("C:/Users/cod/Desktop/train-data.csv",index_col=0)


# In[3]:


pre_data


# In[4]:


refined_data = pre_data.copy(deep=True)


# In[5]:


refined_data.head()


# In[6]:


refined_data.drop(["Name","Location","Year","Fuel_Type","Transmission","Owner_Type","Mileage","Power","Engine","Seats","New_Price"],axis=1,inplace=True)


# In[7]:


refined_data.head()


# In[8]:


refined_data.isnull().sum()


# In[9]:


refined_data.dropna(inplace=True)


# In[10]:


refined_data.shape


# In[11]:


columns=list(refined_data.columns)


# In[12]:


for i in range(len(columns)):
    columns[i]=columns[i].split('_',1)[0]


# In[13]:


refined_data.columns=columns


# In[14]:


refined_data


# In[15]:


refined_data.dtypes


# In[16]:


refined_data.Kilometers=refined_data.Kilometers.astype("float")


# In[17]:


refined_data.dtypes


# In[18]:


kilometers=refined_data.Kilometers.values
price=refined_data.Price.values


# In[19]:


fig, ax = plt.subplots(1,2,figsize=(16,4))

ax[0].plot(kilometers,'o')
ax[0].set_title('kilometers')

ax[1].plot(price,'o')
ax[1].set_title('price')

plt.show()


# In[20]:


check=[]
for i in range(len(kilometers)):
    if kilometers[i]>400000:
        check.append(i)
for i in range(len(price)):
    if price[i]>150:
        check.append(i)


# In[21]:


check


# In[22]:


refined_data.drop(check,inplace=True)
kilometers=refined_data.Kilometers.values
price=refined_data.Price.values


# In[23]:


fig, ax = plt.subplots(1,2,figsize=(10,4))

ax[0].plot(kilometers,'o')
ax[0].set_title('kilometers')

ax[1].plot(price,'o')
ax[1].set_title('price')

plt.show()


# In[24]:


plt.plot(kilometers,price,'o')
plt.show()


# In[25]:


refined_data


# In[26]:


refined_data=refined_data.reset_index()


# In[28]:


refined_data.drop(refined_data.iloc[:,[0]],axis=1,inplace=True)


# In[29]:


refined_data


# In[ ]:




