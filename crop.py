#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp


# In[11]:


def crop(path):
    L = []
    for i in range(len(os.listdir(path))):
        L.append(os.listdir(path)[i])

    A = {}
    for i in range(256):
        filepath = path + L[i]
        A.update({ L[i] : image.imread(filepath)})
    
    R1 = []
    for n in range(len(A)):
        l1=[]
        for i in range(A[L[n]].shape[0]):
            if len(np.unique(A[L[n]][i,:]<0.05))==1:
                l1.append(i)
        R1.append(l1)
        
    R2 = []
    for n in range(len(A)):
        l2=[]
        for j in range(A[L[n]].shape[1]):
            if len(np.unique(A[L[n]][:,j]<0.05))==1:
                l2.append(j)
        R2.append(l2)
        
    for n in range(len(A)):
        A[L[n]] = np.delete(A[L[n]], (R1[n]), axis=0)
        A[L[n]] = np.delete(A[L[n]], (R2[n]), axis=1)
        
    I = []
    for a in range(256):
        if A[L[a]].shape==(0,0):
            I.append(L[a])
    
    if len(I)==1:
        for i in range(256):
        
            if L[i]!=I[0]:
                filepath = path + L[i]
                A[L[i]]  = A[L[i]].copy(order='C')
                plt.imsave(filepath, A[L[i]], format='png', cmap = 'gray')
                
    else:
        print('error:',L[i])


# In[52]:


L = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/demented/'))):
    L.append(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/demented/')[i])


# In[53]:


L


# In[54]:


path = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/demented'))):
    path.append('/Users/taraapple/Downloads/thesis/ALZHEIMER/demented/' +  L[i])


# In[55]:


path[26]


# In[56]:


path = np.delete(path, 26, axis=None)


# In[57]:


path


# In[58]:


for i in range(len(path)):
    crop(path[i] + '/')
    


# In[59]:


L = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/mci/'))):
    L.append(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/mci/')[i])


# In[60]:


path = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/mci'))):
    path.append('/Users/taraapple/Downloads/thesis/ALZHEIMER/mci/' +  L[i])


# In[63]:


path[4]


# In[64]:


path = np.delete(path, 4, axis=None)


# In[65]:


for i in range(len(path)):
    crop(path[i] + '/')


# In[19]:


L = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/normal'))):
    L.append(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/normal')[i])


# In[20]:


path = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/thesis/ALZHEIMER/normal'))):
    path.append('/Users/taraapple/Downloads/thesis/ALZHEIMER/normal/' +  L[i])


# In[21]:


path


# In[22]:


path[93]


# In[23]:


path = np.delete(path, 93, axis=None)


# In[24]:


len(path)


# In[25]:


for i in range(578):
    crop(path[i]+'/')

