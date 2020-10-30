#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create a scatter plot of the hours and grade data in datasets/gradedata.csv.
# Do you see a pattern in the data?
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = r'C:/Users/sadia/OneDrive/Desktop/Business intelligence/datasets/gradedata.csv'
df = pd.read_csv(Location)
df.head()


# In[21]:


#Creating a Scatter Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.hours, df['grade'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




