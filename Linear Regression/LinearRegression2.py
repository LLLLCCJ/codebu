#!/usr/bin/env python
# coding: utf-8

# In[37]:


import matplotlib.pyplot as plt
import numpy as np


# In[46]:


x=np.random.rand(20,1)
y=5*x+2


# In[47]:


x


# In[48]:


plt.scatter(x,y)
print(x,y)
plt.show()


# In[49]:


x=np.random.rand(20,5)
x*=10
y=5*x+10
plt.scatter(x,y)
print(x,y)
plt.show()


# In[50]:


from sklearn.linear_model import LinearRegression
import sklearn


# In[51]:


x=np.random.rand(20,1)
x*=10
y=5*x+10
model = LinearRegression()
model.fit(x,y)
print('기울기 a :',model.coef_)
print('y절편 b',model.intercept_)
print('\n')


# In[45]:


x=np.random.rand(20,1)
x*=10
y=5*x+10
y+=3*np.random.rand(20,1)
model = LinearRegression()
model.fit(x,y)
y_p = model.predict(x)
print('기울기 a :',model.coef_)
print('y절편 b',model.intercept_)
plt.scatter(x,y,marker='x')
plt.scatter(x,y_p,marker='o')
plt.show()


# In[52]:





# In[ ]:




