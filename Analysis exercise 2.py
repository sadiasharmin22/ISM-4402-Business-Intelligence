#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imorting the data Set
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r'C:/Users/sadia/OneDrive/Desktop/Business intelligence/datasets/axisdata.csv'
df = pd.read_csv(Location)
df.head()


# In[4]:


# 1. Average Car sold per month
df['Cars Sold'].mean()


# In[5]:


# 2. Max cars sold per month
df['Cars Sold'].max()


# In[6]:


# 3. Min cars sold per month 
df['Cars Sold'].min()


# In[15]:


# 4. Average cars sold per month by gender 
#intialzation of pivot table with target value "Gender"
pd.pivot_table(df, index=['Gender'])


# In[16]:


pd.pivot_table(df,
 values=['Cars Sold'],
 index=['Gender'])


# In[18]:


#5. Average hours worked by people selling more than three cars per month
df2 = df.loc[df['Cars Sold'] > 3]
pd.pivot_table(df2,
 index=['Gender'],
 aggfunc='mean',
 values=['Hours Worked'],
 margins='True')


# In[19]:


# 6. Average years of experience
df['Years Experience'].mean()


# In[20]:


# 7.Average years of experience for selling more than three cars per month
df2 = df.loc[df['Cars Sold'] > 3]
pd.pivot_table(df2,
 index=['Gender'],
 aggfunc='mean',
 values=['Years Experience'],
 margins='True')


# In[22]:


# 8.Average Cars sold per month sorted by whether they have had sales training 
#intialzation of pivot table with target value "sales training"
pd.pivot_table(df, index=['SalesTraining'])


# In[ ]:


#ANSWER
# The realtionship between how many hours worked and how many cars sold indicates whther that person is good sales person
# and also whether they had sales training .
#the average on the number five shows the how many hours worked and sold more than 3 cars, and its 34.7 at most part.


# In[35]:


#creating dataset by pulling in the first five names and how many hours worked 
#creating a bar graph
import matplotlib.pyplot as plt
import pandas as pd
names = ['Jada','Nicole','Tanya','Ronelle','Brad']
Hrs = [39,46,42,38,33]
Relation = zip(names, Hrs)
df = pd.DataFrame(data = Relation,
 columns=['Lname', 'Hours Worked'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[40]:


#importing the data again to make histogram
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r'C:/Users/sadia/OneDrive/Desktop/Business intelligence/datasets/axisdata.csv'
df = pd.read_csv(Location)
df.head()


# In[39]:


df.hist()


# In[ ]:




