#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
df


# In[31]:


df.loc[df['Grades'] >= 0]


# In[32]:


df.loc[(df['Grades'] <= 0),'Grades'] = 0


# In[33]:


df.head()


# In[ ]:





# In[ ]:




