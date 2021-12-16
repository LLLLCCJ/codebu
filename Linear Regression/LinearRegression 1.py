#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score
from sklearn.metrics import mean_absolute_error
from sklearn import preprocessing


# In[2]:


dummy_data=pd.read_csv("C:/Users/cod/Desktop/train-data.csv")


# In[3]:


dummy_data


# In[4]:


print('row 수 : {}, col 수 : {}'.format(dummy_data.shape[0],dummy_data.shape[1]))


# In[5]:


dummy_data.shape


# In[6]:


clean_data=dummy_data.copy(deep=True)


# In[7]:


clean_data


# In[8]:


clean_data.dropna('index').shape


# In[9]:


clean_data.dropna()


# In[10]:


print(clean_data.New_Price.isna().sum())


# In[11]:


clean_data.drop(columns=['Unnamed: 0','New_Price'], inplace = True)


# In[12]:


clean_data


# In[13]:


clean_data.dropna(("index"),inplace=True)


# In[14]:


clean_data


# In[15]:


clean_data.reset_index(drop=True,inplace=True)


# In[16]:


clean_data


# In[17]:


len(np.unique(list(clean_data.Name)))


# In[18]:


names=list(clean_data.Name)


# In[19]:


names


# In[20]:


for i in range(len(names)):
    names[i]=names[i].split(' ',1)[0]


# In[21]:


names


# In[22]:


clean_data.Name=names


# In[23]:


clean_data.head()


# In[24]:


len(np.unique(list(clean_data.Name)))


# In[25]:


mileage = list(clean_data.Mileage)
engine = list(clean_data.Engine)
power = list(clean_data.Power)


# In[26]:


for i in range(len(names)):
    mileage[i]=mileage[i].split(' ',1)[0]
    engine[i]=engine[i].split(' ',1)[0]
    power[i]=power[i].split(' ',1)[0]


# In[27]:


clean_data.Mileage=mileage
clean_data.Engine=engine
clean_data.Power=power


# In[28]:


clean_data.head()


# In[29]:


clean_data.dtypes


# In[30]:


clean_data["Price"] = clean_data["Price"].astype(float)
clean_data["Kilometers_Driven"] = clean_data["Kilometers_Driven"].astype(float)
clean_data["Mileage"] = clean_data["Mileage"].astype(float)
clean_data["Engine"] = clean_data["Engine"].astype(float)


# In[31]:


clean_data.dtypes


# In[32]:


np.unique(list(clean_data.Name))


# In[33]:


np.unique(clean_data.Location)


# In[34]:


np.unique(clean_data.Year)


# In[35]:


np.unique(clean_data.Fuel_Type)


# In[36]:


np.unique(clean_data.Owner_Type)


# In[37]:


np.unique(clean_data.Seats)


# In[38]:


clean_data=clean_data[clean_data.Seats != 0]


# In[39]:


clean_data.Seats


# In[40]:


clean_data.shape


# In[41]:


np.unique(clean_data.Power) #null


# In[45]:


idx=[]
It = list(clean_data.Power)
for i in range(len(It)):
    if(It[i]=='null'):
        idx.append(i)
clean_data.drop(idx,inplace=True)
clean_data.reset_index(drop = True,inplace=True)


# In[46]:


np.unique(clean_data.Power)


# In[48]:


clean_data.Power = clean_data.Power.astype(float)


# In[49]:


np.unique(clean_data.Power)


# In[50]:


clean_data.Year = pd.Categorical(clean_data['Year'])
clean_data.Seats = pd.Categorical(clean_data["Seats"])


# In[51]:


clean_data


# In[52]:


clean_data.dtypes


# In[53]:


clean_data.columns


# In[54]:


clean_data=pd.get_dummies(clean_data, prefix_sep='_', drop_first = True)


# In[55]:


clean_data


# In[56]:


clean_data.columns


# In[57]:


clean_data.dtypes


# In[58]:


clean_data.shape


# In[59]:


fig, ax = plt.subplots(1,5, figsize=(16,4))
ax[0].boxplot(clean_data.Kilometers_Driven)
ax[0].set_title("Kilometers Driven")

ax[1].boxplot(clean_data.Mileage)
ax[1].set_title("Mileage")

ax[2].boxplot(clean_data.Engine)
ax[2].set_title("Engine")

ax[3].boxplot(clean_data.Power)
ax[3].set_title("Power")

ax[4].boxplot(clean_data.Price)
ax[4].set_title("Price")

plt.show()


# In[60]:


sns.pairplot(data=clean_data, x_vars=['Kilometers_Driven','Mileage','Engine','Power'], y_vars='Price',size=3)


# In[61]:


idx=[]
x=list(clean_data.Kilometers_Driven)
for i in range(len(x)):
    if x[i]>6000000:
        idx.append(i)


# In[62]:


clean_data.drop(idx,inplace=True)


# In[63]:


fig, ax = plt.subplots(1,5, figsize=(16,4))
ax[0].boxplot(clean_data.Kilometers_Driven)
ax[0].set_title("Kilometers Driven")

ax[1].boxplot(clean_data.Mileage)
ax[1].set_title("Mileage")

ax[2].boxplot(clean_data.Engine)
ax[2].set_title("Engine")

ax[3].boxplot(clean_data.Power)
ax[3].set_title("Power")

ax[4].boxplot(clean_data.Price)
ax[4].set_title("Price")

plt.show()


# In[64]:


sns.pairplot(data=clean_data,x_vars=['Kilometers_Driven','Mileage','Engine','Power'],y_vars='Price')


# In[65]:


y = clean_data[['Price']].to_numpy()
clean_data.drop(columns=['Price'],inplace=True)


# In[66]:


x = clean_data.values


# In[67]:


x


# In[68]:


columns = clean_data.columns
scaler = preprocessing.MinMaxScaler()


# In[69]:


columns


# In[70]:


tmp = scaler.fit_transform(x)
clean_data = pd.DataFrame(tmp)


# In[71]:


clean_data


# In[72]:


clean_data.columns = columns
x = clean_data.to_numpy()


# In[73]:


x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.85, random_state = 1)


# In[74]:


train_test_split(x,y,train_size=0.85, random_state = 1)


# In[77]:


lr = LinearRegression(fit_intercept=True, normalize=True,copy_X=True)
lr.fit(x_train,y_train)


# In[78]:


print('Train dats\'s Accuracy : ', format(lr.score(x_train,y_train)))


# In[79]:


y_predict = lr.predict(x_test)


# In[80]:


print('Test dats\' Accuracy', format(lr.score(x_test,y_test)))
print('Test dats\' Accuracy', format(r2_score(y_test,lr.predict(x_test))))


# In[81]:


mean_absolute_error(y_test,y_predict)


# In[ ]:




