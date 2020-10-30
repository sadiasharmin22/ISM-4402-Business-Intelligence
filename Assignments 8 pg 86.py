#!/usr/bin/env python
# coding: utf-8

# In[1]:


# What if, instead of highlighting the worst student, we put a spotlight on
# the best one? Let's rotate the chart and change the settings so we are
# highlighting John instead of Mel
# Pie Charting Your Dataset
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df


# In[4]:


#Creating New Column
# cell, we will create a column to show the total violations or demerits per
# student
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df


# In[14]:


#Creating a Customized Pie Chart
plt.pie(df['TotalDemerits'],
 labels=df['Names'],
 explode=(0,0,0,0.70,0),
 startangle=180,
 autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[ ]:





# In[ ]:




