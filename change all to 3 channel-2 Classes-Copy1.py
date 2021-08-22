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
import imageio
import cv2


# # Demented

# In[2]:


L1 = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/data/ALZHEIMER/demented/'))):
    L1.append(os.listdir('/Users/taraapple/Downloads/data/ALZHEIMER/demented/')[i])


# In[3]:


L1[22]


# In[4]:


L1 = np.delete(L1, 22, axis=None)
L1


# In[5]:


path1 = []
for i in range(150):
    path1.append('/Users/taraapple/Downloads/data/ALZHEIMER/demented/' +  L1[i])


# In[6]:


path1


# # Normal

# In[7]:


L2 = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/data/ALZHEIMER/normal/'))):
    L2.append(os.listdir('/Users/taraapple/Downloads/data/ALZHEIMER/normal/')[i])


# In[8]:


L2[70]


# In[9]:


L2 = np.delete(L2, 70, axis=None)
L2


# In[10]:


path2 = []
for i in range(454):
    path2.append('/Users/taraapple/Downloads/data/ALZHEIMER/normal/' +  L2[i])


# In[11]:


path2


# # Save

# In[15]:


for i in range(len(path1)):
    for n in range(256):
    
        from matplotlib import image
        filepath = path1[i] + '/' + str(n) + path1[i][51:65] + '.png'
        image  = image.imread(filepath)
        if len(image.shape) > 2 and image.shape[2] == 4:
            img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        file_path =  '/Users/taraapple/Downloads/demented/' + str(n) + path1[i][51:65] + '.jpg'
        plt.imsave(file_path, img, format='jpg', cmap = 'gray')


# In[ ]:


for i in range(len(path2)):
    for n in range(256):
        from matplotlib import image
        filepath = path2[i] + '/' + str(n) + path2[i][49:61] + '.png'
        image  = image.imread(filepath)
        if len(image.shape) > 2 and image.shape[2] == 4:
            img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        file_path =  '/Users/taraapple/Downloads/normal/' + str(n) + path2[i][49:61] + '.jpg'
        plt.imsave(file_path, img, format='jpg', cmap = 'gray')


# In[ ]:




