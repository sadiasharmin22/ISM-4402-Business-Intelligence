#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Your Turn!!! (Assignment 8)
# Can you create an age histogram categorized by gender?
#Importing Dataset from CSV File
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r'C:/Users/sadia/OneDrive/Desktop/Business intelligence/datasets/gradedata.csv'
df = pd.read_csv(Location)
df.head()


# In[4]:


#Categorized age Histogram by gender
df.hist(column="age", by="gender")


# In[ ]:




