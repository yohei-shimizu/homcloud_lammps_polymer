#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np


# In[35]:


dipole = np.loadtxt("dc_polar.txt", skiprows = 0)
cellvolume = np.loadtxt("cell_size.txt", skiprows = 0)


# In[36]:


polar = dipole / cellvolume
polar


# In[37]:


dc_ = polar / (1*10**9*8.85418782*10**(-12))
dc = dc_ + 1
dc


# In[38]:


cellsize = np.cbrt(cellvolume)  /10
cellsize


# In[39]:


cellsize_dc1 = np.append(cellsize, dc)
cellsize_dc1


# In[40]:


cellsize_dc2 = cellsize_dc1.reshape(-1,5)
cellsize_dc2


# In[41]:


cellsize_dc3 = np.mean(cellsize_dc2, 1)
cellsize_dc4 = cellsize_dc3.reshape(2,-1).T
cellsize_dc4


# In[42]:


cellsize_dc5 = np.std(cellsize_dc2, 1)
cellsize_dc6 = cellsize_dc5.reshape(2,-1).T
cellsize_dc7 = np.delete(cellsize_dc6, [0,],1)
cellsize_dc7


# In[43]:


cellsize_dc8 = np.append(cellsize_dc4, cellsize_dc7, axis =1)
cellsize_dc9 = np.append(cellsize_dc8, cellsize_dc7, axis =1)
cellsize_dc9


# In[44]:


np.savetxt('DC_result.dat', cellsize_dc9, header='DC,MI,polymer')


# In[ ]:




