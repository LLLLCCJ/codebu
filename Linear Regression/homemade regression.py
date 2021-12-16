#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from car_data1 import refined_data


# In[2]:


#사용자 정의 data
#x=np.random.rand(1000,1)
#y=np.random.rand(1000,1)
#plt.scatter(x,y)
#chart=pd.DataFrame(x)
#chart.insert(1,'y',y)
#chart=chart.drop(0,axis=1)
#chart
#chart.insert(0,'x',x)


# In[3]:


#chart = refined_data


# In[4]:


chart


# In[5]:


columns=["x","y"]
chart.columns=columns


# In[6]:


chart['xy']=chart.x*chart.y


# In[7]:


chart


# In[8]:


chart.reset_index(inplace=True)


# In[9]:


chart


# In[10]:


chart.drop('index',axis=1,inplace=True)


# In[11]:


n=len(chart.iloc[:,0])
x=chart.x.values
y=chart.y.values
xsum=chart.x.sum()
ysum=chart.y.sum()
xSsum=np.square(chart.x).sum()
ySsum=np.square(chart.y).sum()
xysum=chart.xy.sum()
sig_xy=n*xysum-xsum*ysum
sig_x=np.sqrt(n*xSsum-xsum**2)
sig_y=np.sqrt(n*ySsum-ysum**2)


# In[12]:


r=sig_xy/(sig_x*sig_y)


# In[13]:


r


# In[14]:


np.square(r)


# In[15]:


coef=r*sig_y/sig_x


# In[16]:


coef


# In[17]:


y_bar=ysum/n
x_bar=xsum/n


# In[18]:


intercept=y_bar-coef*x_bar


# In[19]:


intercept


# In[20]:


def hommade_regression(x):
    yy=intercept+coef*x
    return yy


# In[21]:


plt.plot(x,y,'ro')
plt.plot(x,hommade_regression(x),'b-')


# In[22]:


hommade_regression(2.432)


# In[23]:


np.corrcoef(x, y)[0,1]


# In[24]:


np.square(np.corrcoef(x, y)[0,1])


# In[25]:


x=x.reshape(-1,1)


# In[ ]:





# In[26]:


model=LinearRegression()


# In[27]:


model.fit(x,y)


# In[28]:


model.coef_


# In[29]:


model.intercept_


# In[30]:


predict_value=model.predict([[2.432]])
plt.plot(x,y,'ro')
plt.plot(x,model.predict(x),'b-')
plt.show()


# In[31]:


predict_value


# In[ ]:




