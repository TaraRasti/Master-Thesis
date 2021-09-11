#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp


# In[3]:


L1 = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/new/demented/'))):
    L1.append(os.listdir('/Users/taraapple/Downloads/new/demented/')[i])


# In[4]:


L1 = np.array(L1)
np.where(L1=='.DS_Store')


# In[6]:


L1 = np.delete(L1, 1140, axis=None)


# In[107]:


path1 = []
for i in range(len(L1)):
    path1.append('/Users/taraapple/Downloads/new/demented/' +  L1[i])


# In[183]:


L2 = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/new/normal/'))):
    L2.append(os.listdir('/Users/taraapple/Downloads/new/normal/')[i])


# In[184]:


len(L2)


# In[185]:


L2 = np.array(L2)


# In[187]:


np.where(L2=='.DS_Store')


# In[188]:


L2 = np.delete(L2, 3480, axis=None)


# In[189]:


path2 = []
for i in range(len(L2)):
    path2.append('/Users/taraapple/Downloads/new/normal/' +  L2[i])


# In[190]:


def row(x, inx):
    z = np.zeros((1, x.shape[1], 3))

    if inx%2==0:
        for i in range(np.int(inx/2)):
            x = np.concatenate((z, x), axis=0)
        for j in range(np.int(inx/2)):
            x = np.concatenate((x, z), axis=0)
    if inx%2==1:
        for i in range(np.int(inx/2)):
            x = np.concatenate((z, x), axis=0)
        for j in range(np.int(inx/2) + 1):
            x = np.concatenate((x, z), axis=0)
    return x
        


# In[191]:


def col(x, inx):
    z = np.zeros((x.shape[0], 1, 3))

    if inx%2==0:
        for i in range(np.int(inx/2)):
            x = np.concatenate((z, x), axis=1)
        for j in range(np.int(inx/2)):
            x = np.concatenate((x, z), axis=1)
    if inx%2==1:
        for i in range(np.int(inx/2)):
            x = np.concatenate((z, x), axis=1)
        for j in range(np.int(inx/2) + 1):
            x = np.concatenate((x, z), axis=1)
    return x


# In[182]:


from matplotlib import image
for k in range(len(path1)):
    filepath = path1[k]
    x  = image.imread(filepath)
    d1 = 228 - x.shape[0]
    x1 = row(x, d1)
    d2 = 228 - x.shape[1]
    x2 = col(x1, d2)
    X = x2/255
    file_path =  '/Users/taraapple/Downloads/Demented1/' + L1[k]
    plt.imsave(file_path, X, format='jpg', cmap = 'gray')


# In[ ]:


from matplotlib import image
for k in range(len(path2)):
    filepath = path2[k]
    x  = image.imread(filepath)
    d1 = 228 - x.shape[0]
    x1 = row(x, d1)
    d2 = 228 - x.shape[1]
    x2 = col(x1, d2)
    X = x2/255
    file_path =  '/Users/taraapple/Downloads/Normal1/' + L2[k]
    plt.imsave(file_path, X, format='jpg', cmap = 'gray')


# In[ ]:




