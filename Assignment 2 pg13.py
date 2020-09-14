#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob


# In[4]:


all_data = pd.DataFrame()
for f in glob.glob("C:/Users/sadia/OneDrive/Desktop/Business intelligence/datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[5]:


df.head()


# In[ ]:




