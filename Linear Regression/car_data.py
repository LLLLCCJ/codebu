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


pre_data.reset_index(inplace=True)


# In[31]:


pre_data.drop(pre_data.iloc[:,[0]],axis=1,inplace=True)


# In[6]:


refined_data = pre_data.copy(deep=True)


# In[7]:


refined_data.head()


# In[8]:


refined_data.drop(["Name","Location","Year","Fuel_Type","Transmission","Owner_Type","Mileage","Power","Engine","Seats","New_Price"],axis=1,inplace=True)


# In[9]:


refined_data.head()


# In[10]:


refined_data.isnull().sum()


# In[11]:


refined_data.dropna(inplace=True)


# In[12]:


refined_data.shape


# In[13]:


columns=list(refined_data.columns)


# In[14]:


for i in range(len(columns)):
    columns[i]=columns[i].split('_',1)[0]


# In[15]:


refined_data.columns=columns


# In[16]:


refined_data


# In[17]:


refined_data.dtypes


# In[18]:


refined_data.Kilometers=refined_data.Kilometers.astype("float")


# In[19]:


refined_data.dtypes


# In[20]:


kilometers=refined_data.Kilometers.values
price=refined_data.Price.values


# In[21]:


fig, ax = plt.subplots(1,2,figsize=(16,4))

ax[0].plot(kilometers,'o')
ax[0].set_title('kilometers')

ax[1].plot(price,'o')
ax[1].set_title('price')

plt.show()


# In[22]:


check=[]
for i in range(len(kilometers)):
    if kilometers[i]>400000:
        check.append(i)
for i in range(len(price)):
    if price[i]>150:
        check.append(i)


# In[23]:


check


# In[24]:


refined_data.drop(check,inplace=True)
kilometers=refined_data.Kilometers.values
price=refined_data.Price.values


# In[25]:


fig, ax = plt.subplots(1,2,figsize=(10,4))

ax[0].plot(kilometers,'o')
ax[0].set_title('kilometers')

ax[1].plot(price,'o')
ax[1].set_title('price')

plt.show()


# In[26]:


plt.plot(kilometers,price,'o')
plt.show()


# In[27]:


refined_data


# In[28]:


refined_data=refined_data.reset_index()


# In[29]:


refined_data.drop(refined_data.iloc[:,[0]],axis=1,inplace=True)


# In[30]:


refined_data


# In[ ]:




