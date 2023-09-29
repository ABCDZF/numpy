#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
list_ = [ '1' , '2' , '3' , '4', '5' ]
array_list = np.array(object = list_)


# Q1

# In[5]:


print(type(list))
print(type(array_list))


# Q2

# In[14]:


for element in list_: 
    print(type(element))
for element in array_list:
    print(type(element))


# Q3

# In[15]:


array_list = np.array(object = list_ , dtype = int)
for element in list_:
    print(type(element))
for element in array_list:
    print(type(element))


# In[16]:


import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)


# Q4

# In[20]:


np.shape(num_list)
np.shape(num_array)


# In[23]:


print(np.size(num_array))
print(np.size(num_list))


# Q5

# In[27]:


print(np.zeros((3,3)))


# Q6

# In[30]:


print(np.eye(5))


# In[ ]:




