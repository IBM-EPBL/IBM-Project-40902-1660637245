#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[1]:


s = "Hi there Sam!"


# In[2]:


s.split()


# ## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[3]:


planet = "Earth"
diameter = 12742


# In[4]:


print("The diameter of {} is {} kilometers.".format(planet,diameter))


# ## 3. In this nest dictionary grab the word "hello"

# In[6]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[7]:


d['k1'][3]['tricky'][3]['target'][3]


# # Numpy

# In[8]:


import numpy as np


# ## 4.1 Create an array of 10 zeros?
# 
# > Indented block
# 
# 
# ## 4.2 Create an array of 10 fives?

# In[10]:


array_zeros=np.zeros(10)
print(array_zeros)


# In[12]:


array_fives=np.ones(10)*5
print(array_fives)


# ## 5. Create an array of all the even integers from 20 to 35

# In[13]:


array=np.arange(20,35,2)
print(array) 


# :## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[14]:


x =  np.arange(0, 9).reshape(3,3)
print(x)


# ## 7. Concatenate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[15]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate((a, b), axis=0)


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[16]:


import pandas as pd


# In[18]:


data = {'Name': ['AR','Arsh','Aira'],
        'Age': [21, 25, 23]}

df = pd.DataFrame(data)
print(df)


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[19]:


per1 = pd.date_range(start ='1-1-2023', 
         end ='10-02-2023')
  
for val in per1:
    print(val)


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[23]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df=pd.DataFrame(lists)
print(df)


# In[ ]:




