#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from pandas .plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## DATA CLEANING_Dataset_1_Airbnb and Visualization

# In[3]:


df = pd.read_csv('Airbnb_Dataset.csv')


# In[4]:


dh = pd.read_csv('HR_Dataset.csv')


# In[5]:


df.shape


# In[8]:


df.head(2)


# In[9]:


df.tail(2)


# In[14]:


df.columns


# In[ ]:





# In[ ]:





# In[10]:


df.index


# In[11]:


# check for dimension
df.ndim


# In[12]:


# check for basic  information
df.info()


# In[15]:


# delete unnecessary coumns
df.drop(['reviews_per_month','calculated_host_listings_count'], axis=1, inplace= True)


# In[16]:


# delete the null amount values
df.dropna(inplace =True)


# In[17]:


df.shape


# In[18]:


# check all columns name

for i in df.columns:
    print(i)


# In[ ]:


# change data  tyype if required
# change the amount dtype fro folat to int

df['price']=df['price'].astype(int)


# In[ ]:


# to check statistics of data
df.describe()


# In[19]:


sns.set(rc={'figure.figsize':(6,4)})
plot = sns.countplot(x='room_type', data=df, palette='rocket')
for count in plot.containers:
    plot.bar_label(count)
plt.show()


# In[24]:


sns.boxplot(x=df['price'], color='lightgreen')
plt.title('Box Plot of Airbnb data')
plt.xlabel('Value')
plt.show()


# In[27]:


sns.barplot(x=df['room_type'], y=df['price'], palette='pastel')
plt.title('Bar Plot of airbnb')
plt.xlabel('room type')
plt.ylabel('price')
plt.show()


# In[29]:


sns.violinplot(data=df['number_of_reviews'], color='lightblue')
plt.title('Violin Plot of Random Data')
plt.ylabel('Value')
plt.show()


# ## Data cleaning Data Set 2 HR Dataset a nd Visualization

# In[31]:


dh.head(2)


# In[32]:


dh.tail()


# In[ ]:


dh.shape
dh.column
dh.index


# In[34]:


df.ndim


# In[36]:


df.info()


# In[37]:


df.describe()


# In[38]:


dh.dropna(inplace =True)


# In[39]:


for i in dh.columns:
    print(i)


# In[40]:


sns.set(rc={'figure.figsize':(6,4)})
plot = sns.countplot(x='GenderID', data=dh, palette='rocket')
for count in plot.containers:
    plot.bar_label(count)
plt.show()


# In[41]:


sns.boxplot(x=dh['Salary'], color='lightgreen')
plt.title('Box Plot of Airbnb data')
plt.xlabel('Value')
plt.show()


# In[42]:


sns.set(rc={'figure.figsize':(6,4)})
plot = sns.countplot(x='EmpSatisfaction', data=dh, palette='rocket')
for count in plot.containers:
    plot.bar_label(count)
plt.show()


# In[45]:


sns.barplot(x=dh['Employee_Name'], y=dh['Absences'], palette='pastel')
plt.title('Bar Plot of airbnb')
plt.xlabel('room type')
plt.ylabel('price')
plt.show()


# In[49]:


# Sort the DataFrame by 'Absences' column in descending order
sorted_df = dh.sort_values(by='Absences', ascending=False)

# Select the top 5 rows
top_5 = sorted_df.head(15)

# Plot bar plot for the top 5 rows
sns.barplot(x=top_5['Employee_Name'], y=top_5['Absences'], palette='pastel')
plt.title('Top 5 Employees with Most Absences')
plt.xlabel('Employee Name')
plt.ylabel('Absences')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




