#!/usr/bin/env python
# coding: utf-8

# ## 1. soru

# In[18]:


import numpy as np
x=np.arange(1,200,2).reshape(10,10)
x


# ## 2. Soru

# In[30]:


import numpy as np
def Birkenar(x,y) :
    z = np.ones((x,y))
    z[1:x-1,1:y-1]=[0]
    return z


# In[31]:


Birkenar(5,6)


# In[ ]:




