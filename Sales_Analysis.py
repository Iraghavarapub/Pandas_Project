#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import os


# # Merge all the sales files in a CSV file
# 

# In[116]:


files = [file for file in os.listdir('./Documents/Pandas/Sales_Data')]
pd.DataFrame(files)
all_months_data= pd.DataFrame()
for file in files:
    df = pd.read_csv("./Documents/Pandas/Sales_Data/"+file)
    all_months_data= pd.concat([all_months_data, df])
    all_months_data.to_csv('all_data.csv', index='false')


# ## Add a Column

# In[117]:


all_months_data['Month'] = all_months_data['Order Date'].str[0:2]


# ## Cleaning Data

# # Drop rows with NaN
# 

# In[118]:


all_months_data=all_months_data.dropna(axis='index',how='all')
all_months_data.head()


# In[119]:


all_months_data=all_months_data[all_months_data['Order Date'].str[0:2]!='Or']
all_months_data.head()


# In[120]:


all_months_data.head()


# # Task 1: The best month in sales

# In[122]:


all_months_data['Price Each']=pd.to_numeric(all_months_data['Price Each'])
all_months_data['Quantity Ordered']=pd.to_numeric(all_months_data['Quantity Ordered'])


# In[123]:


all_months_data['Sales']=all_months_data['Quantity Ordered']*all_months_data['Price Each']
all_months_data.head()


# In[124]:


results=all_months_data.groupby('Month').sum()


# In[125]:


import matplotlib.pyplot as plt
month = range(1,13)
plt.bar(month,results['Sales'])
plt.xticks(month)
plt.xlabel('Months')
plt.ylabel('Sales in USD')
plt.show()


# # Task 2: Which city sold the most product

# In[127]:


def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]


all_months_data['City']=all_months_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")
all_months_data.head()


# In[143]:


results=all_months_data.groupby('City').sum()
results.head(10)


# In[147]:


import matplotlib.pyplot as plt
city = all_months_data['City'].unique()
cities=[city for city, df in all_months_data.groupby('City')]
plt.bar(cities,results['Sales'])
plt.xticks(cities,rotation='vertical',size=8)
plt.xlabel('City')
plt.ylabel('Sales in USD')
plt.show()


# # Task 3: The best time to send advertisement to customers for maximum sales
# 

# In[149]:


all_months_data['Order Date']=pd.to_datetime(all_months_data['Order Date'])
all_months_data.head()


# In[152]:


all_months_data['hour']=all_months_data['Order Date'].dt.hour

all_months_data.head()


# In[164]:


Hours=[hour for hour, df in all_months_data.groupby('hour')]
plt.plot(Hours, all_months_data.groupby('hour').count())
plt.xticks(Hours)
plt.xlabel("Hours")
plt.ylabel("Number of Sales")
plt.grid()
plt.show()


# In[ ]:




