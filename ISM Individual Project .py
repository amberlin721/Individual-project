#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "C:/Users/xlin8/OneDrive/Desktop/datasets/axisdata.csv"
df = pd.read_csv(Location)
df


# In[5]:


#1 average of cars sold per month
df['Cars Sold'].mean()


# In[6]:


#2 max of cars sold per month
df['Cars Sold'].max()


# In[7]:


#3 min od cars sold per month
df['Cars Sold'].min()


# In[18]:


#4 average car sold per month by gender
pd. pivot_table(df, values = ['Cars Sold'], index = ['Gender'], aggfunc = 'mean')


# In[20]:


#5 Average hours worked by people selling more than three cars per month
df1 = df.loc[df['Cars Sold'] > 3]
pd. pivot_table(df1, values = ['Hours Worked'], index = ['Lname'], aggfunc = 'mean')


# In[21]:


#6 average years of experience
df['Years Experience'].mean()


# In[22]:


#7 average years of experience for people selling more than three cars per month
df2 = df.loc[df['Cars Sold'] > 3]
pd. pivot_table(df2, values = ['Years Experience'], index = ['Lname'], aggfunc = 'mean')


# In[27]:


#8 average cars sold per month sorted by whether they have had sales training
df3 = df.loc[df['SalesTraining']=='Y']
pd. pivot_table(df1, values = ['Cars Sold'], index = ['Lname'], aggfunc = 'mean')


# In[28]:


#Question: What do you think is the best indicator of whether someone is a good salesperson?
#Base on my knowledge for marketing, the number is the best approvment.
#So that, I think that who sales the most of cars per month indicated he/she is a good salesperson. 
#To be a good salesperson, it can be effected by the year experience and sales training.
#Because the experience bring the confident for the person to do this job,
#The sales training educates the knowledge to the person that he/she will have better understanding on sale.


# In[29]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/xlin8/OneDrive/Desktop/datasets/axisdata.csv"
df = pd.read_csv(Location)
df. head()


# In[30]:


df.hist()


# In[31]:


df.hist(column='Cars Sold',by='Gender')


# In[33]:


df.hist(column='Cars Sold',by='SalesTraining')


# In[39]:


df.plot.scatter(x='Years Experience',y='Hours Worked')
plt.show()


# In[40]:


df.plot.scatter(x='Cars Sold',y='Hours Worked')
plt.show()


# In[53]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/xlin8/OneDrive/Desktop/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.plot(kind='bar')


# In[56]:


df2 = df.set_index(df['Gender'])
df2.plot(kind="bar")


# In[ ]:




