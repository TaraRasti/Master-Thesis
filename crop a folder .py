#!/usr/bin/env python
# coding: utf-8

# In[30]:


from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp


# In[41]:


path = '/Users/taraapple/Downloads/ALZHEIMER/normal/sub-OAS30015/'
L = []
for i in range(len(os.listdir(path))):
    L.append(os.listdir(path)[i])


# In[50]:


A = {}
for i in range(256):
    filepath = path + L[i]
    A.update({ L[i] : image.imread(filepath)})


# In[51]:


R1 = []
for n in range(len(A)):
    l1=[]
    for i in range(A[L[n]].shape[0]):
        if len(np.unique(A[L[n]][i,:]<0.05))==1:
            l1.append(i)
    R1.append(l1)


# In[52]:


R2 = []
for n in range(len(A)):
    l2=[]
    for j in range(A[L[n]].shape[1]):
        if len(np.unique(A[L[n]][:,j]<0.05))==1:
            l2.append(j)
    R2.append(l2)


# In[53]:


for n in range(len(A)):
    A[L[n]] = np.delete(A[L[n]], (R1[n]), axis=0)
    A[L[n]] = np.delete(A[L[n]], (R2[n]), axis=1)


# In[54]:


I = []
for a in range(256):
    if A[L[a]].shape==(0,0):
        I.append(L[a])
I        


# In[37]:


for i in range(256):
        filepath = path + L[i]
        plt.imsave(filepath, A[L[i]], format='png', cmap = 'gray')


# In[55]:


for i in range(256):
    
    if L[i]!= I:
        filepath = path + L[i]
        plt.imsave(filepath, A[L[i]], format='png', cmap = 'gray')

